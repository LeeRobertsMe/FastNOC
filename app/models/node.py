"""
Description:
    This module is responsible for defining the FastAPI application.
"""
# Import necessary modules
from pydantic import BaseModel

class HostReport(BaseModel):
    hostname: str
    ip_address: str
    status: str
