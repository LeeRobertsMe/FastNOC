"""
Description:
    This module is responsible for defining the FastAPI application.
"""
# Import necessary modules
from fastapi import APIRouter, Response
from app.services.poller import check_cluster_health

router = APIRouter()

@router.get("/")
async def cluster_health():
    return await check_cluster_health()

@router.get("/metrics")
async def prometheus_metrics():
    # Placeholder for real Prometheus integration
    return Response(content="# HELP dummy_metric Just a stub\n# TYPE dummy_metric counter\ndummy_metric 1\n",media_type="text/plain")
