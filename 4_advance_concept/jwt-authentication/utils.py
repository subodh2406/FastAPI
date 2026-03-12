# utils.py (short for utilities) is used to store helper functions that are reused in many parts of the application.
# Instead of repeating the same logic in multiple files, you place it in utils.py and import it wherever needed.

# 1️⃣ Main Purpose of utils.py
# utils.py contains common helper functions that support the main logic of your application.
# Typical things placed in utils.py:
# Password hashing
# Password verification
# Token generation
# Date formatting
# Data conversion
# Helper calculations


from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# CryptContext is a password hashing manager.
# It is used to:
# 1. Hash passwords
# 2. Verify passwords
# 3. Manage multiple hashing algorithms
#
# schemes=['bcrypt']
# → Tells Passlib to use the bcrypt algorithm to hash passwords.
#
# deprecated='auto'
# → Automatically marks older hashing algorithms (e.g., sha256) as deprecated.
# → Ensures new passwords are hashed using bcrypt.


#fake_user_db is a temporary dictionary that stores a user and their hashed password for testing authentication.
fake_user_db = {
    'johndoe': {
        'username': 'johndoe',
        'hashed_password': pwd_context.hash('secret123')
    }
}

#This function retrieves a user from the fake database.
def get_user(username: str):
    user = fake_user_db.get(username)
    return user

#This function checks if the entered password matches the stored hashed password.
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)