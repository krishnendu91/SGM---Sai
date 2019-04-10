#!/usr/bin/python3

import telegram
bot = telegram.Bot(token='813728431:AAEmpmT-UXIQQcdzwkih8k1XSdCbiMIFP2Q')
chat_id =-304438902

def sendmessage(message):
  bot.send_message(chat_id=chat_id, text="Power Outage!")
  return "Message Sent"
