# Purpose of this file
# This module handles JWT (JSON Web Token) security.
# It is responsible for:
# 1️⃣ Creating tokens after user login
# 2️⃣ Verifying tokens when accessing protected APIs


from datetime import datetime, timedelta, timezone
from authlib.jose import JoseError, jwt 
from fastapi import HTTPException

# constants
SECRET_KEY = 'my_secret'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRY_MINUTES = 30


# This function is used to create a JWT access token after a user logs in successfully.
def create_access_token(data: dict):
    header = {'alg': ALGORITHM} #The header tells which algorithm is used to sign the token.
    expire = datetime.now(timezone.utc) + timedelta(ACCESS_TOKEN_EXPIRY_MINUTES)
    payload = data.copy() #We copy it so the original dictionary is not modified.
    payload.update({'exp': expire})
    return jwt.encode(header, payload, SECRET_KEY).decode('utf-8')
    # This generates the JWT token using:
    # header
    # payload
    # secret key
    #encode() is used to generate a JWT token.
    #decode() is used when a client sends the token back.
    

# encode()	Create a token after login
# decode()	Verify and read token when user makes request

# $#Authorization: Bearer <token>
def verify_token(token: str):
    try:
        claims = jwt.decode(token, SECRET_KEY) #this willl read the token verifies its signature using SECRET_KEY exteacts the playload
        claims.validate()#This checks: #expiration time (exp) token format If the token is expired, this step will raise an error.
        username = claims.get('sub')
        if username is None:
            raise HTTPException(status_code=401, detail='Token missing')
        return username
    except JoseError:
        raise HTTPException(status_code=401, detail="Couldn't Validate Credentials")
    # JoseError occurs when:
    #     token is invalid
    #     token signature doesn't match
    #     token is corrupted