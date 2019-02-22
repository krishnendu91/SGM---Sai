#!/usr/bin/python3

import datetime,sys,os
from urllib.request import urlopen
from flask import Flask, jsonify,request
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
urls=("/favicon.ico","dummy")
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'AmritaSGM'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

nodeId={'1':{'url':"http://192.168.179.231:5000/"},
	'2':{'url':"http://192.168.179.232:5000/"},
	'3':{'url':"http://192.168.179.233:5000/"},
	'4':{'url':"http://192.168.179.234:5000/"},
	'5':{'url':"http://192.168.179.235:5000/"},
	'6':{'url':"http://192.168.179.236:5000/"},
	'7':{'url':"http://192.168.179.237:5000/"},
	'8':{'url':"http://192.168.179.238:5000/"},
	'9':{'url':"http://192.168.179.239:5000/"},
	'10':{'url':"http://192.168.179.240:5000/"},
	'11':{'url':"http://192.168.179.241:5000/"},
	'12':{'url':"http://192.168.179.242:5000/"},
	'13':{'url':"http://192.168.179.243:5000/"},}

def security(fname):
	APILog={'clientAgent':str(request.headers.get('User-Agent')),
		'clientIP':str(request.environ['REMOTE_ADDR']),
		'API':fname}
	
	conn = mysql.connect()
	cur=conn.cursor()
	cur.execute('INSERT INTO APILogs(clientAgent,clientIP,API)VALUES(%(clientAgent)s,%(clientIP)s,%(API)s); ',APILog)
	conn.commit()

@app.route('/')
def welcome():
	security(str(sys._getframe().f_code.co_name))
#	print "Welcome to Amrita Smart-Grid Middleware"
#	print "kindly use one of the APIs to get data"
	return "\tWelcome to Amrita Smart-Grid Middleware.\n\n \tKindly use one of the APIs to get data"

@app.route('/updateserver')
def serverupdate():
	security(str(sys._getframe().f_code.co_name))
	cmd="/home/cs/SGM_Local/gitpull.sh"
	os.system(cmd)
	return "Server Updation Complete"

@app.route('/restart')
def restart():
	security(str(sys._getframe().f_code.co_name))
	cmd="restartServer.py"
	os.system(cmd)
	return "restart complete"

@app.route('/dimis/update/<node>')
def updatedimis(node):
	security(str(sys._getframe().f_code.co_name))
	sURL=str(nodeId[node]['url'])+'update'
	try:	
		api_page = urlopen(sURL) #Python 3
		api=api_page.read()
		message=api
	except:
		pass
		message="Error accessing URL \n " + str(sURL)
	return message

@app.route('/dimis/switchcontrol/<node>/<switch>')
def switchcontrol(node,switch):
	security(str(sys._getframe().f_code.co_name))
	conn = mysql.connect()
	cur=conn.cursor()
	dURL='192.168.179.23'+str(node)+':2000/'+str(switch)
	sURL=str(nodeId[node]['url'])+str(switch)
	print(dURL)
	print(sURL)
	try:	
		success=1
		api_page = urlopen(sURL) #Python 3
		api=api_page.read()
		message=str(sURL)+ " Triggered successfully"
		
	except:
		pass
		success=0
		message="Error accessing URL \n " + str(sURL)
	switchControl={"nodeId":node,"switchID":switch,"switchState":1,"success":success}
	cur.execute('INSERT INTO switchInstruction(nodeId,switchID,switchState,success)VALUES(%(nodeId)s,%(switchID)s,%(switchState)s,%(success)s); ',switchControl)
	conn.commit()
	print("Switch State Updated in DB")
	return message

@app.route('/mqtttest')
def mqtttest():
	security(str(sys._getframe().f_code.co_name))
	conn = mysql.connect()
	cur=conn.cursor()
	cur.execute('select * from mqttTest ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'mqtt Test data' : r})

@app.route('/alive/1')
def alive_1():
	security(str(sys._getframe().f_code.co_name))
	conn = mysql.connect()
	cur=conn.cursor()
	cur.execute('select * from lastseen where nodeid=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Alive' : r})

@app.route('/alive/2')
def alive_2():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Alive' : r})

@app.route('/alive/3')
def alive_3():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=3 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Alive' : r})

@app.route('/alive/4')
def alive_4():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=4 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Alive' : r})

@app.route('/alive/5')
def alive_5():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=5 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Alive' : r})

@app.route('/alive/6')
def alive_6():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=6 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Alive' : r})

@app.route('/alive/7')
def alive_7():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=7 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Alive' : r})

@app.route('/alive/8')
def alive_8():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=8 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Alive' : r})

@app.route('/alive/9')
def alive_9():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=9 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Alive' : r})

@app.route('/alive/10')
def alive_10():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=10 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Alive' : r})

@app.route('/alive/11')
def alive_11():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=11 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Alive' : r})

@app.route('/alive/12')
def alive_12():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=12 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Alive' : r})

@app.route('/alive/13')
def alive_13():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=13 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Alive' : r})

@app.route('/alive/14')
def alive_14():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=14 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Alive' : r})

@app.route('/alive/100')
def alive_100():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('SELECT * FROM `nodeHealth` WHERE aggId =1 ORDER BY `id` DESC limit 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Alive' : r})

@app.route('/alive/200')
def alive_200():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('SELECT * FROM `nodeHealth` WHERE aggId =2 ORDER BY `id` DESC limit 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=(r[0]['timestamp'].timestamp())*1000
	return jsonify({'Alive' : r})

@app.route('/alive/300')
def alive_300():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('SELECT * FROM `nodeHealth` WHERE aggId =3 ORDER BY `id` DESC limit 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Alive' : r})

