from fastapi import APIRouter
from fastapi.responses import FileResponse
from colorama import Fore, Style
import logging

router = APIRouter()

@router.get("/", tags=["snapshot"])
async def get_snapshot():
    logging.info(Fore.BLUE + ' get_snapshot | get_snapshot | request snapshot \n ' + Style.RESET_ALL)
    return FileResponse('img/img.jpg')

@router.get("/snapshot", tags=["snapshot"])
async def get_snapshot():
    logging.info(Fore.BLUE + ' get_snapshot | get_snapshot | request snapshot \n ' + Style.RESET_ALL)
    return FileResponse('img/img.jpg')