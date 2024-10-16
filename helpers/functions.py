from fastapi import HTTPException
import pandas as pd
import numpy as np

def write_data(table, file, conn):
          
    for batch in pd.read_csv(file.file, header=None, chunksize=1000):
        batch = batch.replace(np.nan, None)
           
        match table:
            case "employees":
                try:
                    with conn.cursor() as cursor:
                        for index, row in batch.iterrows():
                            print(row.iloc[0], row.iloc[1], row.iloc[2], row.iloc[3], row.iloc[4])
                            cursor.execute("INSERT INTO employees (id, name, datetime, department_id, job_id) VALUES (%s, %s, %s, %s, %s)", (row.iloc[0], row.iloc[1], row.iloc[2], row.iloc[3], row.iloc[4]))
                            conn.commit()

                except:
                    raise HTTPException(400, f"Writing to database has failed")

            case "departments":
                try:
                    with conn.cursor() as cursor:
                        for index, row in batch.iterrows():
                            print(row.iloc[0], row.iloc[1])
                            cursor.execute("INSERT INTO departments (id, department) VALUES (%s, %s)", (row.iloc[0], row.iloc[1]))
                            conn.commit()

                except:
                    raise HTTPException(400, f"Writing to database has failed")

            case "jobs":
                try:
                    with conn.cursor() as cursor:
                        for index, row in batch.iterrows():
                            print(row.iloc[0], row.iloc[1])
                            cursor.execute("INSERT INTO jobs (id, job) VALUES (%s, %s)", (row.iloc[0], row.iloc[1]))
                            conn.commit()

                except:
                    raise HTTPException(400, f"Writing to database has failed")

    print("Data inserted successfully")
    