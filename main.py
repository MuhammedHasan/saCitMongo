from pymongo import MongoClient
from PaperContext import paperead, settings
import sys
import os


def save_to_mongo(paper_id):
    client = MongoClient()
    db = client.paper_db
    colletion = db.paper
    doc = paperead.get_xml_paper(paper_id)
    paper = doc['document']
    paper['paper_id'] = doc['document']['@id']
    paper['text'] = paperead.get_text_paper(paper_id)
    colletion.insert_one(paper)


def main(paper_colletion_number):
    for j in range(3, 648):
        for i in paperead.list_paper_id_in_paper_colletion(j):
            try:
                save_to_mongo(i)
            except Exception as e:
                open('error-log.txt', 'a').write(str(i) + ' ' + e.message + '\n')


if __name__ == '__main__':
    main()
