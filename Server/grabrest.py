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
    cur.execute("INSERT INTO nodeData(meterId,nodeId,meterType,V1, V2, V3, I1, I2, I3,F1,F2,F3,PF1,PF2,PF3,W1,W2,W3,VA1,VA2,VA3,VAR1,VAR2,VAR3,WH,VAH,VARH,WH1,WH2,WH3,VAH1,VAH2,VAH3,VARH1,VARH2,VARH3,D1,D2,D3,D4,D5,D6,D7,D8)VALUES( %(meterId)s,%(nodeId)s,%(meterType)s,%(V1)s,%(V2)s,%(V3)s,%(I1)s,%(I2)s,%(I3)s,%(F1)s,%(F2)s,%(F3)s,%(PF1)s,%(PF2)s,%(PF3)s,%(W1)s,%(W2)s,%(W3)s,%(VA1)s,%(VA2)s,%(VA3)s,%(VAR1)s,%(VAR2)s,%(VAR3)s,%(WH)s,%(VAH)s,%(VARH)s,%(WH1)s,%(WH2)s,%(WH3)s,%(VAH1)s,%(VAH2)s,%(VAH3)s,%(VARH1)s,%(VARH2)s,%(VARH3)s,%(D1)s,%(D2)s,%(D3)s,%(D4)s,%(D5)s,%(D6)s,%(D7)s,%(D8)s);",data)
  
  elif dev==41: #Outback Inverter
    json_api=json.loads(api)
    data= json_api['Recent data'][-1]
    print ("Website grabbed")
    print (data)
    txId=0
    cur.execute("INSERT INTO inverterData(nodeid,type,port,battVoltage,aux,error,dev,vac1_in_l2,ac_input,vac_out_l2,inv_mode,inv_i_l2,warn,buy_i_l2,vac_in_l2,sell_i_l2,chg_i_l2,ac_mode) VALUES(%(nodeid)s,%(type)s,%(port)s,%(battVoltage)s,%(aux)s,%(error)s,%(dev)s,%(vac1_in_l2)s,%(ac_input)s,%(vac_out_l2)s,%(inv_mode)s,%(inv_i_l2)s,%(warn)s,%(buy_i_l2)s,%(vac_in_l2)s,%(sell_i_l2)s,%(chg_i_l2)s,%(ac_mode)s);",data)
  elif dev==42: #Outback CC
    json_api=json.loads(api)
    data= json_api['Recent data'][-1]
    print ("Website grabbed")
    print (data)
    txId=0
    cur.execute("INSERT INTO inverterData(nodeid,type,port,battVoltage,aux,error,dev,cc_mode,aux_mode,in_i,out_i,in_v,out_kwh,out_ah ) VALUES(%(nodeid)s,%(type)s,%(port)s,%(battVoltage)s,%(aux)s,%(error)s,%(dev)s,%(cc_mode)s,%(aux_mode)s,%(in_i)s,%(out_i)s,%(in_v)s,%(out_kwh)s,%(out_ah)s);",data)


  
  
  elif dev==0: #events
    json_api=json.loads(api)
    data= json_api['Event Data'][-1]
    print ("Website grabbed")
    print (data)
    txId=data['id']
    cur.execute("SELECT id FROM weather ORDER BY id DESC LIMIT 1")
    weatherID=cur.fetchall()
    weatherID=weatherID[0]
    weatherID=weatherID[0]
    data['weatherID']=weatherID
    print(weatherID)
    cur.execute("INSERT INTO `event` (nodeId,meterId, errorId, errorMsg, errorVal,errorTime,weatherID) VALUES(%(nodeId)s,%(meterId)s,%(errorId)s,%(errorMsg)s,%(errorVal)s,%(errorTime)s,%(weatherID)s);",data)
    print(data)
  elif dev==100:
    json_api=json.loads(api)
    data= json_api['Alive'][-1]
    print ("Website grabbed")
    print (data)
    cur.execute("INSERT INTO nodeHealth(nodeId,alive,temp,SSID,wlan_ss) VALUES(%(nodeId)s,%(alive)s,%(temp)s,%(SSID)s,%(wlan_ss)s);",data)
    txId=1
  elif dev==101:
    json_api=json.loads(api)
    data= json_api['switchState'][-1]
    print ("Website grabbed")
    print (data)
    cur.execute("INSERT INTO maximData(nodeId,C1,C2,C3,C4) VALUES(%(nodeId)s,%(C1)s,%(C2)s,%(C3)s,%(C4)s);",data)
    txId=1
    
  elif dev==2:
    json_api=json.loads(api)
    data= json_api['Recent data'][-1]
    print ("Website grabbed")
    print (data)
    cur.execute("INSERT INTO maximData(nodeid,v1,i1, w1,va1,var1,wh1,vah1,varh1,pf1,f1) VALUES(%(nodeid)s,%(v1)s,%(i1)s,%(w1)s,%(va1)s,%(var1)s,%(wh1)s,%(vah1)s,%(varh1)s,%(pf1)s,%(f1)s);",data)
    txId=1 
  
  else:
    print("none")
  
  cur.close()
  conn.commit()
  conn.close()
  print ("DB Dump success")
  #value=json.dumps(value)
  return txId
