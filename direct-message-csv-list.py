"""
This will take a CSV file, parse it for an email field, and send a message to each email

"""

from ciscosparkapi import CiscoSparkAPI
import os
import csv

_my_spark_token = os.environ.get("MYSPARKTOKEN")
spark = CiscoSparkAPI(access_token=_my_spark_token)

file = "test.csv"

with open(file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        message = "Hello {}. This is an automated message.".format(row['First Name'])
        spark.messages.create(toPersonEmail=row['Email'],markdown=message)
