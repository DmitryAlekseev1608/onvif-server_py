from fastapi import APIRouter
from fastapi.responses import FileResponse

from utils import parsing_xml

router = APIRouter()

@router.get("/snapshot", tags=["snapshot"])
async def get_snapshot():
    return FileResponse('img/img.jpg')