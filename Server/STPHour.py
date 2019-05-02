#!/usr/bin/python3
import pymysql
import datetime
import errornotify as EN
a=1


conn = pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur = conn.cursor()

while a<13:
	cur.execute('SELECT meterName FROM STP where id= %(a)s ;',{'a':a})
	meterName=cur.fetchone()
	meterName=meterName[0]
#	print(meterName)
	cur.execute('SELECT A,VLL,W,F,PF,max(WH),timestamp FROM STPData WHERE meterName=%s ORDER by id desc limit 1',meterName)
	data=cur.fetchone()
	A=data[0]
	VLL=data[1]
	W=data[2]
	F=data[3]
	PF=data[4]
	WH=data[5]
	dbtime=data[6]
	try:
		cur.execute('SELECT WH,timestamp FROM STPData WHERE meterName=%s and timestamp < DATE_SUB(NOW(),INTERVAL 1 HOUR) ORDER by id desc limit 1',meterName)
		data=cur.fetchone()
		WH_old=data[0]
		dbtime_old=data[1]
	except Exception as e:
		print(e)
		EN.sendmessage('STPHour.py '+str(e))
	try:
		WH_new=float(WH)-float(WH_old)
		if(WH_new<=0):
			WH_new=0
	except Exception as e:
		print(str(e))
		EN.sendmessage('STPHour.py '+str(e))
		WH_new=0
		pass
	newData={'meterName':meterName,'A':A,'VLL':VLL,'W':W,'F':F,'PF':PF,'WH':WH_new,'dbtime':dbtime}
	print(meterName,WH_new)
	#print(newData)
	cur.execute("INSERT INTO STPHourData(meterName,A, VLL,F,PF,W,WH,dbtime) VALUES (%(meterName)s,%(A)s, %(VLL)s,%(F)s,%(PF)s,%(W)s,%(WH)s,%(dbtime)s);",newData)
	a=a+1
cur.close()
conn.commit()
conn.close()
	
	
