#!/usr/bin/python3
import pymysql
import datetime
a=1

def tdcalc(nodeId,dbtime,temp,ssid,wlan_ss):
  dbtimeE=dbtime.timestamp() #Epoch conversion
  timenow=datetime.datetime.now()
  print(timenow)
  timenow=datetime.datetime.now().timestamp() #get current time in Epoch
  print(timenow)
  timedrift=timenow-dbtimeE
  print(timedrift)
  #timedrift=datetime.datetime.fromtimestamp(timedrift).strftime('%s')
  #print(timedrift)

  if timedrift<420:
    alive=1
  else:
    alive=0

  conn = pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
  cur=conn.cursor()
  data={"dbtime":dbtime,"alive":alive,"timedrift":timedrift,"nodeid":nodeid,"temp":temp,"ssid":ssid,"wlan_ss":wlan_ss}
  cur.execute("INSERT INTO `lastseen` (dbtime,alive,timedrift,nodeid,temp,ssid,wlan_ss) VALUES (%(dbtime)s,%(alive)s,%(timedrift)s,%(nodeid)s,%(temp)s,%(ssid)s,%(wlan_ss)s);",data)
  conn.commit()
  conn.close()
  print("DB Updated with alive state: " +str(alive) + " for Node "+str(nodeid))
while(a<15):
  try:
    conn = pymysql.connect(database="AmritaSGM",user="grafana",password="grafana",host="localhost")
    cur=conn.cursor()
    cur.execute("SELECT timestamp,nodeid,temp,ssid,wlan_ss FROM `nodeHealth` where nodeid=%s order by id desc limit 1;",a)
    data=cur.fetchone() #fetch all
    dbtime=data[0]
    nodeid=data[1]
    temp=data[2]
    ssid=data[3]
    wlan_ss=data[4]
    
    tdcalc(nodeid,dbtime,temp,ssid,wlan_ss)
    conn.close()
    a=a+1
  except:
    pass
