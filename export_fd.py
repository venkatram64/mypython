from datetime import timedelta, date, datetime

import random

import string
import requests

start_date = datetime(2017, 11, 22)

for x in range(60 * 48):
    print(x, ", ",)
    single_date = start_date + timedelta(minutes=x)
    dt = single_date.strftime("%Y-%m-%d")
    url = "http://localhost:9200/{}-fake/fake".format(dt)
    doc = {"user": "venn.com",
           "post_date": single_date.isoformat(),
           "message": ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12)),
           "x": x,
           "cpu": random.randint(0, 100),
           "io": random.randint(0, 100)

           }
    resp = requests.post(url, json=doc)
    print( resp.text)