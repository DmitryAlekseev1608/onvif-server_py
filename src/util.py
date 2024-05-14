from lxml import etree

def parsing_xml(xml_bytes):
    xml_string = xml_bytes.decode("utf-8")
    root = etree.fromstring(xml_string)
    return root

def create_content_xml(path):
    with open(path) as file:
        xml_response = file.read()
    return xml_response