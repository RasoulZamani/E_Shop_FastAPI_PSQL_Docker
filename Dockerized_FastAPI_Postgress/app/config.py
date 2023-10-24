# app/config.py

import os

from pydantic.v1 import BaseSettings, Field


class Settings(BaseSettings):
    db_url: str = Field(..., env='DATABASE_URL') # will declared in docker-compose.yml
    secret: str = "" # automatically taken from environment variable
    token_url: str = "users/auth/token"

SETTINGS = Settings()
