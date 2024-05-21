from bs4 import BeautifulSoup
import datetime
from configs.configs import MEDIA_TYPE, HEADERS, PATH_TAG
from colorama import Fore, Style
import logging
from fastapi import Response

def create_response(tag_for_det_act, soup_request):
    with open(PATH_TAG[tag_for_det_act]) as file:
        xml_response = file.read()
    match tag_for_det_act:
        case 'Renew':
            status_code = 200
            current_time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
            termination_time = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
            content = xml_response.format(current_time=current_time,
                                    termination_time=termination_time)
            response = Response(media_type = MEDIA_TYPE, 
                            status_code = status_code, 
                            content = content,
                            headers = HEADERS)
            logging.info(Fore.RED + ' sevices | create_response | response: %s \n '  % (content.replace('\n', '').replace(' ', '')) + Style.RESET_ALL)
            return response