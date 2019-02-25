#!/usr/bin/python

# Version 1.0a
#Real time data collection from Evoleo Dimis Energy Meter
import sys
import socket,mqttservice,algorithm
import time,json
from datetime import datetime
import pymysql
from subprocess import check_output
import utils

#get IP addresses & Node ID
ip_eth0,ip_wlan0,id_node=utils.sysinfo()
print ("Starting Data fetch for Node "+str(id_node) +" connected at eth0 " +str(ip_eth0) + " and WLan0 " + str(ip_wlan0))
#get Port nos
#port= int(sys.argv[1])
port_GM=10001
port_LM1=10002
port_GM2=10003
port_LM3=10004

#Get Meter ID with respect to the node
#meterId_GM1=utils.getmeterid(id_node,'GM1')
#meterId_GM2=utils.getmeterid(id_node,'GM2')
#meterId_LM=utils.getmeterid(id_node,'LM')

# Create a TCP/IP socket
def dimishelper(ip, port):
	if port==10001:
		meterType=1
		try:
			meterId=utils.getmeterid(id_node,'GM1')
		except:
			pass
	elif port==10002:
		meterType=2
		try:
			meterId=utils.getmeterid(id_node,'LM')
		except:
			pass
	elif port==10003:
		meterType=3
		try:
			meterId=utils.getmeterid(id_node,'GM2')
		except:
			pass
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	print('Dimis polling begins for ' +str(port))
# Bind the socket to the server port
	server_address = (ip, port)
#	print('Starting up on %s port %s' % server_address)
	sock.bind(server_address)

# Listen for incoming connections
	sock.listen(1)
	a=1
	b=1
	while a:
	# Wait for a connection
		print('waiting for a connection')
		connection, client_address = sock.accept()
		count = 0
		#print('Starting up on %s port %s' % server_address)
		data = bytearray()
		while b:
		# Receive the data in small chunks
			data += connection.recv(16)
			if '\r\n' in data.decode():
			# when a full message is received
				val = data.decode().split('\r\n')
#			print('received %s' % val
				time.sleep(0.5)
				if count == 0:
					connection.sendall(
						('{"opt":"RC","GTW":{"protV":"Core-1A_Energy-1A","PN":"DA01-0021","SN":"170092"},timestamp":'+ str(round(time.time() * 1000)) + '}').encode())
				else:
				
					connection.sendall(
						('{"opt":"R","GTW":{"protV":"Core-1A_Energy-1A","PN":"DA01-0021","SN":"170092"},"timestamp":'+ str(round(time.time() * 1000)) + '}').encode())
				count += 1
				if len(val[1]) > 0:
					data = val[1].encode()
				else:
					data = bytearray()
					time.sleep(0.5)
				if count >2:
					b=0
		a=0
	# Clean up the connection
	connection.close()

	#decode dimis to match ASGM format
	value=utils.dimisdecode(val[0],meterType,meterId)
	return value
#Read from GM1
#print (id_node)
#if(1<id_node <9   | 9<id_node <12 | id_node ==13):

if(1<id_node <7 or id_node ==8 or id_node ==13 or 9<id_node <12): # For Node 2,3,4,5,6,8,10,11, 13
	#fetch GM
	value_GM=dimishelper(ip_eth0,port_GM)
	mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_dimis_gm1_direct",value_GM,ip_wlan0)
	utils.todbdimis(value_GM)
	
	#algorithm.poweroutage(value_GM['v1'],value_GM['v2'],value_GM['v3'],value_GM['meterType'],id_node,ip_wlan0)
	#algorithm.frequency(value_GM['v1'],value_GM['v2'],value_GM['v3'],value_GM['meterType'],id_node,ip_wlan0)
	#algorithm.powerquality(value_GM['v1'],value_GM['v2'],value_GM['v3'],value_GM['meterType'],id_node,ip_wlan0)
	#algorithm.current(value_GM['i1'],value_GM['i2'],value_GM['i3'],value_GM['meterType'],id_node,ip_wlan0)
	print("GM1 Fetch Complete")
	
	#Fetch LM1
	value_LM1=dimishelper(ip_eth0,port_LM1)
	utils.todbdimis(value_LM1)
	mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_dimis_lm1_direct",value_LM1,ip_wlan0)
	#algorithm.poweroutage(value_LM1['v1'],value_LM1['v2'],value_LM1['v3'],value_LM1['meterType'],id_node,ip_wlan0)
	#algorithm.frequency(value_LM1['v1'],value_LM1['v2'],value_LM1['v3'],value_LM1['meterType'],id_node,ip_wlan0)
	#algorithm.powerquality(value_LM1['v1'],value_LM1['v2'],value_LM1['v3'],value_LM1['meterType'],id_node,ip_wlan0)
	#algorithm.current(value_LM1['i1'],value_LM1['i2'],value_LM1['i3'],value_LM1['meterType'],id_node,ip_wlan0)
	#mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_dimis_gm1","DONE",ip_wlan0)
	#mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_dimis_lm1","DONE",ip_wlan0)
	print("LM1 Fetch Complete")

