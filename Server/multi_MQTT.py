#!/usr/bin/python3
import sys
import os
import paho.mqtt.client as paho

global mqttclient;
global broker;
global port;

broker = "192.168.112.110";
port = 1883;
mypid = os.getpid()
print(mypid)
client_uniq = "pubclient_"+str(mypid)
mqttclient = paho.Client(client_uniq, False) #nocleanstart
mqttclient.connect(broker, port, 60)
mqttclient.subscribe("Commands/#")

def test1(client, userdata, message):
  print("test1")
  print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "' with QoS " + str(message.qos))
  
def test2(client, userdata, message):
  print("test2")
  print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "' with QoS " + str(message.qos))

  
  
mqttclient.message_callback_add("Commands/test1", test1)
mqttclient.message_callback_add("Commands/test2", test2)
mqttclient.loop_forever()

