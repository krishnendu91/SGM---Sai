#!/usr/bin/python3
import pymysql
import datetime
a=1

conn = pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur = conn.cursor()

while a<13:
cur.execute('SELECT meterName FROM STP where id= %(a)s ;',{'a':a})
  meterName=cur.fetchone()
  meterName=meterName[0]
