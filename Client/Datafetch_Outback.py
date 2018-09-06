#!/usr/bin/python

from datetime import datetime
import pymysql
from subprocess import check_output
from urllib.request import urlopen

scanoutput=check_output(["hostname -I"],shell=1)
ip_eth0=scanoutput.decode().split()[0]
ip_wlan0=scanoutput.decode().split()[1]
conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()

mate=urlopen('http://192.168.0.64/Dev_status.cgi?&Port=0')
mate=mate.read()
mate=json.loads(mate)
print(mate)

inv1= mate['devstatus']['ports'][0]
inv2= mate['devstatus']['ports'][1]
inv3= mate['devstatus']cur.execute("INSERT INTO nodeData(nodeid,meterType, v1, v2, v3, i1, i2, i3, w1,w2,w3,va1,va2,va3,var1,var2,var3,wh,vah,varh,wh1,wh2,wh3,vah1,vah2,vah3,varh1,varh2,varh3,pf1,pf2,pf3,f1,f2,f3,d1,d2,d3,d4,d5,d6,d7,d8) VALUES(%(nodeid)s,%(meterType)s,%(v1)s,%(v2)s,%(v3)s,%(i1)s,%(i2)s,%(i3)s,%(w1)s,%(w2)s,%(w3)s,%(va1)s,%(va2)s,%(va3)s,%(var1)s,%(var2)s,%(var3)s,%(wh)s,%(vah)s,%(varh)s,%(wh1)s,%(wh2)s,%(wh3)s,%(vah1)s,%(vah2)s,%(vah3)s,%(varh1)s,%(varh2)s,%(varh3)s,%(pf1)s,%(pf2)s,%(pf3)s,%(f1)s,%(f2)s,%(f3)s,%(D1)s,%(D2)s,%(D3)s,%(D4)s,%(D5)s,%(D6)s,%(D7)s,%(D8)s);",value_GM1)
conn.commit()['ports'][2]
cc1= mate['devstatus']['ports'][3]
cc2= mate['devstatus']['ports'][4]
cc3= mate['devstatus']['ports'][5]



print "inv1"
print inv1
print "inv2"
print inv2
print "inv3"
print inv3
print "cc1"
print cc1
print "cc2"
print cc2
print "cc3"
print cc3



mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch","DONE",ip_wlan0)
print("MQTT Success")
