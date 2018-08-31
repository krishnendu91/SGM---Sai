import paho.mqtt.client as mqtt
import json

#acknowledgement 
def on_connect(client1, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client1.subscribe("SGM/ack")
def on_message(client1, userdata, msg):
	payload=msg.payload.decode()
	print(payload)
def mqttack():
	client1 = mqtt.Client()
	client1.connect("0.0.0.0",1883,60)
	#client.subscribe("SGM/ack")
	client1.on_connect = on_connect
	client1.on_message = on_message
	print("ack received")
	
  #client.disconnect()
 
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
	client.publish(topic,payload);
	client.disconnect();
	mqttack()

