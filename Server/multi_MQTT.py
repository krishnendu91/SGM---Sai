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
print(mypid)
client_uniq = "pubclient_"+str(mypid)
mqttclient = paho.Client(client_uniq, False) #nocleanstart
mqttclient.connect(broker, port, 60)
mqttclient.subscribe("SGM/#")

def test1(client, userdata, message):
  print("test1")
  print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "' with QoS " + str(message.qos))
  
def datafetch(client, userdata, msg):
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
  
mqttclient.message_callback_add("SGM/test1", test1)
mqttclient.message_callback_add("SGM/datafetch", datafetch)
mqttclient.loop_forever()

