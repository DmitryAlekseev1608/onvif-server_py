from configs.configs import MEDIA_TYPE, HEADERS, PATH_TAG, VIDEO_SOURCE, COMMON
from colorama import Fore, Style
import logging
from fastapi import Response

def create_response(tag_for_det_act, soup_request):
    with open(PATH_TAG[tag_for_det_act]) as file:
        xml_response = file.read()

    match tag_for_det_act:
        case 'GetProfiles':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' media_service | create_response | response: %s \n '  % (content.replace('\n', '').replace(' ', '')) + Style.RESET_ALL)
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
            logging.info(Fore.RED + ' media_service | create_response | response: %s \n '  % (content.replace('\n', '').replace(' ', '')) + Style.RESET_ALL)
            return response
        
        case 'GetSnapshotUri':
            status_code = 200
            content = xml_response.format(ip_server=COMMON.ip_server)
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' media_service | create_response | response: %s \n '  % (content.replace('\n', '').replace(' ', '')) + Style.RESET_ALL)
            return response

        case 'GetVideoSources':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' media_service | create_response | response: %s \n '  % (content.replace('\n', '').replace(' ', '')) + Style.RESET_ALL)
            return response
        
        case 'GetVideoSourceConfigurations':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' media_service | create_response | response: %s \n '  % (content.replace('\n', '').replace(' ', '')) + Style.RESET_ALL)
            return response
        
        case 'GetAudioSourceConfigurations':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' media_service | create_response | response: %s \n '  % (content.replace('\n', '').replace(' ', '')) + Style.RESET_ALL)
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
            logging.info(Fore.RED + ' media_service | create_response | response: %s \n '  % (content.replace('\n', '').replace(' ', '')) + Style.RESET_ALL)
            return response

        case 'GetVideoSourceConfiguration':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' media_service | create_response | response: %s \n '  % (content.replace('\n', '').replace(' ', '')) + Style.RESET_ALL)
            return response
        
        case 'GetMetadataConfigurationOptions':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' media_service | create_response | response: %s \n '  % (content.replace('\n', '').replace(' ', '')) + Style.RESET_ALL)
            return response
        
        case 'GetMetadataConfiguration':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' media_service | create_response | response: %s \n '  % (content.replace('\n', '').replace(' ', '')) + Style.RESET_ALL)
            return response
        
        case 'GetAudioSources':
            status_code = 200
            content = xml_response
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' media_service | create_response | response: %s \n '  % (content.replace('\n', '').replace(' ', '')) + Style.RESET_ALL)
            return response