# models.py acts as a central place to define data models used across your project.
# It helps with:
# Data validation
# Data structure definition
# Database representation
# Code reuse
#this is basically the blue print or the architecture of tha data that are actually gonna share b.w the api 


from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str

class UserInDB(User):
    hashed_password: str