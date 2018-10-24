#!/usr/bin/python

# Version 1.0a
#Real time data collection from Evoleo Dimis Energy Meter
import sys
import socket,mqttservice
import time,json
from datetime import datetime
import pymysql
from subprocess import check_output
import utils

#get IP addresses & Node ID
ip_eth0,ip_wlan0,id_node=utils.sysinfo()
print ("Starting Data fetch for Node"+str(id_node)+"connected at eth0" +str(ip_eth0) + "and WLan0" + str(ip_wlan0))
#get Port nos
#port= int(sys.argv[1])
port_GM=10001
port_LM1=10002
port_LM2=10003
port_LM3=10004

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the server port
server_address = (ip_eth0, port_GM)
print('Starting up on %s port %s' % server_address)
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
	print('Starting up on %s port %s' % server_address)
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
value_GM1=utils.dimisdecode(val[0])
print (value_GM1)

#DB Dump
utils.todbdimis(value_GM1)

utils.switchstatus()
#Data trasfer to CS Service
mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch","DONE",ip_wlan0)
print("MQTT Success")
