import sys
import socket
import time,json
from datetime import datetime
import pymysql
from subprocess import check_output
import paho.mqtt.client as mqtt

def mqtt_publish(topic,payload):
	payload=json.dumps(payload)
	topic="SGM/"+topic
	client = mqtt.Client()
	client.connect('192.168.112.110',1883,60)
	(rc,mid)=client.publish(topic,payload);
	client.disconnect();
	return rc

def sysinfo():
  ip_scanoutput=check_output(["hostname -I"],shell=1)
  ip_eth0=ip_scanoutput.decode().split()[0]
  id_scanoutput=check_output(["hostname"],shell=1)
  id_node=id_scanoutput.decode().split()[0]
  nodeId=id_node[-4:]
  return(ip_eth0,nodeId)

def todbsch(schData):
  conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
  cur=conn.cursor()
  cur.execute("INSERT INTO schData (nodeId,meterId,A, A1, A2, A3, VLL, VLN, V1, V2, V3, V12, V23, V31, F, PF, PF1, PF2, PF3, W, W1, W2, W3, VA, VA1, VA2, VA3, WH, VAH, INTR) VALUES (%(nodeId)s,%(meterId)s ,%(A)s, %(A1)s, %(A2)s, %(A3)s, %(VLL)s, %(VLN)s, %(V1)s, %(V2)s, %(V3)s, %(V12)s, %(V23)s, %(V31)s, %(F)s, %(PF)s, %(PF1)s, %(PF2)s, %(PF3)s, %(W)s, %(W1)s, %(W2)s, %(W3)s, %(VA)s, %(VA1)s, %(VA2)s, %(VA3)s, %(WH)s, %(VAH)s, %(INTR)s);",schData)
  conn.commit()
  conn.close()
  print ("Schneider Meter - DB Dump success")
  return "Completed"
