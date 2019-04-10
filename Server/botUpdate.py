#!/usr/bin/python3

import telegram,pymysql
bot = telegram.Bot(token='813728431:AAEmpmT-UXIQQcdzwkih8k1XSdCbiMIFP2Q')

conn = pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur = conn.cursor()

while a<13:
	cur.execute('SELECT meterName FROM STP where id= %(a)s ;',{'a':a})
	meterName=cur.fetchone()
	meterName=meterName[0]
	#print(meterName)
	cur.execute('SELECT id,state FROM STPState WHERE meterName=%s ORDER by id desc limit 1',meterName)
	data=cur.fetchone()
  idNew=data[0]
  stateNew=data[1]
  id=idNew-1
  cur.execute('SELECT id,state FROM STPState WHERE where id=%(id)s meterName=%(meterName)s ORDER by id desc limit 1',{'meterName':meterName,'id':id})
	data=cur.fetchone()
  idOld=data[0]
  stateOld=data[1]
  
  if (stateOld!=StateNew):
    if(stateNew==1):
      print("str(meterName)+ " Turned On")
      sendmessage(str(meterName)+ " Turned On")
    elif(stateNew==0):
      print("str(meterName)+ " Turned OFF")
      sendmessage(str(meterName)+ " Turned OFF")
  else:
      print("No change in State")
  
def sendmessage(message):
  chat_id =-304438902
  bot.send_message(chat_id=chat_id, text=message)
  return "Done!"
