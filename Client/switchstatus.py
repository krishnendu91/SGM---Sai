#!/usr/bin/python

import utils,mqttservice
ip_eth0,ip_wlan0,id_node=utils.sysinfo()
utils.switchstatus()
print("Switch State updated")
