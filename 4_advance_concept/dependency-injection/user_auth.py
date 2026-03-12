# Authentication and Authorization in FastAPI

# Authentication:
# Authentication is the process of verifying the identity of a user.
# It checks if the user is who they claim to be.
# Example: Logging in with username and password.

# Authorization:
# Authorization determines what actions an authenticated user is allowed to perform.
# Example: Only an admin user can delete data.

# In FastAPI, authentication and authorization are usually implemented using:
# 1. Dependencies (Depends())
# 2. Middleware
# These mechanisms help control access to API endpoints.


# JSON Web Token (JWT)

# JWT is a compact and URL-safe token used for securely transmitting information
# between two parties (usually client and server).

# In FastAPI authentication:
# 1. User logs in with username and password.
# 2. Server verifies credentials.
# 3. Server generates a JWT token.
# 4. Client stores the token.
# 5. Client sends the token in the Authorization header for future requests.

# Example header:
# Authorization: Bearer <JWT_token>

# The server then verifies the token and allows access to protected routes.


# OAuth2

# OAuth2 is an authorization framework that allows applications to access
# user resources on another service in a controlled way.

# In FastAPI, OAuth2 is commonly implemented using OAuth2PasswordBearer.

# OAuth2 Password Flow works like this:
# 1. User sends username and password to the /token endpoint.
# 2. Server verifies the credentials.
# 3. Server returns an access token.
# 4. Client uses the token in future API requests.

# FastAPI extracts the token using OAuth2PasswordBearer and validates it
# before allowing access to protected routes.

from fastapi import FastAPI, Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token') #it is a dependency provided by fastapi that extracts an token from authorization header 
#OAuth2PasswordBearer is a FastAPI security class used to implement OAuth2 authentication using Bearer tokens.
# I'ts job is to:
# Look for the Authorization header
# Extract the token
# Provide that token to your route or dependency

@app.post('/token')
def login(username: str = Form(...), password: str = Form(...)):
    if username == 'john' and password == 'pass123':
        return {'access_token': 'valid_token', 'token_type': 'bearer'}
    raise HTTPException(status_code=400, detail='Invalid Credentials')


def decode_token(token: str):
    if token == 'valid_token':
        return {'name': 'john'}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid Authentication Credentials'
    )


def get_current_user(token: str = Depends(oauth2_scheme)):
    return decode_token(token)


@app.get('/profile')
def get_profile(user=Depends(get_current_user)):
    return {'username': user['name']}