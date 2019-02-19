#!/usr/bin/python

import utils,mqttservice
utils.switchstatus()
mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_switch","DONE",ip_wlan0)
