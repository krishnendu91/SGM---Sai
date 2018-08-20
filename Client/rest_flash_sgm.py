#!/usr/bin/python

from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
urls=("/favicon.ico","dummy")
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'AmritaSGM'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

@app.route('/')
def welcome():
#	print "Welcome to Amrita Smart-Grid Middleware"
#	print "kindly use one of the APIs to get data"
	return "\tWelcome to Amrita Smart-Grid Middleware.\n\n \tKindly use one of the APIs to get data"


@app.route('/recentgm')
def recentgm():
	cur = mysql.connect().cursor()
	cur.execute('select * from node_data ORDER BY id DESC LIMIT 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/recentlm1')
def recentlm1():
	cur = mysql.connect().cursor()
	cur.execute('select * from node_data ORDER BY id DESC LIMIT 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/recentlm2')
def recentlm2():
	cur = mysql.connect().cursor()
	cur.execute('select * from node_data ORDER BY id DESC LIMIT 1')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data' : r})

@app.route('/hour')
def hhistory():
	cur = mysql.connect().cursor()
	cur.execute('select * from node_data where timestamp >= DATE_SUB(NOW(),INTERVAL 1 HOUR)')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Last one hour' : r})

@app.route('/day')
def dhistory():
	cur = mysql.connect().cursor()
	cur.execute('select * from node_data where timestamp >= DATE_SUB(NOW(),INTERVAL 1 DAY)')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Last one day' : r})

@app.route('/month')
def mhistory():
        cur = mysql.connect().cursor()
        cur.execute('select * from node_data where timestamp >= DATE_SUB(NOW(),INTERVAL 1 MONTH)')
        r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
        return jsonify({'Last one month' : r})

@app.route('/year')
def yhistory():
        cur = mysql.connect().cursor()
        cur.execute('select * from node_data where timestamp >= DATE_SUB(NOW(),INTERVAL 1 YEAR)')
        r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
        return jsonify({'Last one year' : r})


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=1)

