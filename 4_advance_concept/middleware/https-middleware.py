from fastapi import FastAPI
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware

app = FastAPI()

app.add_middleware(HTTPSRedirectMiddleware)



# 1. HTTPSRedirectMiddleware
# Purpose: Automatically redirects all HTTP requests to HTTPS.

# Why use it:
# Ensures secure communication between clients and the server using TLS/SSL.
# Helps prevent sensitive data from being transmitted over insecure HTTP connections.