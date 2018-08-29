import paho.mqtt.client as mqtt
# This is the Subscriber

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("topic/test")

def on_message(client, userdata, msg):
	#if msg.payload.decode() == "Hello world!":
	status=msg.payload.decode()
	#print(status)
	data={'status':status}
	print(data)
  #todb(data)
    #client.disconnect()
    
client = mqtt.Client()
client.connect("0.0.0.0",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
