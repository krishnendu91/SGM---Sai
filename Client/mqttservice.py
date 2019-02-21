import paho.mqtt.client as mqtt
import json,mqtt_reply

def mqtt_publish(broker,port,topic,payload,ip_wlan0):
# This is the Publisher
  #broker="192.168.112.110"
  #port=1883
  #topic="switch"
  #payload="ON"
	payload={'message':payload,"ip":ip_wlan0}
	payload=json.dumps(payload)
	topic="SGM/"+topic
	client = mqtt.Client()
	client.connect(broker,port,600)
	(rc,mid)=client.publish(topic,payload);
	client.disconnect();
	mqtt_reply.mqttack()
