#!/usr/bin/python3

import paho.mqtt.client as mqtt
import json,grabrest,mqtt_reply
# This is the Subscriber

def on_connect(client, userdata, mid, rc):
	print("Connected with result code "+str(rc))
	print(str(mid))
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
	mqtt_reply.mqttack(broker,reply)
	
client = mqtt.Client()
client.connect("0.0.0.0",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
