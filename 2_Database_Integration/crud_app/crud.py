# crud.py is:
# The file where all database operations (Create, Read, Update, Delete) are written.
# It keeps database logic separate from API logic.

from sqlalchemy.orm import Session
import models, schemas

#It fetches all employees from the database
def get_employees(db: Session):
    return db.query(models.Employee).all()


# 🔹 What This Function Does
# This function fetches a single employee from the database using the employee ID.

# 🔹 Parameters
# db: Session
#   - Database session (connection to the database).
# emp_id: int
#   - The ID of the employee we want to retrieve.
def get_employee(db: Session, emp_id: int):
    return (
        db
        .query(models.Employee)
        .filter(models.Employee.id == emp_id)
        .first()
    )


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(
        name=employee.name, email=employee.email
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def update_employee(db: Session, emp_id: int, employee: schemas.EmployeeUpdate):
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_employee:
        db_employee.name = employee.name
        db_employee.email = employee.email
        db.commit()
        db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, emp_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee
# db.delete() requires a SQLAlchemy model object.
# It cannot delete using just an ID.
# So we must first query the object, then delete it.
# After delete():
# - The database row is removed.
# - The Python object still exists in memory.
# - refresh() cannot be used because the row no longer exists.



# 🔹 What is db.refresh()?
# db.refresh(db_employee)
#
# It means:
# - Go to the database again
# - Get the latest data for this row
# - Update the Python object with that data

# 🔹 Why Do We Need It?
#
# 🗄 Database = Real storage
# 🧠 Python object = Copy in memory
#
# After:
# db.commit()
#
# The database is updated ✅
# But the Python object might still have old values ❗
#
# So we use:
# db.refresh(db_employee)
#
# To sync the Python object with the database.

# 🔥 Example (Create Case)
#
# Before commit:
# db_employee = Employee(name="John", email="john@mail.com")
#
# At this moment:
# db_employee.id = None
#
# After:
# db.add(db_employee)
# db.commit()
#
# Database generates:
# id = 1
#
# But the Python object may not yet reflect this.
#
# So:
# db.refresh(db_employee)
#
# Now:
# db_employee.id = 1
#
# Now the Python object matches the database.

# 🔥 Important Understanding
# After deletion:
# 🗄 Database row → ❌ removed
# 🧠 Python object → ✅ still exists in memory