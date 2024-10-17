# Globant Test Overview #

This repository contains the code corresponding to the 2 code challenges proposed by Globant for the Python Developer role. 

### First challenge ###
The first challenge consists of a Python script that is used for DB migration. We are asked to create a local REST API that must receive historical data from a CSV file and upload this data to the new DB through batch transactions of up to 1000 rows with one request. 

in order to run this code, first install the dependencies:

```sh
$ pip install -r requirements.txt
```

After this, run the SQL docker container:
```sh
docker-compose up -d
```

Now we can run the uvicorn server using the following command:

```sh
HOST=localhost USER=root PASSWORD=12345678 DB=mysql uvicorn main:app --reload
```

Then, open a browser tab and enter the following:
```
http://127.0.0.1:8000/docs
```

Finally, use the Swagger UI to try each endpoint.

### Second challenge ###
The second challenge requires us to get some metrics from the data that we previously stored. First we need an endpoint that returns the number of hired employees for each department and job divided by each quarter of the year 2021. The second endpoint returns the id, name and ammount of hired employees for each department that hired more employees than the mean of employees hired during 2021 for all departments.     

These endpoints become online once the uvicorn server is up and running.

### Accesing the database ###
The created database can be accessed using the container itself:
```sh
docker exec -it mysql bash
```
and then logging into the DB:
```sh
mysql -h 127.0.0.1 -u root -P 3306 -p
```

or by using an external software such as DbVisualizer.


