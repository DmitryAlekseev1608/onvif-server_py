import datetime
from configs.configs import MEDIA_TYPE, HEADERS, PATH_TAG, VIDEO_SOURCE, COMMON
from colorama import Fore, Style
import logging
from fastapi import Response

def create_response(tag_for_det_act, soup_request):
    with open(PATH_TAG[tag_for_det_act]) as file:
        xml_response = file.read()
    match tag_for_det_act:
        case 'GetSystemDateAndTime':
            current_time = datetime.datetime.now()
            content = xml_response.format(past_hour=current_time.hour,
                                    past_minute=current_time.minute,
                                    past_second= current_time.second,
                                    past_year=current_time.year,
                                    past_month=current_time.month,
                                    past_day=current_time.day)
            status_code = 200
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' device_service | create_response | response: %s \n '  % (content.replace('\n', '').replace(' ', '')) + Style.RESET_ALL)
            return response
        
        case 'GetCapabilities':
            status_code = 200
            content = xml_response.format(ip_server=COMMON.ip_server)
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' device_service | create_response | response: %s \n '  % (content.replace('\n', '').replace(' ', '')) + Style.RESET_ALL)
            return response
        
        case 'GetDeviceInformation':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' device_service | create_response | response: %s \n '  % (content.replace('\n', '').replace(' ', '')) + Style.RESET_ALL)
            return response
        
        case 'GetScopes':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' device_service | create_response | response: %s \n '  % (content.replace('\n', '').replace(' ', '')) + Style.RESET_ALL)
            return response
        
        case 'GetServices':
            status_code = 200
            content = xml_response.format(ip_server=COMMON.ip_server)
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' device_service | create_response | response: %s \n '  % (content.replace('\n', '').replace(' ', '')) + Style.RESET_ALL)
            return response
        
        case 'GetNetworkInterfaces':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' device_service | create_response | response: %s \n '  % (content.replace('\n', '').replace(' ', '')) + Style.RESET_ALL)
            return response
        
        case 'GetDNS':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' device_service | create_response | response: %s \n '  % (content.replace('\n', '').replace(' ', '')) + Style.RESET_ALL)
            return response