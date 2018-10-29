import pymysql,mqtt_reply,mqttservice
conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()

def poweroutage(v1,v2,v3,ip_wlan0):
  if (int(v1)&int(v2)&int(v3)==0):
    print("no input voltage supply")
    cur.execute("INSERT INTO `event` (`nodeId`, `errorId`, `errorMsg`, `errorVal`) VALUES ('5', '1', 'no input voltage supply', '230');")
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
