# Globant Test Overview #

This repository contains the code corresponding to the 2 code challenges proposed by Globant for the Python Developer role. 

### db_migration.py ###
The first challenge consists of a Python script that is used for DB migration. We are asked to create a local REST API that must receive historical data from a CSV file and upload this data to the new DB through batch transactions of up to 1000 rows with one request. 

in order to run this code, first install the dependencies:

```sh
$ pip install -r requirements.txt
```

Next, in the db_migration.py file, change the DB credentials on line 7

After this, run the uvicorn server:
```sh
HOST=host USER=user PASSWORD=password DB=db uvicorn db_migration:app --reload
```
Make sure to change the values corresponding to the database you want to connect to.

Then, open a browser tab and enter the following:
```
http://127.0.0.1:8000/docs
```

Finally, use the Swagger UI to try each endpoint.


