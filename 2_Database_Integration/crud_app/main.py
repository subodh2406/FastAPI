# This is where the API is defined, exposing endpoints for the end users•
# Denotes the entry point of the API server•
# Defines the FastAPI app and all associated routes

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from typing import List
import models, schemas, crud
# Create all tables in the database based on the models defined with Base.
# Base.metadata keeps track of all model/table definitions.
# create_all(bind=engine) ensures each table exists in the database (does nothing if it already exists).
Base.metadata.create_all(bind=engine)

app = FastAPI()#Create a FastAPI app called app that will handle all incoming web requests and route them to the functions I define.


# dependency with the DB
# Dependency Injection is a way to give a function or class the resources it needs without having it create them itself.
# Purpose:
# FastAPI uses dependency injection to automatically provide resources to your endpoint functions.
# get_db is a dependency that provides a database session to any route that needs it.
# 
# Step by step:
# db = SessionLocal()
# - SessionLocal is a SQLAlchemy session factory.
# - Calling SessionLocal() creates a new database session.
# - This session lets you query, insert, update, or delete records.
#
# try: yield db
# - yield makes this a generator function.
# - FastAPI treats generators in dependencies specially:
#   - It gives the yielded db to the endpoint function.
#   - Once the request is done, execution continues after the yield.
#
# finally: db.close()
# - Ensures the database session is closed after the request, even if an exception occurs.
# - This prevents database connection leaks, which can crash your app if too many connections stay open.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# endpoints
# 1. create an employee
# db: Session = Depends(get_db)
# db → This is a variable that will hold a database session (SQLAlchemy session).
# Session → The type hint; helps with code completion and static typing.
# Depends(get_db) → FastAPI dependency injection.

@app.post('/employees', response_model=schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)


# 2. get all employees
@app.get('/employees', response_model=List[schemas.EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)


# 3. get specific employee
@app.get('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail='Employee Not Found')
    return employee



# 4. update an employee
@app.put('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def update_employee(emp_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db, emp_id, employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail='Employee Not Found')
    return db_employee


# 5. delete an employee
@app.delete('/employees/{emp_id}', response_model=dict)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.delete_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail='Employee Not Found')
    # return employee
    return {'detail': 'Employee Deleted'}