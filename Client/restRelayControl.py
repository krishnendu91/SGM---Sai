#!/usr/bin/python
#!/usr/bin/python

from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
urls=("/favicon.ico","dummy")
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 

pins = {26 : {'name' : 'R1', 'state' : GPIO.LOW},
	19 : {'name' : 'R2', 'state' : GPIO.LOW},
	13 : {'name' : 'R3', 'state' : GPIO.LOW},
	6 : {'name' : 'R4', 'state' : GPIO.LOW},
	12 : {'name' : 'R5', 'state' : GPIO.LOW},
	16 : {'name' : 'R6', 'state' : GPIO.LOW},
	20 : {'name' : 'R7', 'state' : GPIO.LOW},
	21 : {'name' : 'R8', 'state' : GPIO.LOW}
   }

pinsID = {'R1' : {'gpio' : '26', 'state' : GPIO.LOW},
	'R2' : {'gpio' : '19', 'state' : GPIO.LOW},
	'R3' : {'gpio' : '13', 'state' : GPIO.LOW},
	'R4': {'gpio' : '6', 'state' : GPIO.LOW},
	'R5' : {'gpio' : '12', 'state' : GPIO.LOW},
	'R6' : {'gpio' : '16', 'state' : GPIO.LOW},
	'R7' : {'gpio' : '20', 'state' : GPIO.LOW},
	'R8' : {'gpio' : '21', 'state' : GPIO.LOW}
   }

for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)

@app.route('/')
def welcome():
	return "\tWelcome to Amrita Smart-Grid Middleware.\n\n \tKindly use one of the APIs to get data"

@app.route('/<pinId>/<state>')
def action(pinId, state):
	state=int(state)
	device=pinsID[pinId]['gpio']
	print(device)
	print(pinsID[pinId]['state'])
	
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=2000,debug=1)
