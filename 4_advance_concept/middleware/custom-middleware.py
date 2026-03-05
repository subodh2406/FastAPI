import time
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()


class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        print(f'Request: {request.url.path} processed in {duration:.5f} seconds')
        return response


app.add_middleware(TimerMiddleware)


@app.get('/hello')
async def hello():
    for _ in range(10000000):
        pass
    return {'message': 'Hello World!'}




# BaseHTTPMiddleware
# -------------------
# BaseHTTPMiddleware is a base class provided by Starlette (the framework FastAPI is built on)
# that allows you to create custom HTTP middleware.
#
# It provides a structured way to intercept and process every HTTP request
# and response in your application.
#
# It comes from:
# from starlette.middleware.base import BaseHTTPMiddleware
#
# What it is used for:
# - Logging requests
# - Measuring execution time
# - Adding custom headers
# - Handling authentication globally
# - Modifying request or response data
# - Implementing custom security checks
#
# How it works:
# When you inherit from it:
#     class TimerMiddleware(BaseHTTPMiddleware):
#
# You must implement the dispatch() method:
#     async def dispatch(self, request: Request, call_next):
#
# Inside dispatch:
# - request → represents the incoming HTTP request
# - call_next → function that forwards the request to the next middleware or endpoint
# - You must return a response object
#
# The middleware runs before the endpoint and can also modify the response
# before it is sent back to the client.