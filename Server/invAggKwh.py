#!/usr/bin/python3

import pymysql
conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()
cur.execute("SELECT out_kwh from inverterData where port=2 or 3 or 5 order by id desc limit 3")
data=cur.fetchall()
print(data)
for item in data:
  kwh1=data[0]
  kwh2=data[1]
  kwh3=data[2]
kwh=kwh1+kwh2+kwh3
print(kwh)
cur.execute("Insert into inverterData (totalKwh) values(%s);",kwh)
conn.commit()
conn.close()

