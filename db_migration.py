from fastapi import FastAPI, UploadFile, File, Response
from helpers.functions import write_data
from config import HOST, USER, PASSWORD, DB
import pymysql

app = FastAPI()

conn = pymysql.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    db=DB,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

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
