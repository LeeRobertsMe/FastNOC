# FastNOC v1.0

Private on-premise infrastructure management control panel, powered by FastAPI.

The dashboard acts as the “front door” to a larger system. Public routes serve only the frontend (web/), while the backend (app/) remains private — exposed solely via NGINX reverse proxy at /api/\*, enabling secure ingress for remote traffic.

Designed for extensibility, observability, and secure multi-region orchestration — an infrastructure-first platform for self-hosted control, visibility, and automation.
