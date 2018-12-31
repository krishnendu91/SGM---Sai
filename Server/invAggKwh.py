#!/usr/bin/python3

import pymysql
conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()
cur.execute("SELECT out_kwh from inverterData where port=2 or 3 or 5 order by id desc limit 3")
data=cur.fetchall()
#print(data)
for item in data:
  kwh1=data[0]
  kwh2=data[1]
  kwh3=data[2]
kwh=kwh1[0]+kwh2[0]+kwh3[0]
#print(kwh)
avgData={'nodeId':14,'kwh':kwh,'type':'avg'}
cur.execute("Insert into inverterData (nodeId,totalKwh,type) values(%(nodeId)s,%(kwh)s,%(type)s);",avgData)
conn.commit()
conn.close()

