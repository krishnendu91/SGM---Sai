#!/usr/bin/python3
import telebot,pymysql,time
from datetime import datetime
from datetime import timedelta
bot = telebot.TeleBot(token='813728431:AAEmpmT-UXIQQcdzwkih8k1XSdCbiMIFP2Q')

def sendmessage(message):
	chat_id =-304438902
	bot.send_message(chat_id=chat_id, text=message)
	return "Done!"



conn1 =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur1=conn1.cursor()


cur1.execute("SELECT faclon1, wiman1, wiman2, vvm, embedos FROM `4wardDevStatus` ORDER BY ID DESC LIMIT 1;")
pastData = cur1.fetchone()
status = {"faclon1":pastData[0],"wiman1":pastData[1],"wiman2":pastData[2], "vvm":pastData[3], "embedos":pastData[4]}

#Faclon 869523055584990
cur1.execute("SELECT receiveTime FROM `faclon` WHERE imei = 869523055584990 ORDER BY `faclon`.`receiveTime` DESC LIMIT 1;")
RT = cur1.fetchone()[0]
RT2 = time.mktime(RT.timetuple())
currentTime = time.time()
delta = (currentTime-RT2)
if delta > 600:
	if status["faclon1"] == 0:
		sendmessage("Faclon - 869523055584990 - No data for last 10 min. Last data received time: " + str(RT) )
		faclon1 = 1
else:
	faclon1 = 0

#Wiman 869523057988207
cur1.execute("SELECT receiveTime FROM `wiman` WHERE imei = 869523057988207 ORDER BY `receiveTime` DESC LIMIT 1;")
RT = cur1.fetchone()[0]
RT2 = time.mktime(RT.timetuple())
currentTime = time.time()
delta = (currentTime-RT2)
if delta > 600:
	sendmessage("Wiman - 869523057988207 - No data for last 10 min. Last data received time: " + str(RT) )
	wiman1 = 1
else:
	wiman1 = 0
	

#Wiman 869523057983679
cur1.execute("SELECT receiveTime FROM `wiman` WHERE imei = 869523057983679 ORDER BY `receiveTime` DESC LIMIT 1;")
RT = cur1.fetchone()[0]
RT2 = time.mktime(RT.timetuple())
currentTime = time.time()
delta = (currentTime-RT2)
if delta > 600:
	if status["wiman2"] == 0:
		sendmessage("Wiman - 869523057988207 - No data for last 10 min. Last data received time: " + str(RT) )
		wiman2 = 1
else:
	wiman2 = 0


#VVM AMGW001
cur1.execute("SELECT receiveTime FROM `VVMGateway` WHERE devID = 'AMGW001' ORDER BY `receiveTime` DESC LIMIT 1;")
RT = cur1.fetchone()[0]
RT2 = time.mktime(RT.timetuple())
currentTime = time.time()
delta = (currentTime-RT2)
if delta > 600:
	sendmessage("VVM - AMGW001 - No data for last 10 min. Last data received time: " + str(RT) )
	vvm = 1
else:
	vvm = 0

#Embeddos	
cur1.execute("SELECT timestamp FROM `embedos` ORDER BY `timestamp` DESC LIMIT 1;")
RT = cur1.fetchone()[0]
RT2 = time.mktime(RT.timetuple())
currentTime = time.time()
delta = (currentTime-RT2)
if delta > 600:
	sendmessage("Embeddos - No data for last 10 min. Last data received time: " + str(RT) )
	embedos = 1
else:
	embedos = 0
	

status = {"faclon1":faclon1,"wiman1":wiman1,"wiman2":wiman2, "vvm":vvm, "embedos":embedos}
print(status)
cur1.execute("INSERT INTO 4wardDevStatus (faclon1, wiman1, wiman2, vvm, embedos) VALUES (%(faclon1)s, %(wiman1)s, %(wiman2)s, %(vvm)s, %(embedos)s;",status)
cur1.commit()
conn1.close()

# sendmessage("test")
