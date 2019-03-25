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
import serial,utils
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder as payloadDecode
from pymodbus.payload import BinaryPayloadBuilder as builder

eth0,nodeId=utils.sysinfo()
if nodeId=='STP1':
	metercount=6
elif nodeId=='STP2':
	metercount=4
else:
	metercount=2

def meter(meterId):
	meterName=utils.meterinfo(nodeId,meterId)
	print(meterName)
	meterId=int(meterId)
	#meterId=5
	client = ModbusClient(method ='rtu',port='/dev/ttyUSB0',timeout=3) 
	C_connected=client.connect()
	client.debug_enabled()
	if C_connected:
		print("Device Connected successfully. Device ID="+str(meterId) + "for: " +str(meterName))
		A=client.read_holding_registers(3912,2,unit=meterId)
		A=valDecode(A)
		A1=client.read_holding_registers(3928,2,unit=meterId) 
		A1=valDecode(A1)
		A2=client.read_holding_registers(3942,2,unit=meterId) 
		A2=valDecode(A2)
		A3=client.read_holding_registers(3956,2,unit=meterId)
		A3=valDecode(A3)
		VLL=client.read_holding_registers(3908,2,unit=meterId) 
		VLL=valDecode(VLL)
		VLN=client.read_holding_registers(3910,2,unit=meterId)
		VLN=valDecode(VLN)
		V12=client.read_holding_registers(3924,2,unit=meterId)
		V12=valDecode(V12)
		V23=client.read_holding_registers(3938,2,unit=meterId) 
		V23=valDecode(V23)
		V31=client.read_holding_registers(3952,2,unit=meterId) 
		V31=valDecode(V31)
		V1=client.read_holding_registers(3926,2,unit=meterId) 
		V1=valDecode(V1)
		V2=client.read_holding_registers(3940,2,unit=meterId) 
		V2=valDecode(V2)
		V3=client.read_holding_registers(3954,2,unit=meterId) 
		V3=valDecode(V3)
		W=client.read_holding_registers(3902,2,unit=meterId) 
		W=valDecode(W)
		W1=client.read_holding_registers(3918,2,unit=meterId)  
		W1=valDecode(W1)
		W2=client.read_holding_registers(3932,2,unit=meterId)  
		W2=valDecode(W2)
		W3=client.read_holding_registers(3946,2,unit=meterId)
		W3=valDecode(W3)
		VA=client.read_holding_registers(3900,2,unit=meterId)
		VA=valDecode(VA)
		VA1=client.read_holding_registers(3916,2,unit=meterId) 
		VA1=valDecode(VA1)
		VA2=client.read_holding_registers(3930,2,unit=meterId) 
		VA2=valDecode(VA2)
		VA3=client.read_holding_registers(3944,2,unit=meterId) 
		VA3=valDecode(VA3)
		PF=client.read_holding_registers(3906,2,unit=meterId)
		PF=valDecode(PF)
		PF1=client.read_holding_registers(3922,2,unit=meterId) 
		PF1=valDecode(PF1)
		PF2=client.read_holding_registers(3936,2,unit=meterId) 
		PF2=valDecode(PF2)
		PF3=client.read_holding_registers(3950,2,unit=meterId) 
		PF3=valDecode(PF3)
		F=client.read_holding_registers(3914,2,unit=meterId)
		F=valDecode(F)
		VAH=client.read_holding_registers(3958,2,unit=meterId) 
		VAH=valDecode(VAH)
		WH=client.read_holding_registers(3960,2,unit=meterId) 
		WH=valDecode(WH)
		intr=client.read_holding_registers(3998,2,unit=meterId) 
		intr=valDecode(intr)
		data={'nodeId':nodeId,'meterName':meterName,'meterId':meterId,'A':A,'A1':A1,'A2':A2,'A3':A3,'VLL':VLL,'VLN':VLN,'V1':V1,'V2':V2,'V3':V3,'V12':V12,'V23':V23,'V31':V31,'W':W,'W1':W1,'W2':W2,'W3':W3,'VA':VA,'VA1':VA1,'VA2':VA2,'VA3':VA3,'PF':PF,'PF1':PF1,'PF2':PF2,'PF3':PF3,'F':F,'VAH':VAH,'WH':WH,'INTR':intr}
		return data
	else:
		print("Error Connecting to Device")
		quit()
def valDecode(value_d):
	#print(value_d)
	try:
		value_d = payloadDecode.fromRegisters(value_d.registers, byteorder=Endian.Big)
	#print(value_d)
		value_d ={'float':value_d.decode_32bit_float(),}
	#print(value_d['float'])
	#for i, value in value_d.iteritems():
	 #     value=value
	except:
		pass
	return value_d['float']

#ETP1 has 6 Meters
i=1
while i<=metercount:
	schData=meter(i)
	print(schData)
	utils.todbsch(schData)
	utils.mqtt_publish("datafetch_stp_direct",schData)
	print("Push to Server complete")
	i=i+1
	time.sleep(3)
