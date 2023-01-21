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

#Faclon 869523055584990
cur1.execute("SELECT receiveTime FROM `faclon` WHERE imei = 869523055584990 ORDER BY `faclon`.`receiveTime` DESC LIMIT 1;")
RT = cur1.fetchone()[0]
RT2 = time.mktime(RT.timetuple())
currentTime = time.time()
print(RT)
print(currentTime)
delta = (currentTime-RT2)
if delta > 600:
	sendmessage("Faclon - 869523055584990 - No data for last 10 min. Last data received time: " + str(RT) )

#Wiman 869523057988207
cur1.execute("SELECT receiveTime FROM `wiman` WHERE imei = 869523057988207 ORDER BY `receiveTime` DESC LIMIT 1;")
RT = cur1.fetchone()[0]
RT2 = time.mktime(RT.timetuple())
currentTime = time.time()
delta = (currentTime-RT2)
if delta > 600:
	sendmessage("Wiman - 869523057988207 - No data for last 10 min. Last data received time: " + str(RT) )
	

#Wiman 869523057983679
cur1.execute("SELECT receiveTime FROM `wiman` WHERE imei = 869523057983679 ORDER BY `receiveTime` DESC LIMIT 1;")
RT = cur1.fetchone()[0]
RT2 = time.mktime(RT.timetuple())
currentTime = time.time()
delta = (currentTime-RT2)
if delta > 600:
	sendmessage("Wiman - 869523057988207 - No data for last 10 min. Last data received time: " + str(RT) )


#VVM AMGW001
cur1.execute("SELECT receiveTime FROM `VVMGateway` WHERE devID = AMGW001 ORDER BY `receiveTime` DESC LIMIT 1;")
RT = cur1.fetchone()[0]
RT2 = time.mktime(RT.timetuple())
currentTime = time.time()
delta = (currentTime-RT2)
if delta > 600:
	sendmessage("VVM - AMGW001 - No data for last 10 min. Last data received time: " + str(RT) )

#Embeddos	
cur1.execute("SELECT timestamp FROM `embedos` WHERE devID = AMGW001 ORDER BY `receiveTime` DESC LIMIT 1;")
RT = cur1.fetchone()[0]
RT2 = time.mktime(RT.timetuple())
currentTime = time.time()
delta = (currentTime-RT2)
if delta > 600:
	sendmessage("Embeddos - No data for last 10 min. Last data received time: " + str(RT) )

	

conn1.close()

# sendmessage("test")
