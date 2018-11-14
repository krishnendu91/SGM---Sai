import pymysql,mqtt_reply,mqttservice
conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()
global errorVal_po
global errorVal_f
global errorVal_pq
global errorVal_i

errorVal_po=0
errorVal_f=0
errorVal_pq=0
errorVal_i=0
def poweroutage(v1,v2,v3,meterId,nodeId,ip_wlan0):
  if (v1 and v2 and v3 < 0):
    errorVal_po= v1 and v2 and v3
    conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
    cur=conn.cursor()
    data={'nodeId':nodeId,'errorId':1,'errorMsg':'no input voltage supply','errorVal':errorVal_po,'meterId':meterId}
    print(data)
    cur.execute("INSERT INTO event(nodeId, meterId, errorId, errorMsg, errorVal) VALUES(%(nodeId)s, %(meterId)s, %(errorId)s, %(errorMsg)s, %(errorVal)s );",data)
    conn.commit()
    conn.close()
    print("Event table updated")
    mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_events","DONE",ip_wlan0)
    #return 
  elif (v1 or v2 or v3 ==0):
    if(v1==0):
      errorVal_po=v1  
    elif(v2==0):
      errorVal_po=v1
    elif(v3==0):
      errorVal_po=v3
    else:
      errorVal_po=0
    conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
    cur=conn.cursor()
    data={'nodeId':nodeId,'errorId':1,'errorMsg':'Line voltage failed','errorVal':errorVal_po,'meterId':meterId}
    print(data)
    cur.execute("INSERT INTO event(nodeId, meterId, errorId, errorMsg, errorVal) VALUES(%(nodeId)s, %(meterId)s, %(errorId)s, %(errorMsg)s, %(errorVal)s );",data)
    conn.commit()
    conn.close()
    print("Event table updated")
    mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_events","DONE",ip_wlan0)

def frequency(f1,f2,f3,meterId,nodeId,ip_wlan0):
  if (f1 or f2 or f3 <49.3):
    if(f1==0):
      errorVal_f=f1  
    elif(f2==0):
      errorVal_f=f1
    elif(f3==0):
      errorVal_f=f3
    else:
      errorVal_f=0
    conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
    cur=conn.cursor()
    data={'nodeId':nodeId,'errorId':1,'errorMsg':'Low Frequency Error','errorVal':errorVal_f,'meterId':meterId}
    print(data)
    cur.execute("INSERT INTO event(nodeId, meterId, errorId, errorMsg, errorVal) VALUES(%(nodeId)s, %(meterId)s, %(errorId)s, %(errorMsg)s, %(errorVal)s );",data)
    conn.commit()
    conn.close()
    print("Event table updated")
    mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_events","DONE",ip_wlan0)
    
  elif (f1 or f2 or f3 >50.8):
    if(f1==0):
      errorVal_f=f1  
    elif(f2==0):
      errorVal_f=f1
    elif(f3==0):
      errorVal_f=f3
    else:
      errorVal_f=0
    conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
    cur=conn.cursor()
    data={'nodeId':nodeId,'errorId':1,'errorMsg':'High Frequency Error','errorVal':errorVal_f,'meterId':meterId}
    print(data)
    cur.execute("INSERT INTO event(nodeId, meterId, errorId, errorMsg, errorVal) VALUES(%(nodeId)s, %(meterId)s, %(errorId)s, %(errorMsg)s, %(errorVal)s );",data)
    conn.commit()
    conn.close() 
    print("Event table updated")
    mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_events","DONE",ip_wlan0)
 
def powerquality(v1,v2,v3,meterId,nodeId,ip_wlan0):
    if (200<v1 or v2 or v3 >250):
      errorVal_pq=v1 or v2 or v3
      conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
      cur=conn.cursor()
      data={'nodeId':nodeId,'errorId':1,'errorMsg':'Power Quality Error','errorVal':errorVal_pq,'meterId':meterId}
      print(data)
      cur.execute("INSERT INTO event(nodeId, meterId, errorId, errorMsg, errorVal) VALUES(%(nodeId)s, %(meterId)s, %(errorId)s, %(errorMsg)s, %(errorVal)s );",data)
      conn.commit()
      conn.close()
      print("Event table updated")
      mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_events","DONE",ip_wlan0)
    else:
      errorVal_pq=0
    
def current(i1,i2,i3,meterId,nodeId,ip_wlan0):
    if (i1 or i2 or i3 >5):
      errorVal_i=i1 or i2 or i3
      conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
      cur=conn.cursor()
      data={'nodeId':nodeId,'errorId':1,'errorMsg':'Power Quality Error','errorVal':errorVal_i,'meterId':meterId}
      print(data)
      cur.execute("INSERT INTO event(nodeId, meterId, errorId, errorMsg, errorVal) VALUES(%(nodeId)s, %(meterId)s, %(errorId)s, %(errorMsg)s, %(errorVal)s );",data)
      conn.commit()
      conn.close()
      print("Event table updated")
      mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_events","DONE",ip_wlan0)
    else
      errorVal_i=0
    

    
#INSERT INTO `event` (`id`, `nodeId`, `errorTime`, `errorId`, `errorMsg`, `errorVal`) VALUES ('1', '5', CURRENT_TIMESTAMP, '1', 'Low Voltage', '230')
