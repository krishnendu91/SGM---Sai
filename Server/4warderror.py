#!/usr/bin/python3
import telebot,pymysql,time
from datetime import timedelta
bot = telebot.TeleBot(token='813728431:AAEmpmT-UXIQQcdzwkih8k1XSdCbiMIFP2Q')

def sendmessage(message):
	chat_id =-304438902
	bot.send_message(chat_id=chat_id, text=message)
	return "Done!"



conn1 =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur1=conn1.cursor()
cur1.execute("SELECT receiveTime FROM `faclon`  ORDER BY `faclon`.`receiveTime`  DESC LIMIT 1")
faclonRT = time.mktime(cur1.fetchone()[0].timetuple())
currentTime = time.time()
print(faclonRT)
print(currentTime)
print((currentTime-faclonRT).total_seconds()/60)

conn1.close()

# sendmessage("test")
