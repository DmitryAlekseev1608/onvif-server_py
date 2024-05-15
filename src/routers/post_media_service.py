from fastapi import Request, Response, APIRouter
import logging
from colorama import Fore, Style
from lxml import etree
import datetime

from utils import parsing_xml, create_content_xml

router = APIRouter()

@router.post("/onvif/media_service", tags=["media_service"])
async def post_media_service(request: Request):
    xml_bytes = await request.body()
    content = parsing_xml(xml_bytes)

    logging.info(Fore.BLUE + ' post_media_service | post_media_service | soapaction from headers: %s \n '  % (request.headers['soapaction']) + Style.RESET_ALL)  
    logging.info(Fore.BLUE + ' post_media_service | post_media_service | content: %s \n '  % (etree.tostring(content)) + Style.RESET_ALL)

    match request.headers['soapaction']:
        case '"http://www.onvif.org/ver10/media/wsdl/GetProfiles"':
            status_code = 200
            media_type = 'application/soap+xml; charset=utf-8'
            content = create_content_xml('src/soap/get_profiles.xml')
            headers = {'Server': 'gSOAP/2.8E',
                       'Connection': 'close',
                       'X-Frame-Options': 'DENY',
                       'X-XSS-Protection': '1; mode=block',
                       'X-Content-Type-Options': 'nosniff',
                       'Strict-Transport-Security': 'max-age=63072000; includeSubdomains;',
                       'Date': datetime.datetime.utcnow().isoformat("T") + "Z"}
            response = Response(media_type = media_type, 
                            status_code = status_code,
                            content = content,
                            headers = headers)
            logging.info(Fore.BLUE + ' post_media_service | post_media_service | response headers: %s \n '  % (response.headers) + Style.RESET_ALL)
            return response
        
        case '"http://www.onvif.org/ver10/media/wsdl/GetStreamUri"':
            status_code = 200
            media_type = 'application/soap+xml; charset=utf-8'
            content = create_content_xml('src/soap/get_stream_uri.xml')
            headers = {'Server': 'gSOAP/2.8E',
                       'Connection': 'close',
                       'X-Frame-Options': 'DENY',
                       'X-XSS-Protection': '1; mode=block',
                       'X-Content-Type-Options': 'nosniff',
                       'Strict-Transport-Security': 'max-age=63072000; includeSubdomains;',
                       'Date': datetime.datetime.utcnow().isoformat("T") + "Z"}
            response = Response(media_type = media_type, 
                            status_code = status_code,
                            content = content,
                            headers = headers)
            logging.info(Fore.BLUE + ' post_media_service | post_media_service | response headers: %s \n '  % (response.headers) + Style.RESET_ALL)
            return response

        case '"http://www.onvif.org/ver10/media/wsdl/GetSnapshotUri"':
            status_code = 200
            media_type = 'application/soap+xml; charset=utf-8'
            content = create_content_xml('src/soap/get_snapshot_uri.xml')
            headers = {'Server': 'gSOAP/2.8E',
                       'Connection': 'close',
                       'X-Frame-Options': 'DENY',
                       'X-XSS-Protection': '1; mode=block',
                       'X-Content-Type-Options': 'nosniff',
                       'Strict-Transport-Security': 'max-age=63072000; includeSubdomains;',
                       'Date': datetime.datetime.utcnow().isoformat("T") + "Z"}
            response = Response(media_type = media_type, 
                            status_code = status_code,
                            content = content,
                            headers = headers)
            logging.info(Fore.BLUE + ' post_media_service | post_media_service | response headers: %s \n '  % (response.headers) + Style.RESET_ALL)
            return response