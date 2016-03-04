from pymongo import MongoClient
from PaperContext import paperead, settings
import sys
import os


def save_to_mongo(paper_id):
    client = MongoClient()
    db = client.paper_db
    colletion = db.paper
    paper = paperead.get_xml_paper(paper_id)['document']
    paper['text'] = paperead.get_text_paper(paper_id)
    colletion.insert_one(paper)


def main(paper_colletion_number):
    for i in paperead.list_paper_id_in_paper_colletion(paper_colletion_number):
        save_to_mongo(i)


if __name__ == '__main__':
    main(int(sys.argv[1]))
