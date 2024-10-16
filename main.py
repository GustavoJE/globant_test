from fastapi import FastAPI, UploadFile, File, HTTPException
from helpers.functions import write_data
import pymysql

app = FastAPI()

conn = pymysql.connect(
    host="sql10.freesqldatabase.com",
    user="sql10738151",
    password="BepAQFKybr",
    db="sql10738151",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

@app.post("/upload/employees")
async def upload_employees(file: UploadFile = File(...)):
    write_data("employees", file, conn)
    return

@app.post("/upload/departments")
async def upload_departments(file: UploadFile = File(...)):
    write_data("departments", file, conn)
    return

@app.post("/upload/jobs")
async def upload_jobs(file: UploadFile = File(...)):
    write_data("jobs", file, conn)
    return
