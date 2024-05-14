from fastapi import FastAPI, Body, Request, Response
from lxml import etree
import uvicorn
import logging
from colorama import Fore, Style

logging.basicConfig(format="%(asctime)s|%(levelname)s|%(message)s", level="INFO")
logger = logging.getLogger(__name__)
app = FastAPI()

def parsing_xml(xml_bytes):
    xml_string = xml_bytes.decode("utf-8")
    root = etree.fromstring(xml_string)
    return root

def create_content_xml(path):
    with open(path) as file:
        xml_response = file.read()
    return xml_response

@app.post("/onvif/device_service")
async def post_device_service(request: Request):
    xml_bytes = await request.body()
    content = parsing_xml(xml_bytes)

    logging.info(Fore.BLUE + ' main | post_device_service | soapaction from headers: %s \n '  % (request.headers['soapaction']) + Style.RESET_ALL)  
    logging.info(Fore.BLUE + ' main | post_device_service | content: %s \n '  % (etree.tostring(content)) + Style.RESET_ALL)

    match request.headers['soapaction']:
        case '"http://www.onvif.org/ver10/device/wsdl/GetSystemDateAndTime"':
            status_code = 200
            media_type = 'application/soap+xml; charset=utf-8'
            content = create_content_xml('soap/get_system_date_and_time.xml')
            return Response(media_type = media_type, 
                            status_code = status_code, 
                            content = content)
        
        case '"http://www.onvif.org/ver10/device/wsdl/GetCapabilities"':
            status_code = 200
            media_type = 'application/soap+xml; charset=utf-8'
            content = create_content_xml('soap/get_capabilities.xml')
            return Response(media_type = media_type,
                            status_code = status_code, 
                            content = content)

@app.post('/onvif/media_service')
async def post_media_service(request: Request):
    print("------------------------------------------")

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8080,
        reload=True
    )