#!/usr/bin/python3
import sys
import os
import paho.mqtt.client as paho
import json,grabrest,pymysql
import ast
from datetime import datetime



global mqttclient;
global broker;
global port;

# Establish a connection to the MySQL database
conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()

# Set up MQTT broker information
broker = "0.0.0.0";
port = 1883;

# Get the process ID and create a unique MQTT client ID
mypid = os.getpid()
print("Process started at: " +str(mypid))
client_uniq = "pubclient_"+str(mypid)
mqttclient = paho.Client(client_uniq, True) #nocleanstart

# Define callback function for the "test" MQTT topic
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

# Define callback function for the "datafetch_dimis_gm1_direct" MQTT topic
def datafetch_dimis_gm1_direct(client, userdata, msg):
	print("Direct MQTT Message received - Dimis GM1")
	payload=json.loads(msg.payload.decode())
	#print(payload)
	grabrest.todb(payload,1)

# Define callback function for the "datafetch_dimis_lm1_direct" MQTT topic
def datafetch_dimis_lm1_direct(client, userdata, msg):
	print("Direct MQTT Message received - Dimis LM")
	payload=json.loads(msg.payload.decode())
	grabrest.todb(payload,1)
	#print(payload)

# Define callback function for the "datafetch_dimis_lm2_direct" MQTT topic
def datafetch_dimis_lm2_direct(client, userdata, msg):
	print("Direct MQTT Message received - Dimis GM2")
	payload=json.loads(msg.payload.decode())
	grabrest.todb(payload,1)
	#print(payload)

# Define callback function for the "datafetch_maxim_direct" MQTT topic
def datafetch_maxim_direct(client, userdata, msg):
	print("Maxim Data received")
	payload=json.loads(msg.payload.decode())
	grabrest.todb(payload,2)

# Define callback function for the "datafetch_sch_direct" MQTT topic
def datafetch_sch_direct(client, userdata, msg):
	print("Schneider Data received")
	payload=json.loads(msg.payload.decode())
	grabrest.todb(payload,3)
	
# Define callback function for the "datafetch_stp_direct" MQTT topic
def datafetch_stp_direct(client, userdata, msg):
	print("Schneider Data received")
	payload=json.loads(msg.payload.decode())
	grabrest.todb(payload,4)
	
	
# Define callback function for the "datafetch_outback_inv_direct" MQTT topic
def datafetch_outback_inv_direct(client, userdata, msg):
	print("Outback Data received")
	payload=json.loads(msg.payload.decode())
	#print(payload)
	grabrest.todb(payload,41)

# Define callback function for the "datafetch_outback_cc_direct" MQTT topic
def datafetch_outback_cc_direct(client, userdata, msg):
	print("Outback Data received")
	payload=json.loads(msg.payload.decode())
	#print(payload)
	grabrest.todb(payload,42)

# Define callback function for the "datafetch_navsemi_direct" MQTT topic
def datafetch_navsemi_direct(client, userdata, msg):
	print("Navsemi Data received")
	payload=json.loads(msg.payload.decode())
	grabrest.todb(payload,5)

# Define callback function for the "datafetch_events_direct" MQTT topic
def datafetch_events_direct(client, userdata, msg):
	print("Event Data received")
	payload=json.loads(msg.payload.decode())
	grabrest.todb(payload,0) 

# Define callback function for the "node_alive_direct" MQTT topic
def node_alive_direct(client, userdata, msg):
	print("Alive beacon received")
	payload=json.loads(msg.payload.decode())
	#print(payload)
	grabrest.todb(payload,100)
	
# Define callback function for the "datafetch_switch_direct" MQTT topic
def datafetch_switch_direct(client, userdata, msg):
	print("Direct MQTT Message received - Switch")
	payload=json.loads(msg.payload.decode())
	#print(payload)
	grabrest.todb(payload,101)

# Define callback function for the "agg_alive_direct" MQTT topic
def agg_alive_direct(client, userdata, msg,):
	print("Direct Alive beacon received from AGG")
	payload=json.loads(msg.payload.decode())
	#print(msg)
	#print(payload)
	grabrest.todb(payload,102)
	
# Define callback function for the "temperature" MQTT topic
def temperature(client, userdata, msg,):
	print("Temperature data recieved")
	payload=json.loads(msg.payload.decode())
	#print(msg)
	print(payload)
	grabrest.todb(payload,5)
	
# Define callback function for the "powerstate" MQTT topic
def powerstate(client, userdata, msg,):
	conn1 =pymysql.connect(database="powerstatus",user="admin",password="admin",host="localhost")
	cur1=conn1.cursor()
	payload=json.loads(msg.payload.decode())
	cur1.execute("INSERT INTO measureData(deviceId,temperature,humidity,state) VALUES(%(deviceId)s,%(temperature)s,%(humidity)s,%(state)s);",payload)
	conn1.commit()
	conn1.close()

