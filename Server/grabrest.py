#!/usr/bin/python

#Import required libraries
import json,time,pymysql
import sys
from urllib.request import urlopen
#Define a page opener using inbuilt function from urllib2
#opener=urllib2.build_opener()
def grab(ip,api_req,dev):
  url='http://'+str(ip)+':5000/'+str(api_req)
  print (url)
  conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
  cur=conn.cursor()
# api_page=opener.open(url) For Python 2
  api_page = urlopen(url) #Python 3
#Read the api output from the variable 
  api=api_page.read()

  if dev==1: #Dimis
    json_api=json.loads(api)
    data= json_api['Recent data'][-1]
    print ("Website grabbed")
    print (data)
    txId=data['id']  
    cur.execute("INSERT INTO nodeData(nodeId,meterType,V1, V2, V3, I1, I2, I3,F1,F2,F3,PF1,PF2,PF3,W1,W2,W3,VA1,VA2,VA3,VAR1,VAR2,VAR3,WH,VAH,VARH,WH1,WH2,WH3,VAH1,VAH2,VAH3,VARH1,VARH2,VARH3,D1,D2,D3,D4,D5,D6,D7,D8)VALUES(%(nodeId)s,%(meterType)s,%(v1)s,%(V2)s,%(V3)s,%(I1)s,%(I2)s,%(I3)s,%(F1)s,%(F2)s,%(F3)s,%(PF1)s,%(PF2)s,%(PF3)s,%(W1)s,%(W2)s,%(W3)s,%(VA1)s,%(VA2)s,%(VA3)s,%(VAR1)s,%(VAR2)s,%(VAR3)s,%(WH)s,%(VAH)s,%(VARH)s,%(WH1)s,%(WH2)s,%(WH3)s,%(VAH1)s,%(VAH2)s,%(VAH3)s,%(VARH1)s,%(VARH2)s,%(VARH3)s,%(D1)s,%(D2)s,%(D3)s,%(D4)s,%(D5)s,%(D6)s,%(D7)s,%(D8)s);",data)
  
  elif dev==0: #events
    json_api=json.loads(api)
    data= json_api['Event Data'][-1]
    print ("Website grabbed")
    print (data)
    txId=data['id']
    weatherID = cur.execute("SELECT id from weather ORDER BY id DESC LIMIT 1")
    data['weatherID']=weatherID
    cur.execute("INSERT INTO `event` (nodeId, errorId, errorMsg, errorVal,errorTime,weatherID) VALUES(%(nodeId)s,%(errorID)s,%(errorMsg)s,%(errorVal)s,%(errorTime)s,%(weatherID)s);",data)
    print(data)
  else:
    print("none")
  
  cur.close()
  conn.commit()
  conn.close()
  print ("DB Dump success")
  #value=json.dumps(value)
  return txId
