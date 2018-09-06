#!/usr/bin/python

from datetime import datetime
import pymysql
from subprocess import check_output
from urllib.request import urlopen

scanoutput=check_output(["hostname -I"],shell=1)
ip_eth0=scanoutput.decode().split()[0]
ip_wlan0=scanoutput.decode().split()[1]

mate=urlopen('http://192.168.0.64/Dev_status.cgi?&Port=0')
mate=mate.read()
mate=json.loads(mate)
print(mate)

inv1= r['devstatus']['ports'][0]
inv2= r['devstatus']['ports'][1]
inv3= r['devstatus']['ports'][2]
cc1= r['devstatus']['ports'][3]
cc2= r['devstatus']['ports'][4]
cc3= r['devstatus']['ports'][5]

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
