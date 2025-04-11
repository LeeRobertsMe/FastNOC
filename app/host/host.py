"""
Description:
    This module is responsible for defining the FastAPI application.
"""
# Import necessary modules
from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/announce")
async def announce(request: Request):
    payload = await request.json()
    return {"announcement": payload}

@router.post("/metrics")
async def metrics(request: Request):
    payload = await request.json()
    return {"metric": payload}

@router.post("/alerts")
async def receive_alerts(request: Request):
    payload = await request.json()
    return {"alert": payload}