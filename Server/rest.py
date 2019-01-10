#!/usr/bin/python3


from flask import Flask, jsonify
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

@app.route('/')
def welcome():
#	print "Welcome to Amrita Smart-Grid Middleware"
#	print "kindly use one of the APIs to get data"
	return "\tWelcome to Amrita Smart-Grid Middleware.\n\n \tKindly use one of the APIs to get data"

@app.route('/mqtttest')
def mqtttest():
	cur = mysql.connect().cursor()
	cur.execute('select * from mqttTest ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'mqtt Test data' : r})

@app.route('/alive/1')
def alive_1():
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Alive' : r})

@app.route('/alive/2')
def alive_2():
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Alive' : r})

@app.route('/alive/3')
def alive_3():
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=3 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Alive' : r})

@app.route('/alive/4')
def alive_4():
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=4 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Alive' : r})

@app.route('/alive/5')
def alive_5():
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=5 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Alive' : r})

@app.route('/alive/6')
def alive_6():
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=6 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Alive' : r})

@app.route('/alive/7')
def alive_7():
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=7 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Alive' : r})

@app.route('/alive/8')
def alive_8():
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=8 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Alive' : r})

@app.route('/alive/9')
def alive_9():
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=9 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Alive' : r})

@app.route('/alive/10')
def alive_10():
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=10 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Alive' : r})

@app.route('/alive/11')
def alive_11():
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=11 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Alive' : r})

@app.route('/alive/12')
def alive_12():
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=12 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Alive' : r})

@app.route('/alive/13')
def alive_13():
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=13 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Alive' : r})

@app.route('/alive/14')
def alive_14():
	cur = mysql.connect().cursor()
	cur.execute('select * from lastseen where nodeid=14 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Alive' : r})

@app.route('/alive/100')
def alive_100():
	cur = mysql.connect().cursor()
	cur.execute('SELECT * FROM `nodeHealth` WHERE aggId =1 ORDER BY `id` DESC limit 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Alive' : r})

@app.route('/alive/200')
def alive_200():
	cur = mysql.connect().cursor()
	cur.execute('SELECT * FROM `nodeHealth` WHERE aggId =2 ORDER BY `id` DESC limit 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Alive' : r})

@app.route('/alive/300')
def alive_300():
	cur = mysql.connect().cursor()
	cur.execute('SELECT * FROM `nodeHealth` WHERE aggId =3 ORDER BY `id` DESC limit 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Alive' : r})

@app.route('/weather')
def weather():
	cur = mysql.connect().cursor()
	cur.execute('select * from weather ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'current weather' : r})

@app.route('/site')
def site():
	cur = mysql.connect().cursor()
	cur.execute('SELECT * FROM `projectSite` ORDER by siteId ASC')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Project Sites' : r})

@app.route('/metertype')
def metertype():
	cur = mysql.connect().cursor()
	cur.execute('SELECT * FROM `Meter` ORDER BY meterID ASC')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Available Meters' : r})

@app.route('/dimis/switchstate')
def switchState():
	cur = mysql.connect().cursor()
	cur.execute('select * from switchState ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'switchState' : r})

@app.route('/dimis/recentgm1')
def recentgm():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/recentlm')
def recentlm1():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where meterType=2 ORDER BY id DESC LIMIT 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/recentgm2')
def recentlm2():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where meterType=3 ORDER BY id DESC LIMIT 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/outbackrecent')
def outbackrecent():
	cur = mysql.connect().cursor()
	cur.execute('select * from inverterData ORDER BY id DESC LIMIT 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

#Event API
@app.route('/dimis/event')
def event():
        cur = mysql.connect().cursor()
        cur.execute('select * from event ORDER BY id DESC LIMIT 15')
        r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
        return jsonify({'Event Data' : r})

#API for node level filtering
@app.route('/dimis/1/gm1')
def n1():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=1 and meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/2/gm1')
def n2_gm():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=2 and meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/2/lm')
def n2_lm():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=2 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/3/gm1')
def n3_gm():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=3 and meterType=1  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/3/lm')
def n3_lm():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=3 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/4/gm1')
def n4_gm1():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=4  and meterType =1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/4/lm')
def n4_lm():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=4 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/5/gm1')
def n5_gm1():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=5 and meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/5/lm')
def n5_lm():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=5 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/6/gm1')
def n6_gm1():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=6 and meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/6/lm')
def n6_lm():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=6 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/7/gm1')
def n7_gm1():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=7 and meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/7/lm')
def n7_lm():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=7 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/7/gm2')
def n7_gm3():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=7 and meterType=3 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/8/gm1')
def n8_gm1():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=8 amd meterType=1  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/8/lm')
def n8_lm():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=8 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/9/gm1')
def n9_gm1():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=9 and meterType=1  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/9/lm')
def n9_lm():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=9 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/9/gm2')
def n9_gm2():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=9 and meterType=3 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/10/gm1')
def n10_gm1():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=10 and meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/10/lm')
def n10_lm():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=10 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/11/gm1')
def n11_gm1():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=11 and meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/2/lm')
def n11_lm():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=11 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/12/gm1')
def n12_gm1():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=12 and meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/12/lm')
def n12_lm():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=12 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/2/gm2')
def n12_gm2():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=12 and meterType=3 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/13/gm1')
def n13_gm1():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=13 and meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/13/lm')
def n13_lm():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=13 and meterType=2 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/maxim/1')
def maxim():
	cur = mysql.connect().cursor()
	cur.execute('select * from maximData where nodeId="IL_1" ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/maxim/2')
def maxim1():
	cur = mysql.connect().cursor()
	cur.execute('select * from maximData where nodeId="IL_2" ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/maxim/3')
def maxim2():
	cur = mysql.connect().cursor()
	cur.execute('select * from maximData where nodeId="IL_3" ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/maxim/4')
def maxim3():
	cur = mysql.connect().cursor()
	cur.execute('select * from maximData where nodeId="IL_4" ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/maxim/5')
def maxim4():
	cur = mysql.connect().cursor()
	cur.execute('select * from maximData where nodeId="IL_5" ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/maxim/6')
def maxim5():
	cur = mysql.connect().cursor()
	cur.execute('select * from maximData where nodeId="IL_6" ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/outbackinv')
def outbackinv():
	cur = mysql.connect().cursor()
	cur.execute('select nodeid,type,port,battVoltage,aux,error,dev,vac1_in_l2,ac_input,vac_out_l2,inv_mode,inv_i_l2,warn,buy_i_l2,vac_in_l2,sell_i_l2,chg_i_l2,ac_mode from inverterData where dev="FXR" ORDER BY id DESC LIMIT 3')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/outbackcc')
def outbackcc():
	cur = mysql.connect().cursor()
	cur.execute('select nodeid,type,port,battVoltage,aux,error,dev,cc_mode,aux_mode,in_i,out_i,in_v,out_kwh,out_ah  from inverterData where dev="CC" ORDER BY id DESC LIMIT 3')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/sch')
def sch():
	cur = mysql.connect().cursor()
	cur.execute('select * from schData ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	r=jsonify({'Recent data' : r})
	print(r['timestamp'])
	return r




if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=1)

