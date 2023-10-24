# E Shop by FastAPI, Postgresql and Docker

## About
This code is implementation of simple e-shop as a task for Lagrange Co. in **FastAPI** framework.
for ORM it use **SQLAlchemy**, and database is **postgresql**.

******************************************************************
## features 


******************************************************************
## Run
After cloning this repository you have two options:

### Option One:
Go to the v-sqlite and  you can use virtual environment and install neccesary pakages by:
 `pip install -r requirements.txt` 
and finally run app:  `python main.py`.
Notice in this case it use sqlite as a database.

### Option Two: Docker and Postgresql
Just run:
 `sudo docker compose up -d --build`

******************************************************************
## See Results
after runing, go to the browser and type:
 `http://localhost:8000\docs`
for accessing 


******************************************************************
# Dockerization

## Dockerfile
```
```

## docker-compose
```
```

As it was said, for runing this app by docker just typy in the root of project:
`sudo docker compose up -t --build`
if there was a problem you can see logs of servece by
`sudo docker compose logs`
and logs of any related container in similar way to debug the issue.

## docker swarm
```
```

******************************************************************
## Test
for testing in the app/ directory after installing pytest, type `pytest` and some tests will be pass.

