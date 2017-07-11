"""
This will take a CSV file, parse it for an email field, and add each email to an existing room
This functionality exists in https://sparkpowerpack.com as well, with a GUI wrapper

"""

from ciscosparkapi import CiscoSparkAPI
import os
import csv

_my_spark_token = os.environ.get("MYSPARKTOKEN")
spark = CiscoSparkAPI(access_token=_my_spark_token)

room_name = "DevNet Express DNA Dublin"
rooms = spark.rooms.list()
for r in rooms:
    if r.title == room_name:
        room_id = r.id
        break

file = "report-2017-05-12T2306.csv"

with open(file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        spark.memberships.create(room_id, personEmail=row['Email'])
