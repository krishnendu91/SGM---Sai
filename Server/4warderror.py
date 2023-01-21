#!/usr/bin/python3
import telebot,pymysql
bot = telebot.TeleBot(token='813728431:AAEmpmT-UXIQQcdzwkih8k1XSdCbiMIFP2Q')

def sendmessage(message):
	chat_id =-304438902
	bot.send_message(chat_id=chat_id, text=message)
	return "Done!"



conn1 =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur1=conn1.cursor()



# cur1.execute("SELECT  INTO mqttTest(message,topic,qos) VALUES(%(message)s,%(topic)s,%(qos)s);",mqttData)

conn1.commit()
conn1.close()

sendmessage("test")
