import csv
from collections import deque
import elasticsearch
from elasticsearch import helpers
import re

def readMovies():
    csvfile = open('movies.csv', 'r', encoding='utf8', errors='ignore')

    reader = csv.DictReader( csvfile )
    for line in reader:
        movie = {}
        movie['id'] = int(line['movieId'])
        movie['title'] = re.sub(" \(.*\)$", "", re.sub('"','', line['title']))
        movie['year'] = line['title'][-5:-1]
        genres = line['genres'].split('|')
        movie['genre'] = genres

        yield movie


es = elasticsearch.Elasticsearch()

es.indices.delete(index="movies",ignore=404)
deque(helpers.parallel_bulk(es,readMovies(),index="movies",doc_type="movie"), maxlen=0)
es.indices.refresh()
