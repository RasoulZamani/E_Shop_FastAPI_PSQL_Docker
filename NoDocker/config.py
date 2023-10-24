# app/config.py

import os

from pydantic.v1 import BaseSettings, Field


class Settings(BaseSettings):
    secret: str = "" # automatically taken from environment variable
    token_url: str = "users/auth/token"

SETTINGS = Settings()