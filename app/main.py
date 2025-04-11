"""
Description:
    This module is responsible for defining the FastAPI application.
"""
# app/main.py   
from fastapi import FastAPI, Request # HTTPException
from fastapi.responses import JSONResponse
from app.host import health, host
import os

app = FastAPI()

WHITELISTED_IPS = os.getenv("WHITELISTED_IPS", "").split(",")

#
# extended later to log full tracebacks, report to Sentry, etc.
# if os.getenv("ENV") == "development":
#
if os.getenv("ENV") == "production":
    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"message": "An internal error occurred. Please try again later."},
        )
#
#

# Middleware to enforce IP whitelisting
@app.middleware("http")
async def enforce_ip_whitelist(request: Request, call_next):
    x_forwarded_for = request.headers.get("x-forwarded-for", request.client.host)
    client_ip = x_forwarded_for.split(",")[0].strip()
    print("REAL CLIENT IP:", client_ip)

    if WHITELISTED_IPS and client_ip not in WHITELISTED_IPS:
        return JSONResponse(status_code=403, content={"detail": "Forbidden"})

    return await call_next(request)

app.include_router(health.router, prefix="/health")
app.include_router(host.router, prefix="/host")

# host.py handles live status, announcements, errors
# region.py handles clusters, groups, availability zones
# dns.py handles vanity hostname registration
# alerts.py for email/pager duty/reporting
# ingest.py for raw metrics streams

@app.get("/")

def root():
    return {"status": "FastNOC v1.0 is live"}
