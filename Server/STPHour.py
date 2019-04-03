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
	print(meterName)
	cur.execute('SELECT A,VLL,W,F,PF,max(WH),timestamp FROM STPData WHERE meterName=%s ORDER by id desc limit 1',meterName)
	data=cur.fetchone()
	A=data[0]
	VLL=data[1]
	W=data[2]
	F=data[3]
	PF=data[4]
	WH=data[5]
	dbtime=data[6]
	cur.execute('SELECT max(WH),timestamp FROM STPData WHERE meterName=%s and timestamp >= DATE_SUB(NOW(),INTERVAL 1 HOUR) ORDER by id desc limit 1',meterName)
	data=cur.fetchone()
	WH_old=data[0]
	dbtime_old=data[1]
	print(WH,dbtime)
	print(WH_old,dbtime_old)
	WH_new=float(WH)-float(WH_old)
	print(WH_new)
	a=a+1
	
