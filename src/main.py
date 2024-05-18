from fastapi import FastAPI
import uvicorn
import logging
import routers

logging.basicConfig(format="%(asctime)s|%(levelname)s|%(message)s", level="INFO")
logger = logging.getLogger(__name__)
app = FastAPI()
app.include_router(routers.router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8080,
        reload=True,
        server_header=False
    )