#!/usr/bin/python

import pymysql,sys,subprocess
from subprocess import check_output

#get IP addresses
ip_scanoutput=check_output(["hostname -I"],shell=1)
ip_eth0=ip_scanoutput.decode().split()[0]
ip_wlan0=ip_scanoutput.decode().split()[1]

temp=subprocess.check_output(["vcgencmd","measure_temp"])
temp=temp.decode()
temp=temp.replace("temp=","")
temp=temp.replace("'C\n","")

		
#get node ID
id_scanoutput=check_output(["hostname"],shell=1)
id_node=id_scanoutput.decode().split()[0]
if len(id_node)>9:
	nodeId=int(id_node[-2:])
else:
	nodeId=int(id_node[-1:])

#Store to DB
dataHealth={'nodeid':nodeId,'alive':1,'temp':temp}
conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()
cur.execute("INSERT INTO nodeHealth(nodeid,alive,temp) VALUES(%(nodeid)s,%(alive)s,%(temp)s);",dataHealth)
conn.commit()
conn.close()
print ("DB Dump success")

#MQTT to server
