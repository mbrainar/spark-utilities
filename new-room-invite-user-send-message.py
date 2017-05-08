"""
This will take a CSV file, parse it for a name and email field,
create a new room, invite the user, and send a message

"""

from ciscosparkapi import CiscoSparkAPI
import os
import csv

def personId(email):
    person = spark.people.list(email=email)
    for p in person:
        return p.id
    return False

_my_spark_token = os.environ.get("MYSPARKTOKEN")
spark = CiscoSparkAPI(access_token=_my_spark_token)

file = "test.csv"

with open(file) as csvfile:
    # DictReader will parse csv and create python dictionary; uses first line as dictionary keys
    reader = csv.DictReader(csvfile)
    for row in reader:
        email = row['Email']
        fname = row['First Name']
        lname = row['Last Name']
        roomname = "New Room for {} {}".format(fname, lname)
        room = spark.rooms.create(roomname)
        membership = spark.memberships.create(room.id,personEmail=email)
        message = "Hello {}.".format(fname)
        spark.messages.create(roomId=room.id,markdown=message)


