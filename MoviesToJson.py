import csv
import re

#http://media.sundog-soft.com/es/MoviesToJson.py
#python MoviesToJson.py > movies.json


#http://localhost:9200/_bulk
#postman


csvfile = open('movies.csv', 'r', encoding='utf8', errors='ignore')

reader = csv.DictReader( csvfile )
for movie in reader:
        print ("{ \"create\" : { \"_index\": \"movies\", \"_type\": \"movie\", \"_id\" : \"" , movie['movieId'], "\" } }", sep='')
        title = re.sub(" \(.*\)$", "", re.sub('"','', movie['title']))
        year = movie['title'][-5:-1]
        if (not year.isdigit()):
            year = "2016"
        genres = movie['genres'].split('|')
        print ("{ \"id\": \"", movie['movieId'], "\", \"title\": \"", title, "\", \"year\":", year, ", \"genre\":[", end='', sep='')
        for genre in genres[:-1]:
            print("\"", genre, "\",", end='', sep='')
        print("\"", genres[-1], "\"", end = '', sep='')
        print ("] }")