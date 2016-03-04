import os
import xmltodict
import settings


def id_to_path(id, type_doc):
    return settings.DATASET_PATH + type_doc + '/' + id.replace('.', '/') + '/'


def get_xml_last_version(id):
    xml_dir = id_to_path(id, 'xml')
    return os.listdir(xml_dir)[-1]


def get_text_paper(id):
    paper_path = id_to_path(id, 'text') + id + '.txt'
    return open(paper_path).read()


def get_xml_paper(id):
    ''' This function will return dict '''
    paper_path = id_to_path(id, 'xml') + get_xml_last_version(id)
    paper_xml = open(paper_path).read()
    return xmltodict.parse(paper_xml)
