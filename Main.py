#
# Playing code to learn how to handle JSON
#

import sys
import json
import request
import time
from datetime import datetime


print("Playing with JSON...")

# load a JSON record from file, squarespace order record format (see data model in project
filehandler = open("sqRecord.txt", "r")
record = filehandler.readline()

# print a bit of stuff just to check (length read and first 64 characters)
print("Record length: ", len(record))
print(record[:64])
print("...")

# now onto JSON stuff
# first, pretty print

pRecord = json.loads(record)
orderId = pRecord["id"]
billingAddress = pRecord["billingAddress"]
shippingAddress = pRecord["shippingAddress"]
lineItems = pRecord["lineItems"]

print("Order Id: ", orderId)
print(billingAddress["lastName"])

# Testing time ISO 8601 date and time string
testTime = "2016-04-10T12:00:00Z"
today = datetime.today()
print("Today: ", today)
print("Iso: ", today.isoformat())








