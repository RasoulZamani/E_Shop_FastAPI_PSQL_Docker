# E Shop by FastAPI, Postgresql and Docker

## About

This code is implementation of simple e-shop as a task for Lagrange Co. in **FastAPI** framework.
for ORM it use **SQLAlchemy**, and database is **postgresql**.
more information of task can be seen in [task_deceleratiom](./doc_resource/task_deceleration.pdf)

---

## Features

In this app three models created in database:**Users, Product and Order**. You can see them in the app/db_models.py file.
Each order contsind foreign key to user and products to implementing 1-to-many relationship between them.
**pydantic schemas** used for validate inut and output of endpointd properly. these schemas can be found in app/schema_models.py file.

## Code Structure

For better organization of the code, cruds (create, read, update and delete) related to each model was written in seprated file and gather together in `app/cruds` directory. Endpoints in similar way are in `app/routers`.
Essential authentication functions are in `app/security.py` and database scripts written in `app/db.py` file.

---

## Installation and Run

After cloning this repository you have two options:

### Option One:

Go to the `NoDocker` directory and you can use virtual environment and install neccesary pakages by:
`pip install -r requirements.txt`
Finally run app: `python main.py`.
Notice in this case it use sqlite as a database.

### Option Two: Docker and Postgresql

Just run:
`sudo docker compose up -d --build`
It will install requirements and create image from `Dockerfile` for app, then based on `docker-compose.yml`, create service that has two container: web (fastAPI app) and db (psql database).

---

## See Results

after installing and running , go to the browser and type:
`http://localhost:8000/docs`
for accessing

Also for automated testing, in the /app directory after installing pytest, type `pytest` and some tests will be pass. more tests can be added based on feuture situations.

---

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

---
