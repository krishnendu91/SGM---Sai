#!/usr/bin/python3

import datetime,sys,os,io
from datetime import datetime
from urllib.request import urlopen
from flask import Flask, render_template, request, redirect, session, jsonify, url_for
from passlib.hash import bcrypt
from flaskext.mysql import MySQL
# import matplotlib.pyplot as plt
# import matplotlib.dates as md
import base64
import pymysql
from flask_cors import CORS
from functools import wraps


# import dispenserHelper as dh


app = Flask(__name__)
app.secret_key = 'intelinfra'

CORS(app)
mysql = MySQL()
urls=("/favicon.ico","dummy")
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'AmritaSGM'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

users = {'admin': bcrypt.hash('password123'), 'user': bcrypt.hash('123456')}


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
	'13':{'url':"http://192.168.179.243:5000/"},
	'14':{'url':"http://192.168.179.244:5000/"},
	'15':{'url':"http://192.168.190.141:5000/"},
	'16':{'url':"http://192.168.190.142:5000/"},
	'17':{'url':"http://192.168.190.143:5000/"},}

def login_required(route_function):
    @wraps(route_function)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login', next=request.url))
        return route_function(*args, **kwargs)
    return decorated_function

def security(fname):
	APILog={'clientAgent':str(request.headers.get('User-Agent')),
		'clientIP':str(request.environ['REMOTE_ADDR']),
		'API':fname}
	
	conn = mysql.connect()
	cur=conn.cursor()
	cur.execute('INSERT INTO APILogs(clientAgent,clientIP,API)VALUES(%(clientAgent)s,%(clientIP)s,%(API)s); ',APILog)
	conn.commit()

# FOR DISPENSER
# @app.route('/Dispenser/getAddress')
# def getAddress():
# 	security(str(sys._getframe().f_code.co_name))
# 	address=dh.addressGen()

# @app.route('/Dispenser/sendData/<address>/<data>')
# def sendData(address,data):
# 	security(str(sys._getframe().f_code.co_name))
# 	rc=dh.sendData(address,data)
# 	if rc==0:
# 		return "Transaction failed"
# 	elif rc==1:
# 		return "Transaction success"
# 	else:
# 		return "Transaction not processed"

# @app.route('/Dispenser/sendMoney/<address>/<data>/<money>')
# def sendMoney(address,data,money):
# 	security(str(sys._getframe().f_code.co_name))

# 	rc=dh.sendMoney(address,data,int(money))
# 	if rc==0:
# 		return "Transaction failed"
# 	elif rc==1:
# 		return "Transaction success"
# 	else:
# 		return "Transaction not processed"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and bcrypt.verify(password, users[username]):
            # Successful login
            session['username'] = username
            redirected_from = session.pop('redirected_from', None)
            return redirect(redirected_from or url_for('welcome'))
        else:
            # Failed login
            return 'Invalid username or password'
    else:
        if 'username' in session:
            return redirect(url_for('welcome'))
        else:
            return render_template('index2.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')



@app.route('/timenow')
@login_required
def timenow():
	security(str(sys._getframe().f_code.co_name))
	now = datetime.now()
	return (now.strftime("%Y-%m-%d %H:%M:%S"))

@app.route('/temperature')
@login_required
def temperature():
	security(str(sys._getframe().f_code.co_name))
	conn = pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
	cur = conn.cursor(pymysql.cursors.DictCursor)
	cur.execute("SELECT timestamp,temp FROM tempData ORDER BY id DESC limit 1")
	r=cur.fetchall()
	return jsonify({'Temperature' : r})

@app.route('/')
@login_required
def welcome():
	security(str(sys._getframe().f_code.co_name))
#	print "Welcome to Amrita Smart-Grid Middleware"
#	print "kindly use one of the APIs to get data"
	return "Welcome to Amrita Intelligent Infrastructure Data Management and Control Panel App. \n Use one of the options below."
	#return render_template('/home/cs/SGM/Server/welcome.html')

@app.route('/stp/test')
@login_required
def stptest():
	security(str(sys._getframe().f_code.co_name))
	#cur = mysql.connect().cursor()
	cmd="/home/cs/SGM/Server/STPHour.py"
	os.system(cmd)
	#cur.execute("SET GLOBAL time_zone = '+05:30';")
	#r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	#return jsonify({'STP Test Data' : r})
	return 'done'

@app.route('/stp/pumplist')
@login_required
def stppump():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('SELECT meterName FROM `STP` order by id ASC')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'STP Data' : r})

