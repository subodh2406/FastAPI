# • Helps setup database connection and provide foundational components for ORM
# • Centralizes DB setup, making it reusable across the app for sessions and models

# create_engine():
# Establishes the connection to the database
# Here, it connects to a SQLite file named test.db○

# connect_args:
# SQLite-specific to allow connection sharing across threads○

# sessionmaker:
# Helps create new database sessions○
# Each session represents a transactional scope to the DB

# autoflush=False:○
# SQLAlchemy will not automatically flush changes to the DB unless explicitly committed
# or refreshed

# autocommit=False:○
# Disables automatic commit after each query▪
# Commit manually to control transactions▪

# declarative_base():
# Creates a base class for models to inherit from, linking the Python classes with DB tables



# sqlite:///./test.db
# │
# ├── sqlite  → Database type
# ├── ///     → Relative file path indicator
# └── ./test.db → File name in current folder
# 🔹 What It Means
# sqlite → Use SQLite database
# ./ → Current directory
# test.db → Database file name
# So this creates (or connects to) a file:
# test.db



# 3️⃣ What is connect_args?
# connect_args={'check_same_thread': False}
# This is specific to SQLite.
# By default:
# SQLite allows only one thread to use a connection.
# But:
# FastAPI can handle multiple requests at the same time (multi-threaded).

# So we set:
# check_same_thread=False
# Which means:
# “Allow the database connection to be used across multiple threads.”
# ⚠️ This is needed only for SQLite.
# You don’t use this for PostgreSQL or MySQL.


# sessionmaker is a factory function from SQLAlchemy.
# It creates a Session class that we use to generate database sessions.
# SessionLocal is a session factory created using SQLAlchemy's sessionmaker.
# It does NOT create a database session immediately.
# Instead, it creates a "Session class" that we can use to generate sessions.

# bind=engine
# This connects the session to the database engine.
# Without this, the session would not know which database to communicate with.

# autoflush=False
# Prevents SQLAlchemy from automatically sending changes to the database
# before executing queries. Changes will only be sent when we explicitly commit.

# autocommit=False
# Disables automatic committing of changes.
# We must manually call db.commit() to permanently save changes to the database.

# To create and use a session:
# db = SessionLocal()
# db.add(obj)
# db.commit()
# db.close()



# 🔹 1️⃣ autoflush=False
# What is flush?
# Flush means:
# Sending pending changes from memory to the database (but not permanently saving them).

# Example:

# db.add(user)

# At this moment:
# The object is in memory
# Not yet sent to database

# If autoflush=True:
# SQLAlchemy automatically sends changes before running a query.

# If autoflush=False:
# It waits until you manually commit or flush.

# Why use autoflush=False?
# ✔ Gives you more control
# ✔ Prevents unexpected automatic database writes
# ✔ Makes debugging easier




# 🔹 2️⃣ autocommit=False
# What is commit?
# Commit means:
# Permanently saving changes to the database.

# Example:
# db.add(user)
# db.commit()

# If autocommit=True:
# Every change is automatically saved immediately.

# If autocommit=False:
# You must manually call:

# db.commit()
# Why use autocommit=False?

# ✔ Prevents accidental data saving
# ✔ Allows transaction control
# ✔ Safer for real applications




from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)
# engine is The main connection between your Python app and the database.

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base() #eclarative_base() creates a base class for all your ORM models.


