#!/usr/bin/python3


import telegram,pymysql
bot = telegram.Bot(token='813728431:AAEmpmT-UXIQQcdzwkih8k1XSdCbiMIFP2Q')

def sendmessage(message):
	chat_id =-304438902
	bot.send_message(chat_id=chat_id, text=message)
	return "Done!"


conn = pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur = conn.cursor()
a=1
while a<13:
	cur.execute('SELECT meterName FROM STP where id= %(a)s ;',{'a':a})
	meterName=cur.fetchone()
	meterName=meterName[0]
	#print(meterName)
	cur.execute('SELECT id,state FROM STPState WHERE meterName=%s ORDER by id desc limit 2',meterName)
	data=cur.fetchall()
	idNew=data[0][0]
	stateNew=int(data[0][1])
	print(idNew)
	idOld=data[1][0]
	print(idOld)
	stateOld=int(data[1][1])
	a=a+1
	if (stateOld==stateNew):
		if(stateNew==1):
			print(str(meterName)+ " Turned On")
			sendmessage(str(meterName)+ " Turned On")
		elif(stateNew==0):
			print(str(meterName)+ " Turned OFF")
			sendmessage(str(meterName)+ " Turned OFF")
	else:
		print("No change in State")
		print(meterName+": "+str(stateOld)+str(stateNew))

