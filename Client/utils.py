import sys
import socket,mqttservice
import time,json
from datetime import datetime
import pymysql
from subprocess import check_output

def sysinfo():
#get IP addresses
  ip_scanoutput=check_output(["hostname -I"],shell=1)
  ip_eth0=ip_scanoutput.decode().split()[0]
  ip_wlan0=ip_scanoutput.decode().split()[1]

#get node ID
  id_scanoutput=check_output(["hostname"],shell=1)
  id_node=id_scanoutput.decode().split()[0]
  if len(id_node)>9:
  	nodeId=int(id_node[-2:])
  else:
    nodeId=int(id_node[-1:])
