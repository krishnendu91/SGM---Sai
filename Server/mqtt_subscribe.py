#!/usr/bin/python3

import paho.mqtt.client as mqtt
import json,grabrest
# This is the Subscriber

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("SGM/datafetch")

def on_message(client, userdata, msg):
	payload=json.loads(msg.payload.decode())
	if payload['message'] == "DONE":
		ip_wlan0= payload['ip']
		api='recentgm'
		grabrest.grab(ip_wlan0,api)
		reply="SUCCESS"
		print(reply)
		mqttack(reply)
		
	else:
		status=msg.payload.decode()
		print(status)
		reply="FAIL"
		print(reply)
		mqttack(reply)

def mqttack(reply):
	client = mqtt.Client()
	client.connect(broker,port,60)
	client.publish("SGM/ack",reply);
	client.disconnect()
	print('acksent')
	
	
client = mqtt.Client()
client.connect("0.0.0.0",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
