from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'https://my-frontend.com', 'http://localhost:3000' ## List of allowed frontend domains/origins
    ],
    allow_credentials=True, ## Allow sending cookies or authentication credentials
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_headers=['*']## Allow all HTTP headers (Authorization, Content-Type, etc.)
)

# Explanation:
# 1. allow_origins: Specifies which origins are allowed to make requests to the API.
# 2. allow_credentials: If True, the browser can send cookies or other credentials in cross-origin requests.
# 3. allow_methods: Restricts which HTTP methods are allowed from the specified origins.
# 4. allow_headers: Determines which HTTP headers can be included in the requests; '*' means all headers are allowed.
# 
# Overall, this setup ensures that only requests from specified frontend domains can access the API,
# while supporting authentication credentials and all necessary headers.



# CORS Middleware
# Purpose:
# Allows controlled cross-origin requests so frontend applications from different domains or ports can communicate with the API.

# Why use it:
# Enables frontend applications (e.g., React, Angular) hosted on different domains to access your backend safely.
# Supports sending authentication credentials (cookies or headers) across origins.
# Prevents browser CORS errors when making API requests from external domains.

# define endpoints