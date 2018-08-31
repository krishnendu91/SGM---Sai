#!/usr/bin/python3

import paho.mqtt.client as mqtt
import json,grabrest
# This is the Subscriber

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("SGM/datafetch")

def on_message(client, userdata, msg):
	payload=json.loads(msg.payload.decode())
	broker=payload['ip']
	if payload['message'] == "DONE":
		ip_wlan0= payload['ip']
		api='recentgm'
		grabrest.grab(ip_wlan0,api)
		reply="SUCCESS"
		print(reply)
		
		
	else:
		status=msg.payload.decode()
		print(status)
		reply="FAIL"
		print(reply)
	mqttack(broker,reply)
def mqttack(broker,reply):
	client1 = mqtt.Client()
	client1.connect(broker,1883,60)
	client1.publish("SGM/ack",reply);
	client1.disconnect()
	print('acksent')
	
	
client = mqtt.Client()
client.connect("0.0.0.0",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
