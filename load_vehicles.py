import requests
import sys
import os
import json
import csv


commands = []

def commit_bulk():
    global commands
    if commands:
        commands.append("\n")
        command = "\n".join(commands)
        headers = {'Content-Type': 'application/x-ndjson'}
        result = requests.post('http://localhost:9200/_bulk', data=command, headers=headers)
        print(result.text)
        commands = []

def add_car(car):
    global commands
    command_row = {"index": {"_index": "cars"}}
    commands.append(json.dumps(command_row))
    commands.append(json.dumps(car))
    if len(commands) > 1000: #Bulk load sizes  of 500, doubled because of command row.
        commit_bulk()

if __name__ == "__main__":
    count = 0
    with open("vehicles.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for car in reader:
            add_car(car)
            #print(json.dumps(car))
            #count += 1
            #if count > 10:
                #sys.exit(1)
    commit_bulk()
