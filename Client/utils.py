import sys
import socket,mqttservice
import time,json
from datetime import datetime
import pymysql
from subprocess import check_output

def getmeterid(nodeid,metertype):
  nodeid=str(nodeid)
  metertype=str(metertype)
  conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
  cur=conn.cursor()
  cur.execute("SELECT meterID FROM `Meter` WHERE nodeId=%s and meterType=%s;",(nodeid,metertype))
  meterid=cur.fetchone()
  meterid=int(meterid[0])
  #print(meterid)
  return meterid

def sysinfo():
#get IP addresses
  ip_scanoutput=check_output(["hostname -I"],shell=1)
  ip_eth0=ip_scanoutput.decode().split()[0]
  ip_wlan0=ip_scanoutput.decode().split()[1]

#get node ID
  id_scanoutput=check_output(["hostname"],shell=1)
  id_node=id_scanoutput.decode().split()[0]
  if len(id_node)>9:
  	nodeId=int(id_node[-2:])
  else:
    nodeId=int(id_node[-1:])
  return(ip_eth0,ip_wlan0,nodeId)

def dimisdecode(val,meterType,meterId):
  ip_eth0,ip_wlan0,nodeId=sysinfo()
  json_val=json.loads(val)
  data=json_val['devs'][-1]['data']
#Voltage
  v1=data[0]
  v2=data[1]
  v3=data[2]

#Current
  i1=data[3]
  i2=data[4]
  i3=data[5]

#Power
#Active Power
  w1=data[6]
  w2=data[7]
  w3=data[8]

#Apparent Power
  va1=data[9]
  va2=data[10]
  va3=data[11]

#Reactive Power
  var1=data[12]
  var2=data[13]
  var3=data[14]

#Power Factor
  pf1=data[15]
  pf2=data[16]
  pf3=data[17]

#Frequency
  f1=data[18]
  f2=data[19]
  f3=data[20]

#Total Consumed Active Energy
  wh=data[24]
  vah=data[25]
  varh=data[26]

#Active Energy
  wh1=data[27]
  wh2=data[30]
  wh3=data[33]

#Apparent Energy
  vah1=data[28]
  vah2=data[31]
  vah3=data[34]

#Reactive Energy
  varh1=data[29]
  varh2=data[32]
  varh3=data[35]

#Digital Outputs
  D1=data[37]
  D2=data[38]
  D3=data[39]
  D4=data[40]
  D5=data[41]
  D6=data[42]
  D7=data[43]
  D8=data[44]
  timestamp=datetime.now().strftime('%d-%m-%Y %H:%M:%S')
#Jsonify decoded values
  data={'meterId':meterId,'nodeid':nodeId,'meterType':meterType,'time':timestamp,'v1':v1,'v2':v2,'v3':v3,'i1':i1,'i2':i2,'i3':i3,'w1':w1,'w2':w2,'w3':w3,'var1':var1,'var2':var2,'var3':var3,'va1':va1,'va2':va2,'va3':va3,'pf1':pf1,'pf2':pf2,'pf3':pf3,'f1':f1,'f2':f2,'f3':f3,'wh':wh,'vah':vah,'varh':varh,'wh1':wh1,'wh2':wh2,'wh3':wh3,'varh1':varh1,'varh2':varh2,'varh3':varh3,'vah1':vah1,'vah2':vah2,'vah3':vah3,'D1':D1,'D2':D2,'D3':D3,'D4':D4,'D5':D5,'D6':D6,'D7':D7,'D8':D8}
  return data

#DB Dump for Dimis
def todbdimis(data):
  conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
  cur=conn.cursor()
  cur.execute("INSERT INTO nodeData(meterId,nodeid,meterType, v1, v2, v3, i1, i2, i3, w1,w2,w3,va1,va2,va3,var1,var2,var3,wh,vah,varh,wh1,wh2,wh3,vah1,vah2,vah3,varh1,varh2,varh3,pf1,pf2,pf3,f1,f2,f3,d1,d2,d3,d4,d5,d6,d7,d8) VALUES(%(meterId)s,%(nodeid)s,%(meterType)s,%(v1)s,%(v2)s,%(v3)s,%(i1)s,%(i2)s,%(i3)s,%(w1)s,%(w2)s,%(w3)s,%(va1)s,%(va2)s,%(va3)s,%(var1)s,%(var2)s,%(var3)s,%(wh)s,%(vah)s,%(varh)s,%(wh1)s,%(wh2)s,%(wh3)s,%(vah1)s,%(vah2)s,%(vah3)s,%(varh1)s,%(varh2)s,%(varh3)s,%(pf1)s,%(pf2)s,%(pf3)s,%(f1)s,%(f2)s,%(f3)s,%(D1)s,%(D2)s,%(D3)s,%(D4)s,%(D5)s,%(D6)s,%(D7)s,%(D8)s);",data)
  conn.commit()
  conn.close()
  print ("DB Dump success")
  
