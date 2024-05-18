from fastapi import Request, Response, APIRouter
import logging
from colorama import Fore, Style
import datetime
import time

from utils import parsing_xml, create_content_xml

router = APIRouter()

@router.post("/onvif/media_service", tags=["media_service"])
async def post_media_service(request: Request):
    xml_bytes = await request.body()
    soup, tag_for_det_act = parsing_xml(xml_bytes)

    logging.info(Fore.BLUE + ' post_media_service | post_media_service | tag_for_det_act: %s \n '  % (tag_for_det_act) + Style.RESET_ALL)
    logging.info(Fore.BLUE + ' post_media_service | post_media_service | headers: %s \n '  % (request.headers) + Style.RESET_ALL)  
    logging.info(Fore.BLUE + ' post_media_service | post_media_service | content: %s \n '  % (soup) + Style.RESET_ALL)

    match tag_for_det_act:
        case 'GetProfiles':
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
            logging.info(Fore.RED + ' post_media_service | post_media_service | response: %s \n '  % (content) + Style.RESET_ALL)
            return response
        
        case 'GetStreamUri':
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
            logging.info(Fore.RED + ' post_media_service | post_media_service | response: %s \n '  % (content) + Style.RESET_ALL)
            return response

        case 'GetSnapshotUri':
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
            logging.info(Fore.RED + ' post_media_service | post_media_service | response: %s \n '  % (content) + Style.RESET_ALL)
            return response
        
        case 'GetVideoSources':
            status_code = 200
            media_type = 'application/soap+xml; charset=utf-8'
            content = create_content_xml('src/soap/get_video_sources.xml')
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
            logging.info(Fore.RED + ' post_media_service | post_media_service | response: %s \n '  % (content) + Style.RESET_ALL)
            return response
        
        case 'GetVideoSourceConfigurations':
            status_code = 200
            media_type = 'application/soap+xml; charset=utf-8'
            content = create_content_xml('src/soap/get_video_source_configuration.xml')
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
            logging.info(Fore.RED + ' post_media_service | post_media_service | response: %s \n '  % (content) + Style.RESET_ALL)
            return response
        
        case 'GetAudioSourceConfigurations':
            status_code = 200
            media_type = 'application/soap+xml; charset=utf-8'
            content = create_content_xml('src/soap/get_audio_source_configuration.xml')
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
            logging.info(Fore.RED + ' post_media_service | post_media_service | response: %s \n '  % (content) + Style.RESET_ALL)
            return response
        
        case 'GetProfile':
            status_code = 200
            media_type = 'application/soap+xml; charset=utf-8'
            content = create_content_xml('src/soap/get_profile.xml')
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
            logging.info(Fore.RED + ' post_media_service | post_media_service | response: %s \n '  % (content) + Style.RESET_ALL)
            return response
        
        case 'GetVideoSourceConfiguration':
            status_code = 200
            media_type = 'application/soap+xml; charset=utf-8'
            content = create_content_xml('src/soap/get_video_source_configuration.xml')
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
            logging.info(Fore.RED + ' post_media_service | post_media_service | response: %s \n '  % (content) + Style.RESET_ALL)
            return response