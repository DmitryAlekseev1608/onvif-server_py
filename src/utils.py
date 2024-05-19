from bs4 import BeautifulSoup
import datetime
from configs.configs import MEDIA_TYPE, HEADERS, PATH_TAG, VIDEO_SOURCE
from colorama import Fore, Style
import logging
from fastapi import Response

def parsing_xml(xml_bytes):
    xml_string = xml_bytes.decode("utf-8")
    soup = BeautifulSoup(xml_string, 'xml')
    tag_for_det_act = soup.find('s:Body').find_next().name
    return soup, tag_for_det_act

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
            logging.info(Fore.RED + ' utils | create_response | response: %s \n '  % (content) + Style.RESET_ALL)
            return response
        
        case 'GetCapabilities':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' utils | create_response | response: %s \n '  % (content) + Style.RESET_ALL)
            return response
        
        case 'GetDeviceInformation':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' utils | create_response | response: %s \n '  % (content) + Style.RESET_ALL)
            return response
        
        case 'GetScopes':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' utils | create_response | response: %s \n '  % (content) + Style.RESET_ALL)
            return response
        
        case 'GetServices':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' utils | create_response | response: %s \n '  % (content) + Style.RESET_ALL)
            return response
        
        case 'GetNetworkInterfaces':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' utils | create_response | response: %s \n '  % (content) + Style.RESET_ALL)
            return response
        
        case 'GetDNS':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' utils | create_response | response: %s \n '  % (content) + Style.RESET_ALL)
            return response
        
        case 'GetProfiles':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' utils | create_response | response: %s \n '  % (content) + Style.RESET_ALL)
            return response
        
        case 'GetStreamUri':
            profile = soup_request.find('ProfileToken').string
            for video_source in list(VIDEO_SOURCE.keys()):
                if profile in VIDEO_SOURCE[video_source].profiles:
                    break
            status_code = 200
            content = xml_response.format(uri=VIDEO_SOURCE[video_source].uri)
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' utils | create_response | response: %s \n '  % (content) + Style.RESET_ALL)
            return response
        
        case 'GetSnapshotUri':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' utils | create_response | response: %s \n '  % (content) + Style.RESET_ALL)
            return response

        case 'GetVideoSources':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' utils | create_response | response: %s \n '  % (content) + Style.RESET_ALL)
            return response
        
        case 'GetVideoSourceConfigurations':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' utils | create_response | response: %s \n '  % (content) + Style.RESET_ALL)
            return response
        
        case 'GetAudioSourceConfigurations':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' utils | create_response | response: %s \n '  % (content) + Style.RESET_ALL)
            return response
        
        case 'GetProfile':
            profile = soup_request.find('ProfileToken').string
            for video_source in list(VIDEO_SOURCE.keys()):
                if profile in VIDEO_SOURCE[video_source].profiles:
                    break
            status_code = 200
            content = xml_response.format(profile=profile,
                        video_source=video_source)
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' utils | create_response | response: %s \n '  % (content) + Style.RESET_ALL)
            return response

        case 'GetVideoSourceConfiguration':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' utils | create_response | response: %s \n '  % (content) + Style.RESET_ALL)
            return response