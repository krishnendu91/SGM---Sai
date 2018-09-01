import paho.mqtt.client as mqtt
import json
#acknowledgement 


def on_message(client1, userdata, msg):
	payload=json.loads(msg.payload.decode())
	print(payload)
	reply = payload['message']
	txId = payload['id']

	if reply == "SUCCESS":
		dbclear(txId)
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

def dbclear(txId):
	print("hello")
	conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
	cur=conn.cursor()
	cur.execute("DELETE FROM nodeData where id = %s;",txId)
	cur.close()
	conn.commit()
	conn.close()
	print ("DB clear success")
	
