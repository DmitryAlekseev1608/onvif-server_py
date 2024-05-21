from fastapi import Request, APIRouter
import logging
from colorama import Fore, Style
from fastapi.responses import FileResponse

import device_service
import media_service
import event_service
import web_service
import services
from request import parsing_xml

router = APIRouter()

@router.post("/onvif/device_service", tags=["device_service"])
async def post_device_service(request: Request):
    xml_bytes = await request.body()
    soup_request, tag_for_det_act = parsing_xml(xml_bytes)

    logging.info(Fore.BLUE + ' routers | post_device_service | tag_for_det_act: %s \n '  % (tag_for_det_act) + Style.RESET_ALL)
    logging.info(Fore.BLUE + ' routers | post_device_service | headers: %s \n '  % (request.headers) + Style.RESET_ALL)  
    logging.info(Fore.BLUE + ' routers | post_device_service | content: %s \n '  % (soup_request) + Style.RESET_ALL)

    response = device_service.create_response(tag_for_det_act, soup_request)
    return response

@router.post("/onvif/media_service", tags=["media_service"])
async def post_media_service(request: Request):
    xml_bytes = await request.body()
    soup_request, tag_for_det_act = parsing_xml(xml_bytes)

    logging.info(Fore.BLUE + ' routers | post_media_service | tag_for_det_act: %s \n '  % (tag_for_det_act) + Style.RESET_ALL)
    logging.info(Fore.BLUE + ' routers | post_media_service | headers: %s \n '  % (request.headers) + Style.RESET_ALL)  
    logging.info(Fore.BLUE + ' routers | post_media_service | content: %s \n '  % (soup_request) + Style.RESET_ALL)

    response = media_service.create_response(tag_for_det_act, soup_request)
    return response

@router.post("/onvif/event_service", tags=["eventservice"])
async def post_event_service(request: Request):
    xml_bytes = await request.body()
    soup_request, tag_for_det_act = parsing_xml(xml_bytes)

    logging.info(Fore.BLUE + ' routers | post_event_service | tag_for_det_act: %s \n '  % (tag_for_det_act) + Style.RESET_ALL)
    logging.info(Fore.BLUE + ' routers | post_event_service | headers: %s \n '  % (request.headers) + Style.RESET_ALL)  
    logging.info(Fore.BLUE + ' routers | post_event_service | content: %s \n '  % (soup_request) + Style.RESET_ALL)

    response = event_service.create_response(tag_for_det_act, soup_request)
    return response

@router.post("/WebService", tags=["WebService"])
async def post_web_service(request: Request, Idx: int):
    xml_bytes = await request.body()
    soup_request, tag_for_det_act = parsing_xml(xml_bytes)

    logging.info(Fore.BLUE + ' routers | post_web_service | tag_for_det_act: %s \n '  % (tag_for_det_act) + Style.RESET_ALL)
    logging.info(Fore.BLUE + ' routers | post_web_service | headers: %s \n '  % (request.headers) + Style.RESET_ALL)  
    logging.info(Fore.BLUE + ' routers | post_web_service | content: %s \n '  % (soup_request) + Style.RESET_ALL)
    logging.info(Fore.BLUE + ' routers | post_web_service | Idx: %s \n '  % (Idx) + Style.RESET_ALL)

    response =  web_service.create_response(tag_for_det_act, soup_request)
    return response

@router.post("/onvif/services", tags=["services"])
async def post_services(request: Request):
    xml_bytes = await request.body()
    soup_request, tag_for_det_act = parsing_xml(xml_bytes)

    logging.info(Fore.BLUE + ' routers | post_services | tag_for_det_act: %s \n '  % (tag_for_det_act) + Style.RESET_ALL)
    logging.info(Fore.BLUE + ' routers | post_services | headers: %s \n '  % (request.headers) + Style.RESET_ALL)  
    logging.info(Fore.BLUE + ' routers | post_services | content: %s \n '  % (soup_request) + Style.RESET_ALL)

    response =  services.create_response(tag_for_det_act, soup_request)
    return response

@router.get("/", tags=["snapshot"])
async def get_snapshot():
    logging.info(Fore.BLUE + ' routers | get_snapshot | request snapshot \n ' + Style.RESET_ALL)
    return FileResponse('img/img.jpg')

@router.get("/snapshot", tags=["snapshot_snapshot"])
async def get_snapshot_snapshot():
    logging.info(Fore.BLUE + ' routers | get_snapshot_snapshot | request snapshot_snapshot \n ' + Style.RESET_ALL)
    return FileResponse('img/img.jpg')