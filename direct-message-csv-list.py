"""
This will take a CSV file, parse it for an email field, and send a message to each email
**Note:** this will not work with users that are not already registered with Spark;
use new-room-invite-user-send-message.py instead.

"""

from ciscosparkapi import CiscoSparkAPI
import os
import csv

_my_spark_token = os.environ.get("MYSPARKTOKEN")
spark = CiscoSparkAPI(access_token=_my_spark_token)

file = "test.csv"

with open(file) as csvfile:
    # DictReader will parse csv and create python dictionary; uses first line as dictionary keys
    reader = csv.DictReader(csvfile)
    for row in reader:
        message = "Hello {}. This is an automated message.".format(row['First Name'])
        spark.messages.create(toPersonEmail=row['Email'],markdown=message)
