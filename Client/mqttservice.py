import paho.mqtt.client as mqtt

def mqtt_publish(broker,port,topic,payload)
# This is the Publisher
  #broker="192.168.112.110"
  #port=1883
  #topic="switch"
  #payload="ON"
  topic="SGM/"+topic
  client = mqtt.Client()
  client.connect(broker,port,60)
  client.publish(topic,payload);
  client.disconnect();
