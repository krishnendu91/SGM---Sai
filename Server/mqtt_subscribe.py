#!/usr/bin/python3

import paho.mqtt.client as mqtt
import json,grabrest,mqtt_reply
# This is the Subscriber

def on_message(client, userdata, msg):
	payload=json.loads(msg.payload.decode())
	ip_wlan0 = payload['ip']
	if payload['message'] == "DONE":
		api='recentgm'
		txId=grabrest.grab(ip_wlan0,api,1)
		reply={'message':'SUCCESS',"id":txId}
		
		print(reply)
		
		
	else:
		status=msg.payload.decode()
		print(status)
		reply="FAIL"
		print(reply)
	reply=json.dumps(reply)
	mqtt_reply.mqttack(ip_wlan0,reply)
	
client = mqtt.Client()
client.connect("0.0.0.0",1883,60)
client.subscribe("SGM/datafetch")
client.on_message = on_message
client.loop_forever()
