import pymysql,mqtt_reply,mqttservice
conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()
global errorVal
def poweroutage(v1,v2,v3,meterId,nodeId,ip_wlan0):
  if (v1 and v2 and v3 < 0):
    errorVal= v1 and v2 and v3
    conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
    cur=conn.cursor()
    data={'nodeId':nodeId,'errorId':1,'errorMsg':'no input voltage supply','errorVal':errorVal,'meterId':meterId}
    print(data)
    cur.execute("INSERT INTO event(nodeId, meterId, errorId, errorMsg, errorVal) VALUES(%(nodeId)s, %(meterId)s, %(errorId)s, %(errorMsg)s, %(errorVal)s );",data)
    conn.commit()
    conn.close()
    print("Event table updated")
    mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_events","DONE",ip_wlan0)
    #return 
  if (v1 or v2 or v3 ==0):
    if(v1==0):
      errorVal=v1  
    if(v2==0):
      errorVal=v1
    if(v3==0):
      errorVal=v3
    else:
      erroVal=0
    conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
    cur=conn.cursor()
    data={'nodeId':nodeId,'errorId':1,'errorMsg':'Line voltage failed','errorVal':errorVal,'meterId':meterId}
    print(data)
    cur.execute("INSERT INTO event(nodeId, meterId, errorId, errorMsg, errorVal) VALUES(%(nodeId)s, %(meterId)s, %(errorId)s, %(errorMsg)s, %(errorVal)s );",data)
    conn.commit()
    conn.close()

def frequency(f1,f2,f3,meterId,nodeId,ip_wlan0):
  if (f1 or f2 or f3 <49.3):
    if(f1==0):
      errorVal=f1  
    if(f2==0):
      errorVal=f1
    if(f3==0):
      errorVal=f3
    else:
      erroVal=0
    conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
    cur=conn.cursor()
    data={'nodeId':nodeId,'errorId':1,'errorMsg':'Low Frequency Error','errorVal':errorVal,'meterId':meterId}
    print(data)
    cur.execute("INSERT INTO event(nodeId, meterId, errorId, errorMsg, errorVal) VALUES(%(nodeId)s, %(meterId)s, %(errorId)s, %(errorMsg)s, %(errorVal)s );",data)
    conn.commit()
    conn.close()
    
  if (f1 or f2 or f3 >50.8):
    if(f1==0):
      errorVal=f1  
    if(f2==0):
      errorVal=f1
    if(f3==0):
      errorVal=f3
    else:
      erroVal=0
    conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
    cur=conn.cursor()
    data={'nodeId':nodeId,'errorId':1,'errorMsg':'High Frequency Error','errorVal':errorVal,'meterId':meterId}
    print(data)
    cur.execute("INSERT INTO event(nodeId, meterId, errorId, errorMsg, errorVal) VALUES(%(nodeId)s, %(meterId)s, %(errorId)s, %(errorMsg)s, %(errorVal)s );",data)
    conn.commit()
    conn.close() 
 
#def powerquality(v1,v2,v3,meterId,nodeId,ip_wlan0)
  
#def current(i1,i2,i3,meterId,nodeId,ip_wlan0)

    
#INSERT INTO `event` (`id`, `nodeId`, `errorTime`, `errorId`, `errorMsg`, `errorVal`) VALUES ('1', '5', CURRENT_TIMESTAMP, '1', 'Low Voltage', '230')
