from bs4 import BeautifulSoup
import datetime
from configs.configs import MEDIA_TYPE, HEADERS, PATH_TAG
from colorama import Fore, Style
import logging
from fastapi import Response

def create_response(tag_for_det_act, soup_request):
    with open(PATH_TAG[tag_for_det_act]) as file:
        xml_response = file.read()