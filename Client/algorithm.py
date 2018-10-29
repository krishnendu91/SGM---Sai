import pymysql,mqtt_reply,mqttservice
conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()

def poweroutage(v1,v2,v3,nodeId,ip_wlan0):
  check = v1 or v2 or v3 
  print(type(check))
  if (check == 0):
    data={'nodeId':nodeId,'errorId':1,'errorMsg':'no input voltage supply','errorVal':check}
    print(data)
    cur.execute("INSERT INTO `event` (`nodeId`, `errorId`, `errorMsg`, `errorVal`) VALUES (%(nodeId)s, %(errorId)s, %(errorMsg)s, %(errorVal)s);",data)
    mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_events","DONE",ip_wlan0)
    #return 
  #if (v1|v2|v3==0):
   # print("Line fault")

def frequency(f1,f2,f3):
  if(f1|f2|f3 <49.5):
    print("Low Frequency")
  
  if(f1|f2|f3 >50.5):
    print("High Frequency")
    
#INSERT INTO `event` (`id`, `nodeId`, `errorTime`, `errorId`, `errorMsg`, `errorVal`) VALUES ('1', '5', CURRENT_TIMESTAMP, '1', 'Low Voltage', '230')
