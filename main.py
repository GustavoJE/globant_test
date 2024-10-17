from fastapi import FastAPI, UploadFile, File, Response, HTTPException
from fastapi.responses import FileResponse
from helpers.functions import write_data
from config import HOST, USER, PASSWORD, DB
import pymysql
import pandas as pd

app = FastAPI()

conn = pymysql.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    db=DB,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

database_credentials = {
    "host": HOST,
    "user": USER,
    "password": PASSWORD,
    "database": DB
}

@app.post("/employees")
async def upload_employees(file: UploadFile = File(..., description="Must be a valid CSV file")):
    
    """Uploads employee data to destination database"""
    
    write_data("employees", file, conn)
    return Response(status_code=200)

@app.post("/departments")
async def upload_departments(file: UploadFile = File(..., description="Must be a valid CSV file")):
    
    """Uploads department data to destination database"""
    
    write_data("departments", file, conn)
    return Response(status_code=200)

@app.post("/jobs")
async def upload_jobs(file: UploadFile = File(..., description="Must be a valid CSV file")):
    
    """Uploads job data to destination database"""
    
    write_data("jobs", file, conn)
    return Response(status_code=200)

@app.get("/employees_hired_by_quarter")
async def employees_hired_by_quarter():
    
    """Get the number of employees hired for each job and department during 2021 divided by quarter"""
    
    query = """
        SELECT 
            d.department AS department,
            j.job AS job,
            COUNT(CASE WHEN QUARTER(e.datetime) = 1 THEN 1 END) AS Q1,
            COUNT(CASE WHEN QUARTER(e.datetime) = 2 THEN 1 END) AS Q2,
            COUNT(CASE WHEN QUARTER(e.datetime) = 3 THEN 1 END) AS Q3,
            COUNT(CASE WHEN QUARTER(e.datetime) = 4 THEN 1 END) AS Q4
        FROM 
            employees e
        JOIN 
            jobs j ON e.job_id = j.id
        JOIN 
            departments d ON e.department_id = d.id
        WHERE 
            YEAR(e.datetime) = 2021
        GROUP BY 
            d.department, j.job
        ORDER BY 
            d.department, j.job;
        """
    
    try:
        # Connect to the database using PyMySQL
        connection = pymysql.connect(**database_credentials)

        # Execute the query and fetch the data into a DataFrame
        df = pd.read_sql(query, connection)

        # Save the DataFrame to a CSV file
        df.to_csv("employees_hired_by_department.csv", index=False)

        # Return the CSV file as a response
        return FileResponse("employees_hired_by_department.csv", media_type='text/csv', filename='employees_hired_by_job_and_department.csv')

    except pymysql.MySQLError as err:
        raise HTTPException(status_code=500, detail=f"Database connection error: {err}")
    

@app.get("/employees_hired_by_department_greater_than_mean")
async def employees_hired_by_department_greater_than_mean():
    
    """Get the ids, name of department and number of employees hired for each department during 2021 for departments that hired more than the mean of all hired employees"""
    
    query = """
        SELECT 
            d.id AS id,
            d.department AS department,
            COUNT(e.id) AS hired
        FROM 
            employees e
        JOIN 
            departments d ON e.department_id = d.id
        WHERE 
            YEAR(e.datetime) = 2021
        GROUP BY 
            d.id, d.department
        HAVING 
            COUNT(e.id) > (
                SELECT AVG(employee_count)
                FROM (
                    SELECT COUNT(e2.id) AS employee_count
                    FROM employees e2
                    WHERE YEAR(e2.datetime) = 2021
                    GROUP BY e2.department_id
                ) AS subquery
            )
        ORDER BY hired DESC;
        """
    
    try:
        # Connect to the database using PyMySQL
        connection = pymysql.connect(**database_credentials)

        # Execute the query and fetch the data into a DataFrame
        df = pd.read_sql(query, connection)

        # Save the DataFrame to a CSV file
        df.to_csv("departments_the_hired_more_employees_than_mean.csv", index=False)

        # Return the CSV file as a response
        return FileResponse("departments_the_hired_more_employees_than_mean.csv", media_type='text/csv', filename='departments_the_hired_more_employees_than_mean.csv')

    except pymysql.MySQLError as err:
        raise HTTPException(status_code=500, detail=f"Database connection error: {err}")
