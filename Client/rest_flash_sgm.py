#!/usr/bin/python

from flask import Flask, jsonify,request
from flaskext.mysql import MySQL
import RPi.GPIO as GPIO
import time,utils,os
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 

app = Flask(__name__)
mysql = MySQL()
urls=("/favicon.ico","dummy")

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'AmritaSGM'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route('/')
def welcome():
	return "\tWelcome to Amrita Smart-Grid Middleware.\n\n \tKindly use one of the APIs to get data"

@app.route('/update')
def update():
	cmd="git pull"
	os.system(cmd)
	return str(request.headers)

@app.route('/alive')
def alive():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeHealth ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Alive' : r})

@app.route('/<pinId>')
def action(pinId):
	pins = {26 : {'name' : 'R1', 'state' : GPIO.LOW},
		19 : {'name' : 'R2', 'state' : GPIO.LOW},
		13 : {'name' : 'R3', 'state' : GPIO.LOW},
		6 : {'name' : 'R4', 'state' : GPIO.LOW},
		12 : {'name' : 'R5', 'state' : GPIO.LOW},
		16 : {'name' : 'R6', 'state' : GPIO.LOW},
		20 : {'name' : 'R7', 'state' : GPIO.LOW},
		21 : {'name' : 'R8', 'state' : GPIO.LOW}}

	pinsID = {'R1' : {'gpio' : '26', 'state' : GPIO.LOW},
		  'R2' : {'gpio' : '19', 'state' : GPIO.LOW},
		  'R3' : {'gpio' : '13', 'state' : GPIO.LOW},
		  'R4': {'gpio' : '6', 'state' : GPIO.LOW},
		  'R5' : {'gpio' : '12', 'state' : GPIO.LOW},
		  'R6' : {'gpio' : '16', 'state' : GPIO.LOW},
		  'R7' : {'gpio' : '20', 'state' : GPIO.LOW},
		  'R8' : {'gpio' : '21', 'state' : GPIO.LOW}}
	for pin in pins:
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, GPIO.LOW)
	
	#state=int(state)
	device=pinsID[pinId]['gpio']
	print(device)
	#print(pinsID[pinId]['state'])
	GPIO.output(int(device),GPIO.HIGH)
	time.sleep(0.3)
	GPIO.output(int(device),GPIO.LOW)
	utils.switchrest()
	return (str(device)+ " Activated")

@app.route('/maxim')
def maxim():
	cur = mysql.connect().cursor()
	cur.execute('select * from maximData ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/sch')
def sch():
	cur = mysql.connect().cursor()
	cur.execute('select * from schData ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/switchState')
def switchState():
	cur = mysql.connect().cursor()
	cur.execute('select * from switchState ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'switchState' : r})

@app.route('/recentgm')
def recentgm():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/recentlm1')
def recentlm1():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where meterType=2 ORDER BY id DESC LIMIT 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/recentlm2')
def recentlm2():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where meterType=3 ORDER BY id DESC LIMIT 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/outbackrecent')
def outbackrecent():
	cur = mysql.connect().cursor()
	cur.execute('select * from inverterData ORDER BY id DESC LIMIT 6')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/outbackinv')
def outbackinv():
	cur = mysql.connect().cursor()
	cur.execute('select nodeid,type,port,battVoltage,aux,error,dev,vac1_in_l2,ac_input,vac_out_l2,inv_mode,inv_i_l2,warn,buy_i_l2,vac_in_l2,sell_i_l2,chg_i_l2,ac_mode from inverterData where dev="FXR" ORDER BY id DESC LIMIT 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/outbackcc')
def outbackcc():
	cur = mysql.connect().cursor()
	cur.execute('select nodeid,type,port,battVoltage,aux,error,dev,cc_mode,aux_mode,in_i,out_i,in_v,out_kwh,out_ah  from inverterData where dev="CC" ORDER BY id DESC LIMIT 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/hour')
def hhistory():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where timestamp >= DATE_SUB(NOW(),INTERVAL 1 HOUR)')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Last one hour' : r})

@app.route('/day')
def dhistory():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where timestamp >= DATE_SUB(NOW(),INTERVAL 1 DAY)')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Last one day' : r})

@app.route('/month')
def mhistory():
        cur = mysql.connect().cursor()
        cur.execute('select * from nodeData where timestamp >= DATE_SUB(NOW(),INTERVAL 1 MONTH)')
        r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
        return jsonify({'Last one month' : r})

@app.route('/year')
def yhistory():
        cur = mysql.connect().cursor()
        cur.execute('select * from nodeData where timestamp >= DATE_SUB(NOW(),INTERVAL 1 YEAR)')
        r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
        return jsonify({'Last one year' : r})



@app.route('/switchstatus')
def switchstatus():
	cur = mysql.connect().cursor()
	cur.execute('select * from switchState ORDER BY id DESC LIMIT 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Switch Status' : r})

@app.route('/events')
def events():
	cur = mysql.connect().cursor()
	cur.execute('select * from event ORDER BY id DESC LIMIT 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Event Data' : r})

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=1)

