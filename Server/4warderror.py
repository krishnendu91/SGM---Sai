#!/usr/bin/python3
import telebot,pymysql,time
from datetime import datetime
from datetime import timedelta
bot = telebot.TeleBot(token='6607765727:AAH28KUmQUwPRVHxE-fIkqL3rQYZPS-b1sk')
def sendmessage(message):
	chat_id =-663842076
	bot.send_message(chat_id=chat_id, text=message)
	return "Done!"
conn1 =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur1=conn1.cursor()
wiman2=0
cur1.execute("SELECT faclon1, wiman1, wiman2, vvm001, vvm005, vvm007, embedos FROM `4wardDevStatus` ORDER BY ID DESC LIMIT 1;")
pastData = cur1.fetchone()
faclon1 = pastData[0]
status = {"faclon1":pastData[0],"wiman1":pastData[1],"wiman2":pastData[2], "vvm001":pastData[3], "vvm005":pastData[4], "vvm007":pastData[5], "embedos":pastData[6]}
print(status)
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
		faclon1 = status["faclon1"]
elif delta < 600:
	if status["faclon1"] == 1:
		sendmessage("Faclon - 869523055584990 - Device Up at " + str(RT) )
		faclon1 = 0
	else:
		faclon1 = status["faclon1"]
else:
	faclon1 = 0

#Wiman 869523057988207
cur1.execute("SELECT receiveTime FROM `wiman` WHERE imei = 869523057988207 ORDER BY `receiveTime` DESC LIMIT 1;")
RT = cur1.fetchone()[0]
RT2 = time.mktime(RT.timetuple())
currentTime = time.time()
delta = (currentTime-RT2)

if delta > 600:
	if status["wiman1"] == 0:
		sendmessage("Wiman - 869523057988207 - No data for last 10 min. Last data received time: " + str(RT) )
		wiman1 = 1
	else:
		wiman1 = status["wiman1"]
elif delta < 600:
	if status["wiman1"] == 1:
		sendmessage("Wiman - 869523057988207 - No data for last 10 min. Last data received time: " + str(RT) )
		wiman1 = 0
	else:
		wiman1 = status["wiman1"]
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
		sendmessage("Wiman - 869523057983679 - No data for last 10 min. Last data received time: " + str(RT) )
		wiman2 = 1
	else:
		wiman2 = status["wiman2"]
elif delta < 600:
	if status["wiman2"] == 1:
		sendmessage("Wiman - 869523057983679 - No data for last 10 min. Last data received time: " + str(RT) )
		wiman2 = 0
	else:
		wiman2 = status["wiman2"]

		
else:
	wiman2 = 0
#VVM AMGW001
cur1.execute("SELECT receiveTime FROM `VVMGateway` WHERE devID = 'AMGW001' ORDER BY `receiveTime` DESC LIMIT 1;")
RT = cur1.fetchone()[0]
RT2 = time.mktime(RT.timetuple())
currentTime = time.time()
delta = (currentTime-RT2)
if delta > 600:
	if status["vvm001"] == 0:
		sendmessage("VVM - AMGW001 - No data for last 10 min. Last data received time: " + str(RT) )
		vvm1 = 1
	else:
		vvm1 = status["vvm001"]

elif delta < 600:
	if status["vvm001"] == 1:
		sendmessage("VVM - AMGW001 - Device up at: " + str(RT) )
		vvm1 = 0
	else:
		vvm1 = status["vvm001"]		
else:
	vvm1 = 1

#VVM AMGW007
cur1.execute("SELECT receiveTime FROM `VVMGateway` WHERE devID = 'AMGW007' ORDER BY `receiveTime` DESC LIMIT 1;")
RT = cur1.fetchone()[0]
RT2 = time.mktime(RT.timetuple())
currentTime = time.time()
delta = (currentTime-RT2)
if delta > 600:
	if status["vvm007"] == 0:
		sendmessage("VVM - AMGW007 - No data for last 10 min. Last data received time: " + str(RT) )
		vvm7 = 1
	else:
		vvm7 = status["vvm007"]
		

elif delta < 600:
	if status["vvm007"] == 1:
		sendmessage("VVM - AMGW007 - Device up at: " + str(RT) )
		vvm7 = 0
	else:
		vvm7 = status["vvm007"]		
else:
	vvm7 = 1
	
#VVM AMGW005
cur1.execute("SELECT receiveTime FROM `VVMGateway` WHERE devID = 'AMGW005' ORDER BY `receiveTime` DESC LIMIT 1;")
RT = cur1.fetchone()[0]
RT2 = time.mktime(RT.timetuple())
currentTime = time.time()
delta = (currentTime-RT2)
if delta > 600:
	if status["vvm005"] == 0:
		sendmessage("VVM - AMGW005 - No data for last 10 min. Last data received time: " + str(RT) )
		vvm5 = 1
	else:
		vvm5 = status["vvm005"]
		

elif delta < 600:
	if status["vvm005"] == 1:
		sendmessage("VVM - AMGW005 - Device up at: " + str(RT) )
		vvm5 = 0
	else:
		vvm5 = status["vvm005"]		
else:
	vvm5 = 1



#Embeddos	
cur1.execute("SELECT timestamp FROM `embedos` ORDER BY `timestamp` DESC LIMIT 1;")
RT = cur1.fetchone()[0]
RT2 = time.mktime(RT.timetuple())
currentTime = time.time()
delta = (currentTime-RT2)
if delta > 600:
	if status["embedos"] == 0:
		sendmessage("Embeddos - No data for last 10 min. Last data received time: " + str(RT) )
		embedos = 1
	else:
		embedos = status["embedos"]
else:
	embedos = 0

	
status = {"faclon1":faclon1,"wiman1":wiman1,"wiman2":wiman2, "vvm001":vvm1, "vvm005":vvm5, "vvm007":vvm7, "embedos":embedos}
print(status)

cur1.execute("INSERT INTO `4wardDevStatus`(`faclon1`, `wiman1`, `wiman2`, `vvm001`, `vvm005`, `vvm007`, `embedos`) VALUES (%(faclon1)s, %(wiman1)s, %(wiman2)s, %(vvm001)s, %(vvm005)s, %(vvm007)s, %(embedos)s);",status)
conn1.commit()
conn1.close()
# sendmessage("test")
