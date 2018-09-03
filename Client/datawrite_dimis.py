#!/usr/bin/python

import socket,mqttservice
import time,json
from datetime import datetime
import pymysql
from subprocess import check_output

scanoutput=check_output(["hostname -I"],shell=1)
ip_eth0=scanoutput.decode().split()[0]
ip_wlan0=scanoutput.decode().split()[1]
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
			print('received %s' % val)
			time.sleep(0.5)
			if count == 0:
				print('if')
				connection.sendall(
					('{"opt":"RC","GTW":{"protV":"Core-1A_Energy-1A","PN":"DA01-0021","SN":"170092"},timestamp":'+ str(round(time.time() * 1000)) + '}').encode())
			else:
				print('else') 
				connection.sendall(
					('{"opt":"W","GTW":{"protV":"Core-1A_Energy-1A","PN":"DA01-0021","SN":"170084"},"devs":[{"PN": "DA01-0021","SN": "170084","dataID":[38,39,40,41,42,43,44,45],"data":[1,1,0,0,1,0,0,0]]},"timestamp":'+ str(round(time.time() * 1000)) + '}').encode())
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
