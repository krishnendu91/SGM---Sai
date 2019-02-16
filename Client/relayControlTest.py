#!/usr/bin/python


import RPi.GPIO as GPIO
import time
R1=26
R2=19
R3=13
R4=6
R5=26
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

GPIO.output(R1,GPIO.HIGH)
time.sleep(1)
GPIO.output(R1,GPIO.LOW)
time.sleep(1)
print("R1 TEST success")

GPIO.output(R2,GPIO.HIGH)
time.sleep(1)
GPIO.output(R2,GPIO.LOW)
time.sleep(1)
print("R2 TEST success")

GPIO.output(R3,GPIO.HIGH)
time.sleep(1)
GPIO.output(R3,GPIO.LOW)
time.sleep(1)
print("R3 TEST success")

GPIO.output(R4,GPIO.HIGH)
time.sleep(1)
GPIO.output(R4,GPIO.LOW)
time.sleep(1)
print("R4 TEST success")

GPIO.output(R5,GPIO.HIGH)
time.sleep(1)
GPIO.output(R5,GPIO.LOW)
time.sleep(1)
print("R5 TEST success")

GPIO.output(R6,GPIO.HIGH)
time.sleep(1)
GPIO.output(R6,GPIO.LOW)
time.sleep(1)
print("R6 TEST success")

GPIO.output(R7,GPIO.HIGH)
time.sleep(1)
GPIO.output(R7,GPIO.LOW)
time.sleep(1)
print("R7 TEST success")

GPIO.output(R8,GPIO.HIGH)
time.sleep(1)
GPIO.output(R8,GPIO.LOW)
time.sleep(1)
print("R8 TEST success")
