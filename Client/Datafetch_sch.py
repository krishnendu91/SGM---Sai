#!/usr/bin/python
# Library for Schneider Poly phase meter Modbus
# Library returns all power parameters
#V1.0 June 12,2018
#Build: 2018-06-12-V1
#Code by Sai Shibu (AWNA/058/15)
#Copyrights AmritaWNA Smartgrid Tag
#ModBUS Communication between Schneider EM6436 Meter and Raspberry Pi


import time
import pymodbus 
import serial,utils,mqttservice
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder as payloadDecode
from pymodbus.payload import BinaryPayloadBuilder as builder

eth0,ip_wlan0,nodeId=utils.sysinfo()

def meter():
	client = ModbusClient(method ='rtu',port='/dev/ttyUSB0',timeout=0.05) 
	client.connect()
	A=client.read_holding_registers(3912,2,unit=1)
	A=valDecode(A)
	A1=client.read_holding_registers(3928,2,unit=1) 
	A1=valDecode(A1)
	A2=client.read_holding_registers(3942,2,unit=1) 
	A2=valDecode(A2)
	A3=client.read_holding_registers(3956,2,unit=1)
	A3=valDecode(A3)
	VLL=client.read_holding_registers(3908,2,unit=1) 
	VLL=valDecode(VLL)
	VLN=client.read_holding_registers(3910,2,unit=1)
	VLN=valDecode(VLN)
	V12=client.read_holding_registers(3924,2,unit=1)
	V12=valDecode(V12)
	V23=client.read_holding_registers(3938,2,unit=1) 
	V23=valDecode(V23)
	V31=client.read_holding_registers(3952,2,unit=1) 
	V31=valDecode(V31)
	V1=client.read_holding_registers(3926,2,unit=1) 
	V1=valDecode(V1)
	V2=client.read_holding_registers(3940,2,unit=1) 
	V2=valDecode(V2)
	V3=client.read_holding_registers(3954,2,unit=1) 
	V3=valDecode(V3)
	W=client.read_holding_registers(3902,2,unit=1) 
	W=valDecode(W)
	W1=client.read_holding_registers(3918,2,unit=1)  
	W1=valDecode(W1)
	W2=client.read_holding_registers(3932,2,unit=1)  
	W2=valDecode(W2)
	W3=client.read_holding_registers(3946,2,unit=1)
	W3=valDecode(W3)
	VA=client.read_holding_registers(3900,2,unit=1)
	VA=valDecode(VA)
	VA1=client.read_holding_registers(3916,2,unit=1) 
	VA1=valDecode(VA1)
	VA2=client.read_holding_registers(3930,2,unit=1) 
	VA2=valDecode(VA2)
	VA3=client.read_holding_registers(3944,2,unit=1) 
	VA3=valDecode(VA3)
	PF=client.read_holding_registers(3906,2,unit=1)
	PF=valDecode(PF)
	PF1=client.read_holding_registers(3922,2,unit=1) 
	PF1=valDecode(PF1)
	PF2=client.read_holding_registers(3936,2,unit=1) 
	PF2=valDecode(PF2)
	PF3=client.read_holding_registers(3950,2,unit=1) 
	PF3=valDecode(PF3)
	F=client.read_holding_registers(3914,2,unit=1)
	F=valDecode(F)
	VAH=client.read_holding_registers(3958,2,unit=1) 
	VAH=valDecode(VAH)
	WH=client.read_holding_registers(3960,2,unit=1) 
	WH=valDecode(WH)
	intr=client.read_holding_registers(3998,2,unit=1) 
	intr=valDecode(intr)
	data={'nodeId':nodeId,'A':A,'A1':A1,'A2':A2,'A3':A3,'VLL':VLL,'VLN':VLN,'V1':V1,'V2':V2,'V3':V3,'V12':V12,'V23':V23,'V31':V31,'W':W,'W1':W1,'W2':W2,'W3':W3,'VA':VA,'VA1':VA1,'VA2':VA2,'VA3':VA3,'PF':PF,'PF1':PF1,'PF2':PF2,'PF3':PF3,'F':F,'VAH':VAH,'WH':WH,'INTR':intr}
	return data

def valDecode(value_d):
	#print(value_d)
	value_d = payloadDecode.fromRegisters(value_d.registers, byteorder=Endian.Big)
	#print(value_d)
	value_d ={'float':value_d.decode_32bit_float(),}
	#print(value_d['float'])
	#for i, value in value_d.iteritems():
	 #     value=value
	return value_d['float']

schData=meter()
print(schData)
utils.todbsch(schData)
mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_sch_direct",schData,ip_wlan0)


