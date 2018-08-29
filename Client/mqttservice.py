import paho.mqtt.client as mqtt

def mqtt_publish(broker,port,topic,payload)
# This is the Publisher
  broker="192.168.112.110"
  client = mqtt.Client()
  client.connect(broker,port,60)
  client.publish(topic,payload);
  client.disconnect();
