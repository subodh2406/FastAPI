# efines Pydantic models (schemas) for request validation and response formatting•
# Promotes data consistency and validation against invalid inputs


# 🔹 schemas.py → Data Validation & API Structure
# This file contains Pydantic models.
#
# Example:
# class EmployeeCreate(BaseModel):
#     name: str
#     email: EmailStr
#
# Purpose:
# - Validates request data
# - Defines response structure
# - Controls what the user can send
# - Controls what the user receives
#
# 👉 schemas.py talks to the API (client).


from pydantic import BaseModel, EmailStr
# from typing import Optional


class EmployeeBase(BaseModel):
    name: str
    email: EmailStr


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    pass


class EmployeeOut(EmployeeBase):
    id: int


    class Config:
        orm_mode = True
        # orm_mode = True allows Pydantic to read data directly
        # from SQLAlchemy ORM model objects.
        # Without this, FastAPI cannot convert a SQLAlchemy model
        # into this Pydantic schema automatically.