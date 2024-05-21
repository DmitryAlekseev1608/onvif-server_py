from bs4 import BeautifulSoup

def parsing_xml(xml_bytes):
    xml_string = xml_bytes.decode("utf-8")
    soup = BeautifulSoup(xml_string, 'xml')
    tag_for_det_act = soup.find('s:Body').find_next().name
    return soup, tag_for_det_act