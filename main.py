from pymongo import MongoClient
from PaperContext import paperead, settings
import sys
import os
from joblib import Parallel, delayed
import multiprocessing


def save_to_mongo(paper_id):
    client = MongoClient()
    db = client.paper_db
    colletion = db.paper
    doc = paperead.get_xml_paper(paper_id)
    paper = doc['document']
    paper['paper_id'] = doc['document']['@id']
    paper['text'] = paperead.get_text_paper(paper_id)
    colletion.insert_one(paper)


def job(paper_colletion_number):
    for i in paperead.list_paper_id_in_paper_colletion(paper_colletion_number):
        try:
            save_to_mongo(i)
        except Exception as e:
            open('error-log.txt', 'a').write(str(i) + ' ' + e.message + '\n')


def main(start, end):
    num_cores = multiprocessing.cpu_count()
    Parallel(n_jobs=num_cores)(delayed(job)(i) for i in range(start, end))


if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
