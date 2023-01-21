#!/usr/bin/python3
import telebot
bot = telebot.TeleBot(token='813728431:AAEmpmT-UXIQQcdzwkih8k1XSdCbiMIFP2Q')

def sendmessage(message):
	chat_id =-304438902
	bot.send_message(chat_id=chat_id, text=message)
	return "Done!"

sendmessage("test")