@app.route('/weather')
def weather():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from weather ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'current weather' : r})

@app.route('/site')
def site():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('SELECT * FROM `projectSite` ORDER by siteId ASC')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Project Sites' : r})

@app.route('/metertype')
def metertype():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('SELECT * FROM `Meter` ORDER BY meterID ASC')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Available Meters' : r})

@app.route('/dimis/switchstate/1')
def n1switchState():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from switchState where nodeId=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'switchState' : r})

@app.route('/dimis/switchstate/2')
def n2switchState():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from switchState where nodeId=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'switchState' : r})

@app.route('/dimis/switchstate/3')
def n3switchState():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from switchState where nodeId=3 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'switchState' : r})

@app.route('/dimis/switchstate/4')
def n4switchState():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from switchState where nodeId=4 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'switchState' : r})

@app.route('/dimis/switchstate/5')
def n5switchState():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from switchState where nodeId=5 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'switchState' : r})

@app.route('/dimis/switchstate/6')
def n6switchState():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from switchState where nodeId=6 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'switchState' : r})

@app.route('/dimis/switchstate/7')
def n7switchState():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from switchState where nodeId=7 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'switchState' : r})

@app.route('/dimis/switchstate/8')
def n8switchState():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from switchState where nodeId=8 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'switchState' : r})

@app.route('/dimis/switchstate/9')
def n9switchState():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from switchState where nodeId=9 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'switchState' : r})

@app.route('/dimis/switchstate/10')
def n10switchState():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from switchState where nodeId=10 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'switchState' : r})

@app.route('/dimis/switchstate/11')
def n11switchState():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from switchState where nodeId=11 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'switchState' : r})

@app.route('/dimis/switchstate/12')
def n12switchState():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from switchState where nodeId=12 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'switchState' : r})

@app.route('/dimis/switchstate/13')
def n13switchState():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from switchState where nodeId=13 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'switchState' : r})

@app.route('/dimis/recentgm1')
def recentgm():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/recentlm')
def recentlm1():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where meterType=2 ORDER BY id DESC LIMIT 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/recentgm2')
def recentlm2():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where meterType=3 ORDER BY id DESC LIMIT 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/outbackrecent')
def outbackrecent():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from inverterData ORDER BY id DESC LIMIT 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

#Event API
@app.route('/dimis/event')
def event():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from event ORDER BY id DESC LIMIT 15')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['updateTime'].timestamp()
	return jsonify({'Event Data' : r})

#API for node level filtering
@app.route('/dimis/1/gm1')
def n1():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=1 and meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/2/gm1')
def n2_gm():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=2 and meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/2/lm')
def n2_lm():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=2 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/3/gm1')
def n3_gm():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=3 and meterType=1  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/3/lm')
def n3_lm():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=3 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/4/gm1')
def n4_gm1():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=4  and meterType =1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/4/lm')
def n4_lm():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=4 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/5/gm1')
def n5_gm1():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=5 and meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/5/lm')
def n5_lm():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=5 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/6/gm1')
def n6_gm1():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=6 and meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/6/lm')
def n6_lm():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=6 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/7/gm1')
def n7_gm1():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=7 and meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/7/lm')
def n7_lm():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=7 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/7/gm2')
def n7_gm3():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=7 and meterType=3 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/8/gm1')
def n8_gm1():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=8 amd meterType=1  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/8/lm')
def n8_lm():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=8 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/9/gm1')
def n9_gm1():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=9 and meterType=1  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/9/lm')
def n9_lm():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=9 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/9/gm2')
def n9_gm2():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=9 and meterType=3 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/10/gm1')
def n10_gm1():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=10 and meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/10/lm')
def n10_lm():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=10 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/11/gm1')
def n11_gm1():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=11 and meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/11/lm')
def n11_lm():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=11 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/12/gm1')
def n12_gm1():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=12 and meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/12/lm')
def n12_lm():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=12 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/12/gm2')
def n12_gm2():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=12 and meterType=3 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/13/gm1')
def n13_gm1():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=13 and meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/dimis/13/lm')
def n13_lm():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=13 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/maxim/1')
def maxim():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from maximData where nodeId="IL_1" ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/maxim/2')
def maxim1():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from maximData where nodeId="IL_2" ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/maxim/3')
def maxim2():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from maximData where nodeId="IL_3" ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/maxim/4')
def maxim3():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from maximData where nodeId="IL_4" ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/maxim/5')
def maxim4():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from maximData where nodeId="IL_5" ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/maxim/6')
def maxim5():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from maximData where nodeId="IL_6" ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/outbackinv')
def outbackinv():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select nodeid,type,port,battVoltage,aux,error,dev,vac1_in_l2,ac_input,vac_out_l2,inv_mode,inv_i_l2,warn,buy_i_l2,vac_in_l2,sell_i_l2,chg_i_l2,ac_mode from inverterData where dev="FXR" ORDER BY id DESC LIMIT 3')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/outbackcc')
def outbackcc():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select nodeid,type,port,battVoltage,aux,error,dev,cc_mode,aux_mode,in_i,out_i,in_v,out_kwh,out_ah  from inverterData where dev="CC" ORDER BY id DESC LIMIT 3')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Recent data' : r})

@app.route('/sch')
def sch():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from schData ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()
	return jsonify({'Recent data' : r})

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=5000,debug=1)
	print(request.environ['REMOTE_ADDR'])

