import sys
import socket,mqttservice
import time,json
from datetime import datetime
import pymysql
from subprocess import check_output

def sysinfo():
#get IP addresses
  try:
  ip_scanoutput=check_output(["hostname -I"],shell=1)
  ip_eth0=ip_scanoutput.decode().split()[0]
  ip_wlan0=ip_scanoutput.decode().split()[1]
