import paho.mqtt.client as mqtt
#acknowledgement 


def on_message(client1, userdata, msg):
	payload=msg.payload.decode()
	print(payload)
	if payload == "SUCCESS":
		dbclear(time)
		print("ack received")
	else:
		print("ack failed")
		
	client1.disconnect()
def mqttack():
	client1 = mqtt.Client()
	client1.connect("0.0.0.0",1883,60)
	client1.subscribe("SGM/ack")
	client1.on_message = on_message
	client1.loop_forever()

def dbclear:
	print("hello")
