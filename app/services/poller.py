"""
Description:
    This module is responsible for defining the FastAPI application.
"""
# app/services/poller.py
import httpx
from app.core.config import HOST_URLS

async def check_cluster_health():
    responding_hosts = []
    for url in HOST_URLS:
        try:
            # r = await httpx.get(f"{url}/health", timeout=3.0)
            async with httpx.AsyncClient(timeout=3.0) as client:
                r = await client.get(f"{url}/health")

            if r.status_code == 200:
                responding_hosts.append(url)
        except (httpx.RequestError, httpx.TimeoutException):
            pass

    return {
        "healthy": len(responding_hosts) > 0,
        "responding_hosts": responding_hosts
    }

