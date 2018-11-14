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

@app.route('/weather')
def weather():
	cur = mysql.connect().cursor()
	cur.execute('select * from weather ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'current weather' : r})


@app.route('/dimis/recentgm')
def recentgm():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where meterType=1 ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/recentlm1')
def recentlm1():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where meterType=2 ORDER BY id DESC LIMIT 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/recentlm2')
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

@app.route('/dimis/hour')
def hhistory():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where timestamp >= DATE_SUB(NOW(),INTERVAL 1 HOUR)')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Last one hour' : r})

@app.route('/dimis/day')
def dhistory():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where timestamp >= DATE_SUB(NOW(),INTERVAL 1 DAY)')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Last one day' : r})

@app.route('/dimis/month')
def mhistory():
        cur = mysql.connect().cursor()
        cur.execute('select * from nodeData where timestamp >= DATE_SUB(NOW(),INTERVAL 1 MONTH)')
        r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
        return jsonify({'Last one month' : r})

#One year
@app.route('/dimis/year')
def yhistory():
        cur = mysql.connect().cursor()
        cur.execute('select * from nodeData where timestamp >= DATE_SUB(NOW(),INTERVAL 1 YEAR)')
        r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
        return jsonify({'Last one year' : r})

#Event API
@app.route('/dimis/event')
def event():
        cur = mysql.connect().cursor()
        cur.execute('select * from event where errorTime >= DATE_SUB(NOW(),INTERVAL 1 YEAR)')
        r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
        return jsonify({'Event Data' : r})

#API for node level filtering
@app.route('/dimis/1')
def n1():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=1  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/2')
def n2():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=2  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/3')
def n3():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=3  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/4')
def n4():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=4  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/5')
def n5():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=5  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/6')
def n6():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=6  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/7')
def n7():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=7  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/8')
def n8():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=8  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/9')
def n9():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=9  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/10')
def n10():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=10  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/11')
def n11():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=11  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/12')
def n12():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=12  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/13')
def n13():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=13  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/dimis/14')
def n14():
	cur = mysql.connect().cursor()
	cur.execute('select * from nodeData where nodeId=14  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})




if __name__ == '__main__':
    app.run(host="0.0.0.0",port=7070,debug=1)

