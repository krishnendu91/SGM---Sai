import paho.mqtt.client as mqtt

# This is the Publisher
broker="192.168.112.110"
client = mqtt.Client()
client.connect(broker,1883,60)
client.publish("topic/test", "Hello world!");
client.disconnect();
