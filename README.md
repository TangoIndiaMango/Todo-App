# Todo App
## About the Stack

A Todo application.
This app is written in Python with Flask and SQLAlchemy, highlights and lessons learnt from Udacity's Full Stack Web Developer Nanodegree program.

## A. Dependency
In order to run this app, the following dependencies must have been already installed:
1. Postgres. 
 * Start manually: `psql -U postgres` Windows Users, Linux
 * Start manually: `psql postgres` MacOs
 
2. Flask

## B. Database 
The database relations `todos(id, description, complete, list_id)` and `todolists(id, name)` must have been already created in Postgres. We have assumed that the Postgres is running on default port 5432.

* `dropdb joint -p 5432 && createdb joint -p 5432` 
* Open the database prompt - `psql -p 5432`
* Connect to the database - `\c joint` 
* Displays the tables in the database `\dt` 
* Displays the schema of the 'todos' table `\d todos`  

You can insert a few rows in the table.

## C. Steps to Run the App: 
* `python3 -m venv env` set the virtual environment for Pyhton 
* `source env/bin/activate` activate the venv
* `python -m pip install -r requirements.txt` to install dependencies. For Mac users, if you face difficulty in installing the `psycopg2`, you may consider intalling the `sudo brew install libpq` before running the `requirement.txt`. 
* `python3 app.py` to run the app (http://127.0.0.1:5000/ or http://localhost:5000)
* `deactivate` de-activate the virtual environment

