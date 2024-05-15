from lxml import etree
import datetime

def parsing_xml(xml_bytes):
    xml_string = xml_bytes.decode("utf-8")
    root = etree.fromstring(xml_string)
    return root

def create_content_xml(path):
    with open(path) as file:
        xml_response = file.read()
    return xml_response

def create_get_system_date_and_time():
    with open("src/soap/get_system_date_and_time.xml", "r") as file:
        xml_response = file.read()
    current_time = datetime.datetime.now()
    xml_response = xml_response.format(past_hour=current_time.hour,
                                       past_minute=current_time.minute,
                                       past_second= current_time.second,
                                       past_year=current_time.year,
                                       past_month=current_time.month,
                                       past_day=current_time.day)
    return xml_response


