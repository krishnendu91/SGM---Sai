#!/usr/bin/python

# Version 1.0a
#Real time data collection from Evoleo Dimis Energy Meter
import sys
import socket,mqttservice
import time,json
from datetime import datetime
import pymysql
from subprocess import check_output

ip_scanoutput=check_output(["hostname -I"],shell=1)
ip_eth0=ip_scanoutput.decode().split()[0]
ip_wlan0=ip_scanoutput.decode().split()[1]

id_scanoutput=check_output(["hostname"],shell=1)
id_node=id_scanoutput.decode().split()[0]
if len(id_node)<10:
	nodeId=id_node[-2:]
else
	nodeId=id_node[-1:]
print(nodeId)

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
#print val[0]
json_val=json.loads(val[0])
 
data=json_val['devs'][-1]['data']
#Voltage
v1=data[0]
v2=data[1]
v3=data[2]

#Current
i1=data[3]
i2=data[4]
i3=data[5]

#Power
#Active Power
w1=data[6]
w2=data[7]
w3=data[8]

#Apparent Power
va1=data[9]
va2=data[10]
va3=data[11]

#Reactive Power
var1=data[12]
var2=data[13]
var3=data[14]

#Power Factor
pf1=data[15]
pf2=data[16]
pf3=data[17]

#Frequency
f1=data[18]
f2=data[19]
f3=data[20]

#Total Consumed Active Energy

wh=data[24]
vah=data[25]
varh=data[26]

#Active Energy
wh1=data[27]
wh2=data[30]
wh3=data[33]

#Apparent Energy
vah1=data[28]
vah2=data[31]
vah3=data[34]

#Reactive Energy
varh1=data[29]
varh2=data[32]
varh3=data[35]

#Digital Outputs

D1=data[37]
D2=data[38]
D3=data[39]
D4=data[40]
D5=data[41]
D6=data[42]
D7=data[43]
D8=data[44]
timestamp=datetime.now().strftime('%d-%m-%Y %H:%M:%S')
#value={'nodeid':1,'time':timestamp,'v':{'v1':v1,'v2':v2,'v3':v3},'i':{'i1':i1,'i2':i2,'i3':i3},'power':{'active':{'w1':w1,'w2':w2,'w3':w3},'reactive':{'var1':var1,'var2':var2,'var3':var3},'apparent':{'va1':va1,'va2':va2,'va3':va3}},'pf':{'pf1':pf1,'pf2':pf2,'pf3':pf3},'f':{'f1':f1,'f2':f2,'f3':f3},'energy':{'total':{'wh':wh,'vah':vah,'varh':varh},'active':{'wh1':wh1,'wh2':wh2,'wh3':wh3},'reactive':{'varh1':varh1,'varh2':varh2,'varh3':varh3},'apparent':{'vah1':vah1,'vah2':vah2,'vah3':vah3}},'switch':{'D1':D1,'D2':D2,'D3':D3,'D4':D4,'D5':D5,'D6':D6,'D7':D7,'D8':D8}}
value_GM1={'nodeid':1,'meterType':1,'time':timestamp,'v1':v1,'v2':v2,'v3':v3,'i1':i1,'i2':i2,'i3':i3,'w1':w1,'w2':w2,'w3':w3,'var1':var1,'var2':var2,'var3':var3,'va1':va1,'va2':va2,'va3':va3,'pf1':pf1,'pf2':pf2,'pf3':pf3,'f1':f1,'f2':f2,'f3':f3,'wh':wh,'vah':vah,'varh':varh,'wh1':wh1,'wh2':wh2,'wh3':wh3,'varh1':varh1,'varh2':varh2,'varh3':varh3,'vah1':vah1,'vah2':vah2,'vah3':vah3,'D1':D1,'D2':D2,'D3':D3,'D4':D4,'D5':D5,'D6':D6,'D7':D7,'D8':D8}
print (value_GM1)
conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()
cur.execute("INSERT INTO nodeData(nodeid,meterType, v1, v2, v3, i1, i2, i3, w1,w2,w3,va1,va2,va3,var1,var2,var3,wh,vah,varh,wh1,wh2,wh3,vah1,vah2,vah3,varh1,varh2,varh3,pf1,pf2,pf3,f1,f2,f3,d1,d2,d3,d4,d5,d6,d7,d8) VALUES(%(nodeid)s,%(meterType)s,%(v1)s,%(v2)s,%(v3)s,%(i1)s,%(i2)s,%(i3)s,%(w1)s,%(w2)s,%(w3)s,%(va1)s,%(va2)s,%(va3)s,%(var1)s,%(var2)s,%(var3)s,%(wh)s,%(vah)s,%(varh)s,%(wh1)s,%(wh2)s,%(wh3)s,%(vah1)s,%(vah2)s,%(vah3)s,%(varh1)s,%(varh2)s,%(varh3)s,%(pf1)s,%(pf2)s,%(pf3)s,%(f1)s,%(f2)s,%(f3)s,%(D1)s,%(D2)s,%(D3)s,%(D4)s,%(D5)s,%(D6)s,%(D7)s,%(D8)s);",value_GM1)
conn.commit()
conn.close()
print ("DB Dump success")
#value=json.dumps(value)
mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch","DONE",ip_wlan0)
print("MQTT Success")


