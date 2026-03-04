# # Import the FastAPI class from the fastapi package
# from fastapi import FastAPI

# # Create an instance of the FastAPI application
# app = FastAPI()

# # Define a route for the root URL ("/")
# # This will respond to HTTP GET requests
# # @app.get('/') is a DECORATOR
# # A decorator connects this function to the given URL path
# @app.get('/')
# def home():
#     # This function will be called whenever someone visits "/"
    
#     # Return a JSON response (FastAPI automatically converts dict to JSON)
#     return {'message': 'Hello FastAPI!'}



# fat api returns response iin three way one is dictionary the above coed
# secodn is pydantic and third is custom object
# ?this is pydantic 
from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


app = FastAPI()


@app.get('/user', response_model=User)
def get_user():
    return User(id=1, name='Bruce')

# What response_model=User does:
# It tells FastAPI:
# "The response of this endpoint must match the User model."
# So FastAPI will:

# ✅ Validate the response
# ✅ Filter extra fields
# ✅ Generate correct API documentation
# ✅ Convert it to JSON