#!/usr/bin/python3
import sys
import os,ast
import paho.mqtt.client as paho
import json,grabrest,mqtt_reply,pymysql

global mqttclient;
global broker;
global port;
conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()
broker = "192.168.112.110";
port = 1883;
mypid = os.getpid()
print("Process started at: " +str(mypid))
client_uniq = "pubclient_"+str(mypid)
#mqttclient = paho.Client() #cleanstart

mqttclient = paho.Client(client_uniq, False) #nocleanstart
mqttclient.connect(broker, port, 0)
#mqttclient.on_disconnect=mqttclient.reconnect()
mqttclient.subscribe("SGM/#")


def datagrab(payload,api,dev):
	ip_wlan0 = payload['ip']
	if payload['message'] == "DONE":
		txId=grabrest.grab(ip_wlan0,api,dev)
		reply={'message':'SUCCESS',"id":txId}
		print(reply)
	else:
		status=msg.payload.decode()
		print(status)
		reply="FAIL"
		print(reply)
	reply=json.dumps(reply)
	#mqtt_reply.mqttack(ip_wlan0,reply)

def test(client, userdata, message):
	print("Test Channel")
	print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "' with QoS " + str(message.qos))
	conn1 =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
	cur1=conn1.cursor()
	mqttData={'message':str(message.payload),'topic':message.topic,'qos':str(message.qos)}
	cur1.execute("INSERT INTO mqttTest(message,topic,qos) VALUES(%(message)s,%(topic)s,%(qos)s);",mqttData)
	conn1.commit()
	conn1.close()
	print("DB DUMP suceess for MQTT Test")
	
def datafetch_dimis_gm1_direct(client, userdata, msg):
	print("Direct MQTT Message received")
	payload=json.loads(msg.payload.decode())
	print(payload)
	payload=dict((k.lower(), v) for k, v in payload.iteritems())
	grabrest.todb(payload,1)
	print(payload)

def datafetch_dimis_gm1(client, userdata, msg):
	print("Dimis Data received")
	payload=json.loads(msg.payload.decode())
	try:
		datagrab(payload,'recentgm',1)
	except:
		pass
	
def datafetch_dimis_lm1(client, userdata, msg):
	print("Dimis Data received")
	payload=json.loads(msg.payload.decode())
	try:
		datagrab(payload,'recentlm1',1)
	except:
		pass

def datafetch_dimis_lm2(client, userdata, msg):
	print("Dimis Data received")
	payload=json.loads(msg.payload.decode())
	try:
		datagrab(payload,'recentlm2',1)
	except:
		pass

def datafetch_maxim(client, userdata, msg):
	print("Maxim Data received")
	payload=json.loads(msg.payload.decode())
	datagrab(payload,'maxim',2)

def datafetch_sch(client, userdata, msg):
	print("Schneider Data received")
	payload=json.loads(msg.payload.decode())
	datagrab(payload,'sch',3)
	
def datafetch_outback_inv(client, userdata, msg):
	print("Outback Data received")
	payload=json.loads(msg.payload.decode())
	datagrab(payload,'outbackinv',41)

def datafetch_outback_cc(client, userdata, msg):
	print("Outback Data received")
	payload=json.loads(msg.payload.decode())
	datagrab(payload,'outbackcc',42)

def datafetch_navsemi(client, userdata, msg):
	print("Navsemi Data received")
	payload=json.loads(msg.payload.decode())
	datagrab(payload,'navsemi',5)

def datafetch_gsm(client, userdata, msg):
	print("GSM Data received")
	#TBD
def datafetch_events(client, userdata, msg):
	print("Event Data received")
	payload=json.loads(msg.payload.decode())
	datagrab(payload,'events',0) 

def node_alive(client, userdata, msg):
	print("Alive beacon received")
	payload=json.loads(msg.payload.decode())
	datagrab(payload,'alive',100)
	
def datafetch_switch(client, userdata, msg):
	print("Switch Status received")
	payload=json.loads(msg.payload.decode())
	datagrab(payload,'switchState',101)
	
def datafetch_switch_rest(client, userdata, msg):
	print("Switch Status received post switch position change")
	payload=json.loads(msg.payload.decode())
	datagrab(payload,'switchState',103)
	
def agg_alive(client, userdata, msg,):
	print("Alive beacon received")
	payload=json.loads(msg.payload.decode())
	datagrab(payload,'alive',102)

def on_log(client, userdata, level, buf):
	print("log:",buf)	
	conn1 =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
	cur1=conn1.cursor()
	cur1.execute("INSERT INTO mqttLog(log) VALUES(%s);",buf)
	conn1.commit()
	conn1.close()

mqttclient.on_log=on_log # set client logging	
#Subscribed Topics 
mqttclient.message_callback_add("SGM/test", test)
mqttclient.message_callback_add("SGM/datafetch_dimis_gm1_direct", datafetch_dimis_gm1_direct)
mqttclient.message_callback_add("SGM/datafetch_dimis_gm1", datafetch_dimis_gm1)
mqttclient.message_callback_add("SGM/datafetch_dimis_lm1", datafetch_dimis_lm1)
mqttclient.message_callback_add("SGM/datafetch_dimis_lm2", datafetch_dimis_lm2)
mqttclient.message_callback_add("SGM/datafetch_maxim", datafetch_maxim)
mqttclient.message_callback_add("SGM/datafetch_sch", datafetch_sch)
mqttclient.message_callback_add("SGM/datafetch_outback_inv", datafetch_outback_inv)
mqttclient.message_callback_add("SGM/datafetch_outback_cc", datafetch_outback_cc)
mqttclient.message_callback_add("SGM/datafetch_navsemi", datafetch_navsemi)
mqttclient.message_callback_add("SGM/datafetch_gsm", datafetch_gsm)
mqttclient.message_callback_add("SGM/datafetch_events", datafetch_events)
mqttclient.message_callback_add("SGM/node_alive", node_alive)
mqttclient.message_callback_add("SGM/datafetch_switch", datafetch_switch)
mqttclient.message_callback_add("SGM/agg_alive", agg_alive)
mqttclient.message_callback_add("SGM/datafetch_switch_rest",datafetch_switch_rest)


mqttclient.loop_forever()

