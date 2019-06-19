import csv
import re

#http://media.sundog-soft.com/es/MoviesToJson.py
#python MoviesToJson.py > movies.json

#https://www.elastic.co/downloads/past-releases/logstash-6-2-3

#http://localhost:9200/_bulk
#postman

#http://media.sundog-soft.com/es/access_log
#https://github.com/elastic/examples/blob/master/Common%20Data%20Formats/apache_logs/apache_logs

#elasticsearch-plugin install ingest-user-agent
#elasticsearch-plugin install ingest-geoip
#elasticsearch-plugin install x-pack
#xpack.security.enabled:false  => elasticsearch.yml

#kibana-plugin.bat install x-pack
#user: elastic
#password:changeme

#document
#https://www.elastic.co/products/elasticsearch
#https://www.elastic.co/learn

#https://raw.githubusercontent.com/elastic/examples/master/Machine%20Learning/Business%20Metrics%20Recipes/twitter_trends/data/tweets.csv
#https://github.com/elastic/examples/tree/master/Machine%20Learning

#logstash-6.2.3\bin>logstash.bat -f ..\..\logData\earthquake_logstash.conf

#https://help.pentaho.com/Documentation/6.1/0R0/0V0/010/000
#https://help.pentaho.com/Documentation/8.2/Developer_Center/PDI/Extend/000

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