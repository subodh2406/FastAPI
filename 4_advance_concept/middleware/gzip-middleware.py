from fastapi import FastAPI
from starlette.middleware.gzip import GZipMiddleware

app = FastAPI()

app.add_middleware(
    GZipMiddleware, minimum_size=1000 #Only compresses responses larger than 1000 bytes.
)

# GZipMiddleware
# Purpose: Automatically compresses HTTP responses using GZip.

# Why use it:
# Reduces the size of large responses (like JSON data), saving bandwidth.
# Speeds up network transfer, especially for clients with slower connections.