@app.route('/stp/<meterName>')
@login_required
def stpdata(meterName):
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('SELECT timestamp,A,VLL,PF,F,W,WH FROM `STPData` where meterName=%s ORDER by id DESC LIMIT 1',meterName)
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'STP Data' : r})

@app.route('/stp/state/<meterName>')
@login_required
def stpstate(meterName):
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('SELECT state FROM `STPState` where meterName=%s ORDER by id DESC LIMIT 1',meterName)
	s = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'STP Data' : s})

@app.route('/deadnodes')
@login_required
def deadnodes():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('SELECT nodeId FROM `lastseen` WHERE alive =0 and timestamp>= NOW() - INTERVAL 3 MINUTE ORDER BY `id` DESC')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Dead Nodes' : r})

@app.route('/xlgen')
@login_required
def xlgen():
	security(str(sys._getframe().f_code.co_name))
	cmd="/home/cs/SGM/Server/XLGen.py"
	os.system(cmd)
	return "Check Your Mailbox"

@app.route('/reboot')
@login_required
def rebootS():
	security(str(sys._getframe().f_code.co_name))
	cmd="reboot"
	#os.system(cmd)
	return "Server rebooting"


@app.route('/updateserver')
@login_required
def serverupdate():
	security(str(sys._getframe().f_code.co_name))
	cmd="/home/cs/SGM_Local/gitpull.sh"
	os.system(cmd)
	return "Server Updation Complete"

@app.route('/switchname/<node>')
@login_required
def switchname(node):
	node=str(node)
	security(str(sys._getframe().f_code.co_name))
	conn = mysql.connect()
	cur=conn.cursor()
	cur.execute('select switchId,switchname from switch where nodeId=%s ORDER BY id ASC ',node)
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'mqtt Test data' : r})

@app.route('/restart')
@login_required
def restart():
	security(str(sys._getframe().f_code.co_name))
	cmd="/home/cs/restartRest.sh"
	os.system(cmd)
	return "restart complete"
@app.route('/mqttlog')
@login_required
def mqttlog():
	security(str(sys._getframe().f_code.co_name))
	conn = mysql.connect()
	cur=conn.cursor()
	cur.execute('select timestamp,log from mqttLog ORDER BY id DESC limit 15')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'mqtt log' : r})

@app.route('/dimis/update/<node>')
@login_required
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
@login_required
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
		message="Node : " + str(node)+ " " + str(switch)+ " Triggered successfully"
		
	except:
		pass
		success=0
		message="Error accessing URL \n " + str(sURL)
	switchControl={"nodeId":node,"switchID":switch,"switchState":1,"success":success}
	#cur.execute('INSERT INTO switchInstruction(nodeId,switchID,switchState,success)VALUES(%(nodeId)s,%(switchID)s,%(switchState)s,%(success)s); ',switchControl)
	#conn.commit()
	print("Switch State Updated in DB")
	return message

@app.route('/mqtttest')
@login_required
def mqtttest():
	security(str(sys._getframe().f_code.co_name))
	conn = mysql.connect()
	cur=conn.cursor()
	cur.execute('select * from mqttTest ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'mqtt Test data' : r})

@app.route('/alive/<id>')
@login_required
def alive_1(id):
	security(str(sys._getframe().f_code.co_name))
	conn = mysql.connect()
	cur=conn.cursor()
	cur.execute('select * from lastseen where nodeid=%s ORDER BY id DESC LIMIT 1 ',id)
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Alive' : r})

@app.route('/alive/100')
@login_required
def alive_100():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('SELECT * FROM `nodeHealth` WHERE aggId =1 ORDER BY `id` DESC limit 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Alive' : r})

@app.route('/alive/200')
@login_required
def alive_200():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('SELECT * FROM `nodeHealth` WHERE aggId =2 ORDER BY `id` DESC limit 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=(r[0]['timestamp'].timestamp())*1000
	return jsonify({'Alive' : r})

@app.route('/alive/300')
@login_required
def alive_300():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('SELECT * FROM `nodeHealth` WHERE aggId =3 ORDER BY `id` DESC limit 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Alive' : r})

@app.route('/weather')
@login_required
def weather():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from weather ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'current weather' : r})

@app.route('/weathersummary')
@login_required
def weathersummary():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select summary,apparentTemperature,humidity from weather ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify(r)

@app.route('/site')
@login_required
def site():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('SELECT * FROM `projectSite` ORDER by siteId ASC')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Project Sites' : r})

@app.route('/metertype')
@login_required
def metertype():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('SELECT * FROM `Meter` ORDER BY meterID ASC')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Available Meters' : r})

