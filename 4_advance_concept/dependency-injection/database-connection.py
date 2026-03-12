# Dependency Injection is a design pattern where a function or class receives the things it needs (dependencies) from outside instead of creating them itself.
from fastapi import FastAPI, Depends

app = FastAPI()


# dependency function
def get_db():
    db = {'connection': 'mock_db_connection'}#Here you created a mock database connection using a dictionary.
    try:
        yield db
    finally:
        db.close()


# endpoint
@app.get('/home')
def home(db=Depends(get_db)):
    return {'db_status': db['connection']}



# Database connection is required and must be established before any database operation is performed•
# get_db() is a dependency function•
# Depends(get_db) tells FastAPI to call get_db() before the request and inject the result into the db parameter•

