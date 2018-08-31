import paho.mqtt.client as mqtt

def mqttack(broker,reply):
	client1 = mqtt.Client()
	client1.connect(broker,1883,60)
	client1.publish("SGM/ack",reply);
	client1.disconnect()
	print('acksent')
	
