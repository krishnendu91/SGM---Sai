#!/usr/bin/python3
import pymysql
import datetime
a=1

def tdcalc(nodeId,dbtime):
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
  data={"dbtime":dbtime,"alive":alive,"timedrift":timedrift,"nodeid":nodeid}
  cur.execute("INSERT INTO `lastseen` (dbtime,alive,timedrift,nodeid) VALUES (%(dbtime)s,%(alive)s,%(timedrift)s,%(nodeid)s);",data)
  conn.commit()
  conn.close()
  print("DB Updated with alive state: " +str(alive) + " for Node "+str(nodeid))
while(a<14):
  try:
    conn = pymysql.connect(database="AmritaSGM",user="grafana",password="grafana",host="localhost")
    cur=conn.cursor()
    cur.execute("SELECT timestamp,nodeid FROM `nodeHealth` where nodeid=%s order by id desc limit 1;",a)
    data=cur.fetchone() #fetch all

    dbtime=data[0]
    nodeid=data[1]
    tdcalc(nodeid,dbtime)
    conn.close()
    a=a+1
  except:
    continue




