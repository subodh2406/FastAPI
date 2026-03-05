# Defines the Employee model, mapping the Python class to the employees table in the DB

# 🔹 models.py → Database Structure
# This file contains SQLAlchemy ORM models.
#
# Example:
# class Employee(Base):
#     __tablename__ = "employees"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     email = Column(String)
#
# Purpose:
# - Defines database tables
# - Defines columns
# - Defines constraints (primary key, unique, etc.)
# - Controls how data is stored in the database
#
# 👉 models.py talks to the database.



from sqlalchemy import Column, Integer, String
from database import Base
# Base is the parent class created using:
# Base = declarative_base()

# Base acts as the foundation for all ORM models.

# When we write:
# class Employee(Base):

# We are telling SQLAlchemy:
# - This class represents a database table.
# - Track this model in Base.metadata.
# - Map this Python class to the database table.

# Without inheriting from Base,
# SQLAlchemy will NOT treat the class as a database table.
class Employee(Base):
    __tablename__ = 'employees' # __tablename__ defines the name of the table in the database.
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)