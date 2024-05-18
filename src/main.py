from fastapi import FastAPI
import uvicorn
import logging
from routers import post_device_service, post_media_service, get_snapshot
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

logging.basicConfig(format="%(asctime)s|%(levelname)s|%(message)s", level="INFO")
logger = logging.getLogger(__name__)
app = FastAPI()
app.include_router(post_device_service.router)
app.include_router(post_media_service.router)
app.include_router(get_snapshot.router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8080,
        reload=True,
        server_header=False
    )