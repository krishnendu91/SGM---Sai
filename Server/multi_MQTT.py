#!/usr/bin/python3
import sys
import os
import paho.mqtt.client as paho
import json,grabrest,pymysql

global mqttclient;
global broker;
global port;
conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()
broker = "172.20.0.16";
port = 1883;
mypid = os.getpid()
print("Process started at: " +str(mypid))
client_uniq = "pubclient_"+str(mypid)
mqttclient = paho.Client(client_uniq, False) #nocleanstart
mqttclient.connect(broker, port, 0)
mqttclient.subscribe("SGM/#")

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
	print("Direct MQTT Message received - Dimis GM1")
	payload=json.loads(msg.payload.decode())
	#print(payload)
	grabrest.todb(payload,1)

def datafetch_dimis_lm1_direct(client, userdata, msg):
	print("Direct MQTT Message received - Dimis LM")
	payload=json.loads(msg.payload.decode())
	grabrest.todb(payload,1)
	#print(payload)

def datafetch_dimis_lm2_direct(client, userdata, msg):
	print("Direct MQTT Message received - Dimis GM2")
	payload=json.loads(msg.payload.decode())
	grabrest.todb(payload,1)
	#print(payload)

def datafetch_maxim_direct(client, userdata, msg):
	print("Maxim Data received")
	payload=json.loads(msg.payload.decode())
	grabrest.todb(payload,2)

def datafetch_sch_direct(client, userdata, msg):
	print("Schneider Data received")
	payload=json.loads(msg.payload.decode())
	grabrest.todb(payload,3)
	
def datafetch_stp_direct(client, userdata, msg):
	print("Schneider Data received")
	payload=json.loads(msg.payload.decode())
	grabrest.todb(payload,4)
	
	
def datafetch_outback_inv_direct(client, userdata, msg):
	print("Outback Data received")
	payload=json.loads(msg.payload.decode())
	#print(payload)
	grabrest.todb(payload,41)

def datafetch_outback_cc_direct(client, userdata, msg):
	print("Outback Data received")
	payload=json.loads(msg.payload.decode())
	#print(payload)
	grabrest.todb(payload,42)

def datafetch_navsemi_direct(client, userdata, msg):
	print("Navsemi Data received")
	payload=json.loads(msg.payload.decode())
	grabrest.todb(payload,5)

def datafetch_gsm_direct(client, userdata, msg):
	print("GSM Data received")
	#TBD

def datafetch_events_direct(client, userdata, msg):
	print("Event Data received")
	payload=json.loads(msg.payload.decode())
	grabrest.todb(payload,0) 

def node_alive_direct(client, userdata, msg):
	print("Alive beacon received")
	payload=json.loads(msg.payload.decode())
	#print(payload)
	grabrest.todb(payload,100)
	
def datafetch_switch_direct(client, userdata, msg):
	print("Direct MQTT Message received - Switch")
	payload=json.loads(msg.payload.decode())
	#print(payload)
	grabrest.todb(payload,101)

def agg_alive_direct(client, userdata, msg,):
	print("Direct Alive beacon received from AGG")
	payload=json.loads(msg.payload.decode())
	#print(msg)
	#print(payload)
	grabrest.todb(payload,102)
	
def temperature(client, userdata, msg,):
	print("Temperature data recieved")
	payload=json.loads(msg.payload.decode())
	#print(msg)
	print(payload)
	grabrest.todb(payload,5)


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
mqttclient.message_callback_add("SGM/datafetch_dimis_lm1_direct", datafetch_dimis_lm1_direct)
mqttclient.message_callback_add("SGM/datafetch_dimis_lm2_direct", datafetch_dimis_lm2_direct)
mqttclient.message_callback_add("SGM/datafetch_maxim_direct", datafetch_maxim_direct)
mqttclient.message_callback_add("SGM/datafetch_sch_direct", datafetch_sch_direct)
mqttclient.message_callback_add("SGM/datafetch_outback_inv_direct", datafetch_outback_inv_direct)
mqttclient.message_callback_add("SGM/datafetch_outback_cc_direct", datafetch_outback_cc_direct)
mqttclient.message_callback_add("SGM/datafetch_navsemi_direct", datafetch_navsemi_direct)
mqttclient.message_callback_add("SGM/datafetch_gsm_direct", datafetch_gsm_direct)
mqttclient.message_callback_add("SGM/datafetch_events_direct", datafetch_events_direct)
mqttclient.message_callback_add("SGM/node_alive_direct", node_alive_direct)
mqttclient.message_callback_add("SGM/datafetch_switch_direct", datafetch_switch_direct)
mqttclient.message_callback_add("SGM/agg_alive_direct", agg_alive_direct)
mqttclient.message_callback_add("SGM/datafetch_stp_direct", datafetch_stp_direct)
mqttclient.message_callback_add("SGM/temperature", temperature)


#mqttclient.message_callback_add("SGM/datafetch_switch_rest",datafetch_switch_rest_direct)

mqttclient.loop_forever()

