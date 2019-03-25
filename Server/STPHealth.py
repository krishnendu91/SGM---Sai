#!/usr/bin/python3
import pymysql
import datetime
a=1
def stateCalc(nodeId,dbtime,meterId,meterName,A): 
  if A>0:
      state=1
  else:
      state=0
  dbtimeE=dbtime.timestamp()
  timeDrift= datetime.datetime.now().timestamp()-dbtimeE
  data={"dbtime":dbtime,"state":state,"timeDrift":timeDrift,"nodeId":nodeId,"meterId":meterId,"meterName":meterName}
  cur.execute("INSERT INTO `STPState` (dbtime,state,timeDrift,nodeId,meterId,meterName) VALUES (%(dbtime)s,%(state)s,%(timeDrift)s,%(nodeId)s,%(meterId)s,%(meterName)s);",data)
  conn.commit()
  conn.close()
  print("DB Updated with alive state: " +str(alive) + " for Node "+str(nodeid))
  return "Completed"
  
while(a<13):
  conn = pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
  cur=conn.cursor()
  cur.execute("SELECT timestamp,nodeId,meterId,meterName,A FROM STPData where meterId=%s order by id desc limit 1;",a)
  data=cur.fetchone() #fetch all
  dbtime=data[0]
  nodeId=data[1]
  meterId=data[2]
  meterName=data[3]
  A=data[4]
  stateCalc(nodeId,dbtime,meterId,meterName,A)
  conn.close()
  a=a+1
  #except:
   # a=a+1
    #print("Error")
    #exit()
#    if a==15:
 #     aggid=200
  #    conn = pymysql.connect(database="AmritaSGM",user="grafana",password="grafana",host="localhost")
   #   cur=conn.cursor()
    #  cur.execute("SELECT timestamp,aggid,temp,ssid,wlan_ss FROM `nodeHealth` where aggid=%s order by id desc limit 1;",a)
     # data=cur.fetchone() #fetch all
      #dbtime=data[0]
      #nodeid=data[1]
      #temp=data[2]
      #ssid=data[3]
      #wlan_ss=data[4]
      #tdcalc(nodeid,dbtime,temp,ssid,wlan_ss)
