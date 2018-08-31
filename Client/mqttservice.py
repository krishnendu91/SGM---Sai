import paho.mqtt.client as mqtt
import json
def mqtt_publish(broker,port,topic,payload,ip_wlan0):
# This is the Publisher
  #broker="192.168.112.110"
  #port=1883
  #topic="switch"
  #payload="ON"
  payload={'message':payload,"ip":ip_wlan0}
  payload=json.dumps(payload)
  topic="SGM/"+topic
  client = mqtt.Client()
  client.connect(broker,port,60)
  (rc,mid)=client.publish(topic,payload,qos=1);
  
  print(str(rc))
  print(str(mid))
  client.loop()
  client.disconnect();
#acknowledgement 
def on_connect(client, userdata, flags, rc):
	#print("Connected with result code "+str(rc))
	client.subscribe("SGM/ack")
def on_message(client, userdata, msg):
	payload=json.loads(msg.payload.decode())
  print(payload)
def mqtt_ack():
  client = mqtt.Client()
  client.connect("0.0.0.0",1883,60)
  client.on_connect = on_connect
  client.on_message = on_message
  print("ack received")
  client.disconnect()
 
