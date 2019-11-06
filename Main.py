#
# Playing code to learn how to handle JSON
#

import sys
import json
import requests
import time
import datetime


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
today = datetime.date.today()
print("Today  : ", today.ctime())
print("SQ test: ", testTime)

# Squarespace API

baseURL = ""
myCursor = ""

import requests

url = "https://api.squarespace.com/1.0/commerce/orders"

querystring = {"fulfillmentStatus":"PENDING"}

headers = {
    'Authorization': "Bearer 15276a39-8522-45a3-8730-ae5df323efd7",
    'User-Agent': "PostmanRuntime/7.19.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "e879f062-4ffa-4c48-8a9a-ade2be98f3b3,c3127bcb-6d9b-45e6-a33a-c9e01e857f52",
    'Host': "api.squarespace.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)