def todbmaxim(data):
  conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
  cur=conn.cursor()
  cur.execute("INSERT INTO maximData(nodeid,v1,i1, w1,va1,var1,wh1,vah1,varh1,pf1,f1) VALUES(%(nodeId)s,%(v1)s,%(i1)s,%(w1)s,%(va1)s,%(var1)s,%(wh1)s,%(vah1)s,%(varh1)s,%(pf1)s,%(f1)s);",data)
  conn.commit()
  conn.close()
  print ("DB Dump success")

  #Contactor status update to DB
def switchstatus():
  
  ip_eth0,ip_wlan0,nodeId=sysinfo()
  i2c=check_output(["i2cget -y 1 0x3b"],shell=1)
  i2c=i2c.decode().split()[0]
  i2c=i2c[3:]
  
  if i2c=='f':
    switch={'nodeid':nodeId,'C1':1,'C2':1,'C3':1,'C4':1}
  elif i2c=='e':
    switch={'nodeid':nodeId,'C1':0,'C2':1,'C3':1,'C4':1}
  elif i2c=='d':
    switch={'nodeid':nodeId,'C1':1,'C2':0,'C3':1,'C4':1}
  elif i2c=='c':
    switch={'nodeid':nodeId,'C1':0,'C2':0,'C3':1,'C4':1}
  elif i2c=='b':
    switch={'nodeid':nodeId,'C1':0,'C2':1,'C3':1,'C4':1}
  elif i2c=='a':
    switch={'nodeid':nodeId,'C1':0,'C2':1,'C3':0,'C4':1}
  elif i2c=='9':
    switch={'nodeid':nodeId,'C1':1,'C2':0,'C3':0,'C4':1}
  elif i2c=='8':
    switch={'nodeid':nodeId,'C1':1,'C2':0,'C3':0,'C4':0}
  elif i2c=='7':
    switch={'nodeid':nodeId,'C1':1,'C2':1,'C3':1,'C4':0}
  elif i2c=='6':
    switch={'nodeid':nodeId,'C1':0,'C2':1,'C3':1,'C4':0}
  elif i2c=='5':
    switch={'nodeid':nodeId,'C1':1,'C2':0,'C3':1,'C4':0}
  elif i2c=='4':
    switch={'nodeid':nodeId,'C1':0,'C2':0,'C3':1,'C4':0}
  elif i2c=='3':
    switch={'nodeid':nodeId,'C1':1,'C2':1,'C3':0,'C4':0}
  elif i2c=='2':
    switch={'nodeid':nodeId,'C1':1,'C2':0,'C3':1,'C4':0}
  elif i2c=='1':
    switch={'nodeid':nodeId,'C1':1,'C2':0,'C3':0,'C4':0}
  elif i2c=='0':
    switch={'nodeid':nodeId,'C1':0,'C2':0,'C3':0,'C4':0}
  else:
    switch={'nodeid':nodeId,'C1':0,'C2':0,'C3':0,'C4':0}
  

  print(i2c)
  
  print(switch)

  conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
  cur=conn.cursor()
  cur.execute("INSERT INTO switchState(nodeid,C1, C2, C3, C4) VALUES(%(nodeid)s,%(C1)s,%(C2)s,%(C3)s,%(C4)s);",switch)
  conn.commit()
  conn.close()
  print ("Switch State - DB Dump success")
  
def todbsch(schData):
  conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
  cur=conn.cursor()
  cur.execute("INSERT INTO schData (nodeId, A, A1, A2, A3, VLL, VLN, V1, V2, V3, V12, V23, V31, F, PF, PF1, PF2, PF3, W, W1, W2, W3, VA, VA1, VA2, VA3, WH, VAH, INTR) VALUES (%(nodeId)s, %(A)s, %(A1)s, %(A2)s, %(A3)s, %(VLL)s, %(VLN)s, %(V1)s, %(V2)s, %(V3)s, %(V12)s, %(V23)s, %(V31)s, %(F)s, %(PF)s, %(PF1)s, %(PF2)s, %(PF3)s, %(W)s, %(W1)s, %(W2)s, %(W3)s, %(VA)s, %(VA1)s, %(VA2)s, %(VA3)s, %(WH)s, %(VAH)s, %(INTR)s);",schData)
  conn.commit()
  conn.close()
  print ("Schineider Meter - DB Dump success")

