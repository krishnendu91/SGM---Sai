# Library for Schneider Poly phase meter Modbus
# Library returns all power parameters
#V1.0 June 12,2018
#Build: 2018-06-12-V1
#Code by Sai Shibu (AWNA/058/15)
#Copyrights AmritaWNA Smartgrid Tag
#ModBUS Communication between Schneider EM6436 Meter and Raspberry Pi


import time
import pymodbus 
import serial
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder as decode
from pymodbus.payload import BinaryPayloadBuilder as builder

def meter():
	client = ModbusClient(method ='rtu',port='/dev/ttyUSB0',timeout=0.05) 
	client.connect()
	A=client.read_holding_registers(3912,2,unit=1)
	A=decode(A)
	A1=client.read_holding_registers(3928,2,unit=1) 
	A1=decode(A1)
	A2=client.read_holding_registers(3942,2,unit=1) 
	A2=decode(A2)
	A3=client.read_holding_registers(3956,2,unit=1)
	A3=decode(A3)
	VLL=client.read_holding_registers(3908,2,unit=1) 
	VLL=decode(VLL)
	VLN=client.read_holding_registers(3910,2,unit=1)
	VLN=decode(VLN)
	V12=client.read_holding_registers(3924,2,unit=1)
	V12=decode(V12)
	V23=client.read_holding_registers(3938,2,unit=1) 
	V23=decode(V23)
	V31=client.read_holding_registers(3952,2,unit=1) 
	V31=decode(V31)
	V1=client.read_holding_registers(3926,2,unit=1) 
	V1=decode(V1)
	V2=client.read_holding_registers(3940,2,unit=1) 
	V2=decode(V2)
	V3=client.read_holding_registers(3954,2,unit=1) 
	V3=decode(V3)
	W=client.read_holding_registers(3902,2,unit=1) 
	W=decode(W)
	W1=client.read_holding_registers(3918,2,unit=1)  
	W1=decode(W1)
	W2=client.read_holding_registers(3932,2,unit=1)  
	W2=decode(W2)
	W3=client.read_holding_registers(3946,2,unit=1)
	W3=decode(W3)
	VA=client.read_holding_registers(3900,2,unit=1)
	VA=decode(VA)
	VA1=client.read_holding_registers(3916,2,unit=1) 
	VA1=decode(VA1)
	VA2=client.read_holding_registers(3930,2,unit=1) 
	VA2=decode(VA2)
	VA3=client.read_holding_registers(3944,2,unit=1) 
	VA3=decode(VA3)
	PF=client.read_holding_registers(3906,2,unit=1)
	PF=decode(PF)
	PF1=client.read_holding_registers(3922,2,unit=1) 
	PF1=decode(PF1)
	PF2=client.read_holding_registers(3936,2,unit=1) 
	PF2=decode(PF2)
	PF3=client.read_holding_registers(3950,2,unit=1) 
	PF3=decode(PF3)
	F=client.read_holding_registers(3914,2,unit=1)
	F=decode(F)
	VAH=client.read_holding_registers(3958,2,unit=1) 
	VAH=decode(VAH)
	WH=client.read_holding_registers(3960,2,unit=1) 
	WH=decode(WH)
	intr=client.read_holding_registers(3998,2,unit=1) 
	intr=decode(intr)
	data={'A':A,'A1':A1,'A2':A2,'A3':A3,'VLL':VLL,'VLN':VLN,'V1':V1,'V2':V2,'V3':V3,'V12':V12,'V23':V23,'V31':V31,'W':W,'W1':W1,'W2':W2,'W3':W3,'VA':VA,'VA1':VA1,'VA2':VA2,'VA3':VA3,'PF':PF,'PF1':PF1,'PF2:PF2,'PF3':PF3,'F':F,'VAH':VAH,'WH':WH,'intr':intr}
	return data

def decode(value):
	value_d = decode.fromRegisters(value.registers, endian=Endian.Little)
	value_d ={'float':A_d.decode_32bit_float(),}
	for i, value in value_d.iteritems():
	      value=value
	return value
