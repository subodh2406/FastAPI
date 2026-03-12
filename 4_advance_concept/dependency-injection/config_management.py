# Configuration Management in FastAPI
#
# This example demonstrates how to manage configuration values
# (like API keys, debug flags, database URLs) in a centralized way.
#
# A Settings class is used to store configuration values.
# This improves maintainability because all configuration values
# are defined in one place.
#
# The get_settings() function acts as a dependency that creates
# and returns a Settings object.
#
# FastAPI's Depends() is used to inject this Settings object
# into the route handler automatically.
#
# Flow:
# 1. Client calls the /config endpoint
# 2. FastAPI sees Depends(get_settings)
# 3. FastAPI calls get_settings()
# 4. The returned Settings object is passed to the function
# 5. The endpoint accesses settings.api_key and returns it
#
# This approach is useful for managing:
# - API keys
# - Database URLs
# - Environment settings
# - Debug flags



    
from fastapi import FastAPI, Depends

app = FastAPI()


class Settings:
    def __init__(self):
        self.api_key = 'my_secret'
        self.debug = True


def get_settings():
    return Settings()


@app.get('/config')
def get_conifig(settings: Settings = Depends(get_settings)):
    return {'api_key': settings.api_key}