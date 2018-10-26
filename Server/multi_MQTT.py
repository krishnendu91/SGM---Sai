#!/usr/bin/python3
import sys
import os
import paho.mqtt.client as paho
import json,grabrest,mqtt_reply

global mqttclient;
global broker;
global port;

broker = "192.168.112.110";
port = 1883;
mypid = os.getpid()
print("Process started at: " +str(mypid))
client_uniq = "pubclient_"+str(mypid)
mqttclient = paho.Client(client_uniq, False) #nocleanstart
mqttclient.connect(broker, port, 60)
mqttclient.subscribe("SGM/#")

def test1(client, userdata, message):
	print("Test Channel")
	print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "' with QoS " + str(message.qos))
  
def datafetch_dimis(client, userdata, msg):
	print("Dimis Data received")
	payload=json.loads(msg.payload.decode())
	
	if payload['ip']:
		print(payload['ip'])

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

def datafetch_maxim(client, userdata, msg):
	print("Maxim Data received")
	payload=json.loads(msg.payload.decode())
	ip_wlan0 = payload['ip']

def datafetch_outback(client, userdata, msg):
	print("Outback Data received")

def datafetch_navsemi(client, userdata, msg):
	print("Navsemi Data received")

def datafetch_gsm(client, userdata, msg):
	print("GSM Data received")

#Subscribed Topics  
mqttclient.message_callback_add("SGM/test1", test1)
mqttclient.message_callback_add("SGM/datafetch_dimis", datafetch_dimis)
mqttclient.message_callback_add("SGM/datafetch_maxim", datafetch_maxim)
mqttclient.message_callback_add("SGM/datafetch_outback", datafetch_outback)
mqttclient.message_callback_add("SGM/datafetch_navsemi", datafetch_navsemi)
mqttclient.message_callback_add("SGM/datafetch_gsm", datafetch_gsm)


mqttclient.loop_forever()

