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


def main(paper_colletion_numbers, number_paper_in_colletion):
    for i in paper_colletion_numbers:
        for j in range(number_paper_in_colletion):
            save_to_mongo('10.1.1.%d.%d' % (i, j))


if __name__ == '__main__':
    args = str(sys.argv)
    main(args[1], args[2])
