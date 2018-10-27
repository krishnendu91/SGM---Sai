#!/usr/bin/python3

#Import required libraries
import json,time,pymysql
import sys
from urllib.request import urlopen

#def current:
url="https://api.darksky.net/forecast/8636a0eb845f3447caa12fe33102d60f/9.092534,76.489965"
api_page = urlopen(url)
api=api_page.read()
json_api=json.loads(api)
data= json_api['currently']
print(data)
