from pymongo import MongoClient
from PaperContext import paperead
import sys


def save_to_mongo(paper_id):
    client = MongoClient()
    db = client.paper_db
    colletion = db.paper
    paper = paperead.get_xml_paper(paper_id)['document']
    paper['text'] = paperead.get_text_paper(paper_id)
    colletion.insert_one(paper)


def main(paper_colletion_number, number_paper_in_colletion):
    for j in range(1, number_paper_in_colletion):
        save_to_mongo('10.1.1.%d.%d' % (paper_colletion_number, j))


if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