elif (id_node == 7 or id_node == 9 or id_node == 12): #For node 7, 9, 12
	#Fetch GM
	value_GM=dimishelper(ip_eth0,port_GM)
	mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_dimis_gm1_direct",value_GM,ip_wlan0)
	utils.todbdimis(value_GM)
	
	#algorithm.poweroutage(value_GM['v1'],value_GM['v2'],value_GM['v3'],value_GM['meterType'],id_node,ip_wlan0)
	#algorithm.frequency(value_GM['v1'],value_GM['v2'],value_GM['v3'],value_GM['meterType'],id_node,ip_wlan0)
	#algorithm.powerquality(value_GM['v1'],value_GM['v2'],value_GM['v3'],value_GM['meterType'],id_node,ip_wlan0)
	#algorithm.current(value_GM['i1'],value_GM['i2'],value_GM['i3'],value_GM['meterType'],id_node,ip_wlan0)
	print("GM1 Fetch Complete")
	
	#Fetch LM1
	value_LM1=dimishelper(ip_eth0,port_LM1)
	utils.todbdimis(value_LM1)
	mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_dimis_gm1_direct",value_LM1,ip_wlan0)

	#algorithm.poweroutage(value_LM1['v1'],value_LM1['v2'],value_LM1['v3'],value_LM1['meterType'],id_node,ip_wlan0)
	#algorithm.frequency(value_LM1['v1'],value_LM1['v2'],value_LM1['v3'],value_LM1['meterType'],id_node,ip_wlan0)
	#algorithm.powerquality(value_LM1['v1'],value_LM1['v2'],value_LM1['v3'],value_LM1['meterType'],id_node,ip_wlan0)
	#algorithm.current(value_LM1['i1'],value_LM1['i2'],value_LM1['i3'],value_LM1['meterType'],id_node,ip_wlan0)
	print("LM1 Fetch Complete")
	#mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_dimis_gm1","DONE",ip_wlan0)
	#mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_dimis_lm1","DONE",ip_wlan0)
	#Fetch GM2
	value_GM2=dimishelper(ip_eth0,port_GM2)
	utils.todbdimis(value_GM2)
	mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_dimis_lm2_direct",value_GM2,ip_wlan0)
	#algorithm.poweroutage(value_GM2['v1'],value_GM2['v2'],value_GM2['v3'],value_GM2['meterType'],id_node,ip_wlan0)
	#algorithm.frequency(value_GM2['v1'],value_GM2['v2'],value_GM2['v3'],value_GM2['meterType'],id_node,ip_wlan0)
	#algorithm.powerquality(value_GM2['v1'],value_GM2['v2'],value_GM2['v3'],value_GM2['meterType'],id_node,ip_wlan0)
	#algorithm.current(value_GM2['i1'],value_GM2['i2'],value_GM2['i3'],value_GM2['meterType'],id_node,ip_wlan0)
	print("GM2 Fetch Complete")
	
elif (id_node == 1):#for source node
	#Fetch GM
	value_GM=dimishelper(ip_eth0,port_GM)
	mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_dimis_gm1_direct",value_GM,ip_wlan0)
	utils.todbdimis(value_GM)
	#mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_dimis_gm1","DONE",ip_wlan0)
	#algorithm.poweroutage(value_GM['v1'],value_GM['v2'],value_GM['v3'],value_GM['meterType'],id_node,ip_wlan0)
	#algorithm.frequency(value_GM['v1'],value_GM['v2'],value_GM['v3'],value_GM['meterType'],id_node,ip_wlan0)
	#algorithm.powerquality(value_GM['v1'],value_GM['v2'],value_GM['v3'],value_GM['meterType'],id_node,ip_wlan0)
	#algorithm.current(value_GM['i1'],value_GM['i2'],value_GM['i3'],value_GM['meterType'],id_node,ip_wlan0)
	print("GM1 Fetch Complete")

switch=utils.switchstatus()
#mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_switch","DONE",ip_wlan0)
mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_switch_direct",switch,ip_wlan0)
print("MQTT Success")