# Define callback function for the "wiman" MQTT topic
def wiman(client, userdata, msg,):
	conn1 =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
	cur1=conn1.cursor()
	print(msg.payload)
	payload=msg.payload.decode()
	
	
	
	payload2= payload.replace("\'", "\"")
	payload2=payload2.replace("\r\n"," ")
	payload2=payload2.replace("AV_TS2,"," ")
 	
	payload3 = json.loads(payload2)
	print("Wiman Data")
# 	print(data)	
	data = payload3['data']
	try:
	
		io = data["io"]
		sysv = data["dev"]
		sqdata = {"deviceID":1,"imei":data["imei"],"uid":data["uid"],"dtm":data["dtm"],"seq":data["seq"],"sig":data["sig"],"di1":io["di1"],"di2":io["di2"],"op1":io["op1"],"a1":io["a1"],"a2":io["a2"],"s1":io["s1"],"p1":io["p1"],"sysv":sysv["sysv"]}
		print(sqdata)
	
		cur1.execute("INSERT INTO `wiman` (`deviceID`, `imei`, `uid`, `dtm`, `seq`, `sig`, `di1`, `di2`, `op1`, `a1`, `a2`, `s1`, `p1`, `sysv`) VALUES(%(deviceID)s, %(imei)s, %(uid)s, %(dtm)s, %(seq)s, %(sig)s, %(di1)s, %(di2)s, %(op1)s, %(a1)s, %(a2)s, %(s1)s, %(p1)s, %(sysv)s);",sqdata)
		
	except:
		print("data format error")
		print(payload)
		pass
	cur1.execute("INSERT INTO wimanRaw (data) VALUES (%s);",payload)
	# 	cur1.execute("INSERT INTO piggyback(TIME,boat,dir,ping_ms,ss,nf,rssi,pos,ccq,d,txrate,rxrate,freq,channel,bs_ip) VALUES(%(TIME)s,%(boat,%(dir)s,%(ping_ms)s,%(ss)s,%(nf)s,%(rssi)s,%(pos)s,%(ccq)s,%(d)s,%(txrate)s,%(rxrate)s,%(freq)s,%(channel)s,%(bs_ip)s);",payload)
	conn1.commit()
	conn1.close()
	
# Define callback function for the "faclon" MQTT topic
def faclon(client, userdata, msg,):
	conn1 =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
	cur1=conn1.cursor()
	payload=msg.payload.decode()
	print("Faclon Data")
	
	
	payload2= payload.replace("\'", "\"")
	payload2=payload2.replace("\r\n"," ")
	payload2=payload2.replace("AV_TS1,"," ")
 	
	
# 	print(data)
	try:
		payload3 = json.loads(payload2)
		data = payload3['data']
		io = data["io"]
		sysv = data["dev"]
		sqdata = {"deviceID":1,"imei":data["imei"],"uid":data["uid"],"dtm":data["dtm"],"seq":data["seq"],"sig":data["sig"],"di1":io["di1"],"di2":io["di2"],"op1":io["op1"],"a1":io["a1"],"a2":io["a2"],"s1":io["s1"],"p1":io["p1"],"sysv":sysv["sysv"]}
		print(sqdata)
		cur1.execute("INSERT INTO `faclon` (`deviceID`, `imei`, `uid`, `dtm`, `seq`, `sig`, `di1`, `di2`, `op1`, `a1`, `a2`, `s1`, `p1`, `sysv`) VALUES(%(deviceID)s, %(imei)s, %(uid)s, %(dtm)s, %(seq)s, %(sig)s, %(di1)s, %(di2)s, %(op1)s, %(a1)s, %(a2)s, %(s1)s, %(p1)s, %(sysv)s);",sqdata)
		
	except:
		print("data format error")
		print(payload)
		pass
	
	cur1.execute("INSERT INTO faclonRaw (data) VALUES (%s);",payload)
# 	cur1.execute("INSERT INTO piggyback(TIME,boat,dir,ping_ms,ss,nf,rssi,pos,ccq,d,txrate,rxrate,freq,channel,bs_ip) VALUES(%(TIME)s,%(boat,%(dir)s,%(ping_ms)s,%(ss)s,%(nf)s,%(rssi)s,%(pos)s,%(ccq)s,%(d)s,%(txrate)s,%(rxrate)s,%(freq)s,%(channel)s,%(bs_ip)s);",payload)
	conn1.commit()
	conn1.close()

# Define callback function for the "trb" MQTT topic
def trb(client, userdata, msg,):
	conn1 =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
	cur1=conn1.cursor()
