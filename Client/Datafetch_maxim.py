#Libary file to read maxim Zon series ev kit
#Build: 2018-05-15-V1
#decoding by Sreevalsa

import serial,time,re,operator,math
def zon():
	port=serial.Serial("/dev/ttyUSB0",baudrate=9600,timeout=.1)
	testarr=[]
	cmnd1='m'
	cmnd2=0

	cmnd=cmnd1+str(cmnd2)
	j=0
	for i in range(9):
		port.write(cmnd)
		port.write("\r")
		rcv =port.read(90)
		rcv=rcv.replace('L1','')
		l=list(rcv)
		if cmnd2<10:
			l[0:2]=[]
		if cmnd2>9:
			l[0:3]=[]
		rcv="".join(l)
		cmnd2+=1
  
  		if cmnd2 == 4
			cmnd2=6
		elif cmnd2 ==8:
			cmnd2=11
		elif cmnd2 ==12:
			cmnd2=15
		elif cmnd2==17:
			cmnd2=0
	cmnd=cmnd1+str(cmnd2)
	g=map(lambda v: float(v) if '.' in v else int(v),re.findall(r'\d+(?:\.\d+)?',rcv))
	testarr.append(g)
	test = reduce(operator.add, testarr)
#meter data stored in variables
	m0_data=test[0]
	m1_data=test[1]
	m2_data=test[2]
	m3_data=test[3]
	m6_data=test[4]
	m7_data=test[5]
	m11_data=test[6]
	m15_data=test[7]
	m16_data=test[8]
	
  
  #power calculation in real time
	realpower=m15_data*m16_data*m11_data
	if (m11_data<1):
		reactivepower=m15_data*m16_data*(math.sin(math.acos(m11_data)))       
	else:
		reactivepower=0

	apparentpower=m15_data*m16_data
	zon_data={'Meter':m0_data,'temp':m1_data,'f':m2_data,'P_eng':m3_data,'Q_eng':m6_data,'S_eng':m7_data,'pf':m11_data,'I':m15_data,'V':m16_data,'P_pwr':realpower,'Q_pwr':reactivepower,'S_pwr':apparentpower}
	return zon_data
