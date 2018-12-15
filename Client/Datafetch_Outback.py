#!/usr/bin/python

from datetime import datetime
import pymysql,json,mqttservice
from subprocess import check_output
from urllib.request import urlopen

scanoutput=check_output(["hostname -I"],shell=1)
ip_eth0=scanoutput.decode().split()[0]
ip_wlan0=scanoutput.decode().split()[1]
conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()

mate=urlopen('http://192.168.0.64/Dev_status.cgi?&Port=0')
mate=mate.read()
#print(mate)
mate=json.loads(mate.decode())
print(mate)

inv1= mate['devstatus']['ports'][0]
inv1['nodeid']=14
error=inv1['Error'][0]
warn=inv1['Warn'][0]
inv1['Error']=error
inv1['Warn']=warn
cur.execute("INSERT INTO inverterData(nodeid,type,port,battVoltage,aux,error,dev,vac1_in_l2,ac_input,vac_out_l2,inv_mode,inv_i_l2,warn,buy_i_l2,vac_in_l2,sell_i_l2,chg_i_l2,ac_mode) VALUES(%(nodeid)s,%(Type)s,%(Port)s,%(Batt_V)s,%(AUX)s,%(Error)s,%(Dev)s,%(VAC1_in_L2)s,%(AC_Input)s,%(VAC_out_L2)s,%(INV_mode)s,%(Inv_I_L2)s,%(Warn)s,%(Buy_I_L2)s,%(VAC2_in_L2)s,%(Sell_I_L2)s,%(Chg_I_L2)s,%(AC_mode)s);",inv1)
conn.commit()

inv2= mate['devstatus']['ports'][3]
inv2['nodeid']=14
error=inv2['Error'][0]
warn=inv2['Warn'][0]
inv2['Error']=error
inv2['Warn']=warn
cur.execute("INSERT INTO inverterData(nodeid,type,port,battVoltage,aux,error,dev,vac1_in_l2,ac_input,vac_out_l2,inv_mode,inv_i_l2,warn,buy_i_l2,vac_in_l2,sell_i_l2,chg_i_l2,ac_mode) VALUES(%(nodeid)s,%(Type)s,%(Port)s,%(Batt_V)s,%(AUX)s,%(Error)s,%(Dev)s,%(VAC1_in_L2)s,%(AC_Input)s,%(VAC_out_L2)s,%(INV_mode)s,%(Inv_I_L2)s,%(Warn)s,%(Buy_I_L2)s,%(VAC2_in_L2)s,%(Sell_I_L2)s,%(Chg_I_L2)s,%(AC_mode)s);",inv2)
conn.commit()

inv3= mate['devstatus']['ports'][5] #5
inv3['nodeid']=14
error=inv3['Error'][0]
warn=inv3['Warn'][0]
inv3['Error']=error
inv3['Warn']=warn
cur.execute("INSERT INTO inverterData(nodeid,type,port,battVoltage,aux,error,dev,vac1_in_l2,ac_input,vac_out_l2,inv_mode,inv_i_l2,warn,buy_i_l2,vac_in_l2,sell_i_l2,chg_i_l2,ac_mode) VALUES(%(nodeid)s,%(Type)s,%(Port)s,%(Batt_V)s,%(AUX)s,%(Error)s,%(Dev)s,%(VAC1_in_L2)s,%(AC_Input)s,%(VAC_out_L2)s,%(INV_mode)s,%(Inv_I_L2)s,%(Warn)s,%(Buy_I_L2)s,%(VAC2_in_L2)s,%(Sell_I_L2)s,%(Chg_I_L2)s,%(AC_mode)s);",inv3)
conn.commit()

cc1= mate['devstatus']['ports'][1]
cc1['nodeid']=14
error=cc1['Error'][0]
cc1['Error']=error
cur.execute("INSERT INTO inverterData(nodeid,type,port,battVoltage,aux,error,dev,cc_mode,aux_mode,in_i,out_i,in_v,out_kwh,out_ah ) VALUES(%(nodeid)s,%(Type)s,%(Port)s,%(Batt_V)s,%(AUX)s,%(Error)s,%(Dev)s,%(CC_mode)s,%(Aux_mode)s,%(In_I)s,%(Out_I)s,%(In_V)s,%(Out_kWh)s,%(Out_AH)s);",cc1)
conn.commit()

cc2= mate['devstatus']['ports'][2]
cc2['nodeid']=14
error=cc2['Error'][0]
cc2['Error']=error
cur.execute("INSERT INTO inverterData(nodeid,type,port,battVoltage,aux,error,dev,cc_mode,aux_mode,in_i,out_i,in_v,out_kwh,out_ah ) VALUES(%(nodeid)s,%(Type)s,%(Port)s,%(Batt_V)s,%(AUX)s,%(Error)s,%(Dev)s,%(CC_mode)s,%(Aux_mode)s,%(In_I)s,%(Out_I)s,%(In_V)s,%(Out_kWh)s,%(Out_AH)s);",cc2)
conn.commit()

cc3= mate['devstatus']['ports'][4]
cc3['nodeid']=14
error=cc3['Error'][0]
cc3['Error']=error
cur.execute("INSERT INTO inverterData(nodeid,type,port,battVoltage,aux,error,dev,cc_mode,aux_mode,in_i,out_i,in_v,out_kwh,out_ah ) VALUES(%(nodeid)s,%(Type)s,%(Port)s,%(Batt_V)s,%(AUX)s,%(Error)s,%(Dev)s,%(CC_mode)s,%(Aux_mode)s,%(In_I)s,%(Out_I)s,%(In_V)s,%(Out_kWh)s,%(Out_AH)s);",cc3)
conn.commit()
conn.close()
print("DB Dump success")
#mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch","DONE",ip_wlan0)
print("MQTT Success")
