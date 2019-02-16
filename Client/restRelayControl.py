#!/usr/bin/python
#!/usr/bin/python

from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
urls=("/favicon.ico","dummy")
import RPi.GPIO as GPIO
import time
R1=26
R2=19
R3=13
R4=6
R5=12
R6=16
R7=20
R8=21
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(R1,GPIO.OUT)
GPIO.setup(R2,GPIO.OUT)
GPIO.setup(R3,GPIO.OUT)
GPIO.setup(R4,GPIO.OUT)
GPIO.setup(R5,GPIO.OUT)
GPIO.setup(R6,GPIO.OUT)
GPIO.setup(R7,GPIO.OUT)
GPIO.setup(R8,GPIO.OUT)

@app.route('/')
def welcome():
	return "\tWelcome to Amrita Smart-Grid Middleware.\n\n \tKindly use one of the APIs to get data"


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=2000,debug=1)
