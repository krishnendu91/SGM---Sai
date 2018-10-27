#!/usr/bin/python3

#Import required libraries
import json,time,pymysql
import sys
from urllib.request import urlopen
conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()

url="https://api.darksky.net/forecast/8636a0eb845f3447caa12fe33102d60f/9.092534,76.489965"
api_page = urlopen(url)
api=api_page.read()
json_api=json.loads(api)
data= json_api['currently']
#print(data)
cur.execute("INSERT INTO weather(time,summary,icon, precipIntensity, precipProbability, precipType, temperature, apparentTemperature,dewPoint,humidity,pressure,windSpeed,windGust,windBearing,cloudCover,uvIndex,visibility,ozone)VALUES(%(time)s,%(summary)s,%(icon)s, %(precipIntensity)s, %(precipProbability)s, %(precipType)s, %(temperature)s, %(apparentTemperature)s,%(dewPoint)s,%(humidity)s,%(pressure)s,%(windSpeed)s,%(windGust)s,%(windBearing)s,%(cloudCover)s,%(uvIndex)s,%(visibility)s,%(ozone)s);",data)
cur.close()
conn.commit()
conn.close()
print("DB Update completed")