# 	print(msg.payload.decode())
	payload=ast.literal_eval(msg.payload.decode())[0]
	print("TRB Data")
	readTime = datetime.utcfromtimestamp(int(payload["readTime"])).strftime('%Y-%m-%d %H:%M:%S')
	data = int(payload["data"])/1000
	payload["data"] = data
	payload["readTime"] = readTime
	print(payload["DevID"] + " Data Received")
	print(payload)
	
	cur1.execute("INSERT INTO trbdata(readTime, DevID, registerAddress,data) VALUES(%(readTime)s, %(DevID)s, %(registerAddress)s,%(data)s);",payload)
	conn1.commit()
	conn1.close()
	print("DB Dump Success")
	
# Define callback function for the "embedos" MQTT topic
def embedos(client, userdata, msg,):
	conn1 =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
	cur1=conn1.cursor()
# 	print(msg.payload.decode())
	payload=msg.payload.decode()
	print("embedos Data")
	print(payload)	
	
	cur1.execute("INSERT INTO embedosRaw(data) VALUES(%s);",payload)
	payload=json.loads(payload)
	analogDataChannel1 = payload["analogDataChannel1"]
	analogDataChannel2 = payload["analogDataChannel2"]
	analogDataChannel3 = payload["analogDataChannel3"]
	analogDataChannel4 = payload["analogDataChannel4"]
	DigitalInput = payload["DigitalInput"]
	DigitalOutput = payload["DigitalOutput"]

	data = {"deviceId":payload["deviceId"],"deviceTypeId":payload["deviceTypeId"],"analogDataChannel1value":analogDataChannel1["value"],"analogDataChannel1status":analogDataChannel1["status"],"analogDataChannel2value":analogDataChannel2["value"],"analogDataChannel2status":analogDataChannel2["status"],"analogDataChannel3value":analogDataChannel3["value"],"analogDataChannel3status":analogDataChannel3["status"],"analogDataChannel4value":analogDataChannel4["value"],"analogDataChannel4status":analogDataChannel4["status"],"DigitalInputvalue":DigitalInput["value"],"DigitalInputstatus":DigitalInput["status"],"DigitalOutputvalue":DigitalOutput["value"],"DigitalOutputstatus":DigitalOutput["status"]}
	print(data)
	
	cur1.execute("INSERT INTO `embedos` (`deviceId`, `deviceTypeId`, `analogDataChannel1value`, `analogDataChannel1status`, `analogDataChannel2value`, `analogDataChannel2status`, `analogDataChannel3value`, `analogDataChannel3status`, `analogDataChannel4value`, `analogDataChannel4status`, `DigitalInputvalue`, `DigitalInputstatus`, `DigitalOutputvalue`, `DigitalOutputstatus`) VALUES (%(deviceId)s, %(deviceTypeId)s, %(analogDataChannel1value)s, %(analogDataChannel1status)s, %(analogDataChannel2value)s, %(analogDataChannel2status)s, %(analogDataChannel3value)s, %(analogDataChannel3status)s, %(analogDataChannel4value)s, %(analogDataChannel4status)s, %(DigitalInputvalue)s, %(DigitalInputstatus)s, %(DigitalOutputvalue)s, %(DigitalOutputstatus)s);",data)
	conn1.commit()
	conn1.close()
	print("DB Dump Success")

# Define callback function for the "vvmgateway" MQTT topic
def vvmgateway(client, userdata, msg,):
	conn1 =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
	cur1=conn1.cursor()
	payload=msg.payload.decode()
	payload=json.loads(payload)
	print("VVM Data")
	print(payload)
	cur1.execute("INSERT INTO `VVMGateway` (`devID`, `G`, `timestamp`, `BTV`, `PVV`, `PVI`, `mA`) VALUES (%(devID)s, %(G)s, %(timestamp)s, %(BTV)s, %(PVV)s, %(PVI)s, %(4-20)s);",payload)
	conn1.commit()
	conn1.close()
	print("DB Dump Success")

# Callback function for MQTT logging
def on_log(client, userdata, level, buf):
	conn1 =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
	cur1=conn1.cursor()
	cur1.execute("INSERT INTO mqttLog(log) VALUES(%s);",buf)
	conn1.commit()
	conn1.close()

	
def _on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	 
#Subscribed Topics 
def _on_connect(mqttclient, userdata, flags, rc):
	mqttclient.subscribe("SGM/#", qos=0)	
	
# Set up callback functions for MQTT client
mqttclient.message_callback_add("SGM/test", test)

# Callbacks for other MQTT topics
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
mqttclient.message_callback_add("SGM/powerstate", powerstate)

# Callbacks for 4Ward devices
mqttclient.message_callback_add("SGM/wiman", wiman)
mqttclient.message_callback_add("SGM/faclon", faclon)
mqttclient.message_callback_add("SGM/trb", trb)
mqttclient.message_callback_add("SGM/embedos", embedos)
mqttclient.message_callback_add("SGM/vvm", vvmgateway)

# Connect to the MQTT broker and start the MQTT client loop
mqttclient.connect(broker, port, keepalive=1, bind_address="")
mqttclient.on_log=on_log # set client logging	
mqttclient.on_connect = _on_connect      
mqttclient.loop_forever()



