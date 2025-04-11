"""
Description:
    This module is responsible for defining the FastAPI application.
"""
# app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", "development")
HOST_URLS = os.getenv("HOST_URLS", "").split(",")