@app.route('/dimis/switchstate/<id>')
@login_required
def n1switchState(id):
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from switchState where nodeId=%s ORDER BY id DESC LIMIT 1 ',id)
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'switchState' : r})

@app.route('/dimis/recentgm1')
@login_required
def recentgm():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/recentlm')
@login_required
def recentlm1():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where meterType=2 ORDER BY id DESC LIMIT 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/recentgm2')
@login_required
def recentlm2():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where meterType=3 ORDER BY id DESC LIMIT 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/outbackrecent')
@login_required
def outbackrecent():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from inverterData ORDER BY id DESC LIMIT 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

#Event API
@app.route('/dimis/event')
@login_required
def event():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from event ORDER BY id DESC LIMIT 15')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['updateTime'].timestamp()
	return jsonify({'Event Data' : r})

#API for node level filtering
@app.route('/dimis/<id>/gm1')
@login_required
def n1(id):
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=%s and meterType=1 ORDER BY id DESC LIMIT 1 ',id)
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/dimis/<id>/gm2')
@login_required
def n2(id):
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=%s and meterType=3 ORDER BY id DESC LIMIT 1 ',id)
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/dimis/<id>/lm')
@login_required
def n3(id):
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=%s and meterType=2 ORDER BY id DESC LIMIT 1 ',id)
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['Timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/maxim/1')
@login_required
def maxim():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from maximData where nodeId="IL_1" ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/maxim/2')
@login_required
def maxim1():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from maximData where nodeId="IL_2" ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/maxim/3')
@login_required
def maxim2():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from maximData where nodeId="IL_3" ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/maxim/4')
@login_required
def maxim3():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from maximData where nodeId="IL_4" ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/maxim/5')
@login_required
def maxim4():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from maximData where nodeId="IL_5" ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/maxim/6')
@login_required
def maxim5():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from maximData where nodeId="IL_6" ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/outbackinv')
@login_required
def outbackinv():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select nodeid,type,port,battVoltage,aux,error,dev,vac1_in_l2,ac_input,vac_out_l2,inv_mode,inv_i_l2,warn,buy_i_l2,vac_in_l2,sell_i_l2,chg_i_l2,ac_mode from inverterData where dev="FXR" ORDER BY id DESC LIMIT 3')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/outbackcc')
@login_required
def outbackcc():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select nodeid,type,port,battVoltage,aux,error,dev,cc_mode,aux_mode,in_i,out_i,in_v,out_kwh,out_ah  from inverterData where dev="CC" ORDER BY id DESC LIMIT 3')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/sch')
@login_required
def sch():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from schData ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

#4Ward
@app.route('/4ward/trbdata')
@login_required
def trb():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from trbdata ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
# 	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/4ward/trbdata/<imei>')
@login_required
def trbimei(imei):
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from trbdata where DevID=%s ORDER BY id DESC LIMIT 1 ',imei)
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
# 	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/4ward/faclon')
@login_required
def faclon():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from faclon ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
# 	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/4ward/faclon/<imei>')
@login_required
def faclonimei(imei):
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from faclon where imei = %s ORDER BY id DESC LIMIT 1 ',imei)
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
# 	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/4ward/faclonRaw')
@login_required
def faclonRaw():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from faclonRaw ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
# 	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/4ward/wiman')
@login_required
def wiman():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from wiman ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
# 	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/4ward/wiman/<imei>')
@login_required
def wimanimei(imei):
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from wiman where imei = %s ORDER BY id DESC LIMIT 1 ',imei)
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
# 	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/4ward/wimanRaw')
@login_required
def wimanRaw():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from wimanRaw ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
# 	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/4ward/embedosRaw')
@login_required
def embedosRaw():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from embedosRaw ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
# 	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/4ward/embedos')
@login_required
def embedos():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from embedos ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
# 	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})


@app.route('/4ward/embedos/<devid>')
@login_required
def embedosID(devid):
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from embedos where deviceId =%s  ORDER BY id DESC LIMIT 1 ',devid)
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
# 	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/4ward/VVM/<devID>')
@login_required
def VVMdev(devID):
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from VVMGateway where devID = %s ORDER BY id DESC LIMIT 1 ',devID)
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
# 	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})

@app.route('/4ward/VVM')
@login_required
def VVM():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from VVMGateway ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
# 	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify({'Recent data' : r})



@app.route('/BIoT/API1')
def biot1():
	security(str(sys._getframe().f_code.co_name))
	cur = mysql.connect().cursor()
	cur.execute('select * from wiman ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
# 	r[0]['timestampEpoch']=r[0]['timestamp'].timestamp()*1000
	return jsonify(r)

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=5000,debug=1)

