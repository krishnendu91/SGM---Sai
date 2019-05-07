#!/usr/bin/python3
import telegram,pymysql
bot = telegram.Bot(token='813728431:AAEmpmT-UXIQQcdzwkih8k1XSdCbiMIFP2Q')

def sendmessage(message):
	chat_id =337874213
	bot.send_message(chat_id=chat_id, text=message)
	return "Done!"
