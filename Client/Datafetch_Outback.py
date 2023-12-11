#!/usr/bin/python

from datetime import datetime
import time
import pymysql,json,mqttservice
from subprocess import check_output
from urllib.request import urlopen

#This line uses the check_output function to run the shell command "hostname -I" and captures the command's output. The shell=1 argument indicates that the command should be executed in a shell.
scanoutput=check_output(["hostname -I"],shell=1)

#These lines decode the output from the previous shell command, split it into a list of words, and assign the first and second words to the variables ip_eth0 and ip_wlan0, respectively. This is used to obtain the IP addresses.
ip_eth0=scanoutput.decode().split()[0]
ip_wlan0=scanoutput.decode().split()[1]

#These lines establish a connection to a MySQL database named "AmritaSGM" using the pymysql library. It also creates a cursor object (cur) for executing SQL queries.
conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()

#These lines use the urlopen function to fetch data from the URL 'http://192.168.0.64/Dev_status.cgi?&Port=0'. The retrieved data is then read and stored in the mate variable.
mate=urlopen('http://192.168.0.64/Dev_status.cgi?&Port=0')
mate=mate.read()
#print(mate)

#This line decodes the JSON data stored in the mate variable, converting it into a Python dictionary. This data likely contains information about devices.
mate=json.loads(mate.decode())
#This line prints the message "Connected to Inverter" to the console.
print("Connected to Inverter")
#print(mate)

#These lines extract data from the mate dictionary. It appears to be related to an inverter device. The device's node ID is set to 14.
inv1= mate['devstatus']['ports'][0]
inv1['nodeid']=14

#These lines extract and assign values to variables error and warn from the inv1 dictionary. These variables are then assigned back to the inv1 dictionary with the same keys.
error=inv1['Error'][0]
warn=inv1['Warn'][0]
inv1['Error']=error
inv1['Warn']=warn

#This line uses the execute method of the cursor (cur) to execute an SQL INSERT statement. It inserts data from the inv1 dictionary into the "inverterData" table in the MySQL database.
cur.execute("INSERT INTO inverterData(nodeid,type,port,battVoltage,aux,error,dev,vac1_in_l2,ac_input,vac_out_l2,inv_mode,inv_i_l2,warn,buy_i_l2,vac_in_l2,sell_i_l2,chg_i_l2,ac_mode) VALUES(%(nodeid)s,%(Type)s,%(Port)s,%(Batt_V)s,%(AUX)s,%(Error)s,%(Dev)s,%(VAC1_in_L2)s,%(AC_Input)s,%(VAC_out_L2)s,%(INV_mode)s,%(Inv_I_L2)s,%(Warn)s,%(Buy_I_L2)s,%(VAC2_in_L2)s,%(Sell_I_L2)s,%(Chg_I_L2)s,%(AC_mode)s);",inv1)
#This line commits the changes made to the database, making them permanent.
conn.commit()

#This line seems to publish data using MQTT. It sends data from the inv1 dictionary to the MQTT broker located at IP address "192.168.112.110" on port 1883.
mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_outback_inv_direct",inv1,ip_wlan0)
print("MQTT Success for inv1")
time.sleep(0.5)

#The code continues with similar patterns for inv2, inv3, cc1, cc2, and cc3, fetching data, inserting it into the database, and publishing it via MQTT.
inv2= mate['devstatus']['ports'][3]
inv2['nodeid']=14
error=inv2['Error'][0]
warn=inv2['Warn'][0]
inv2['Error']=error
inv2['Warn']=warn
cur.execute("INSERT INTO inverterData(nodeid,type,port,battVoltage,aux,error,dev,vac1_in_l2,ac_input,vac_out_l2,inv_mode,inv_i_l2,warn,buy_i_l2,vac_in_l2,sell_i_l2,chg_i_l2,ac_mode) VALUES(%(nodeid)s,%(Type)s,%(Port)s,%(Batt_V)s,%(AUX)s,%(Error)s,%(Dev)s,%(VAC1_in_L2)s,%(AC_Input)s,%(VAC_out_L2)s,%(INV_mode)s,%(Inv_I_L2)s,%(Warn)s,%(Buy_I_L2)s,%(VAC2_in_L2)s,%(Sell_I_L2)s,%(Chg_I_L2)s,%(AC_mode)s);",inv2)
conn.commit()
mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_outback_inv_direct",inv2,ip_wlan0)
print("MQTT Success for inv2")
time.sleep(0.5)

inv3= mate['devstatus']['ports'][5] #5
inv3['nodeid']=14
error=inv3['Error'][0]
warn=inv3['Warn'][0]
inv3['Error']=error
inv3['Warn']=warn
cur.execute("INSERT INTO inverterData(nodeid,type,port,battVoltage,aux,error,dev,vac1_in_l2,ac_input,vac_out_l2,inv_mode,inv_i_l2,warn,buy_i_l2,vac_in_l2,sell_i_l2,chg_i_l2,ac_mode) VALUES(%(nodeid)s,%(Type)s,%(Port)s,%(Batt_V)s,%(AUX)s,%(Error)s,%(Dev)s,%(VAC1_in_L2)s,%(AC_Input)s,%(VAC_out_L2)s,%(INV_mode)s,%(Inv_I_L2)s,%(Warn)s,%(Buy_I_L2)s,%(VAC2_in_L2)s,%(Sell_I_L2)s,%(Chg_I_L2)s,%(AC_mode)s);",inv3)
conn.commit()
mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_outback_inv_direct",inv3,ip_wlan0)
print("MQTT Success for INV3")
time.sleep(0.5)

cc1= mate['devstatus']['ports'][1]
cc1['nodeid']=14
error=cc1['Error'][0]
cc1['Error']=error
cur.execute("INSERT INTO inverterData(nodeid,type,port,battVoltage,aux,error,dev,cc_mode,aux_mode,in_i,out_i,in_v,out_kwh,out_ah ) VALUES(%(nodeid)s,%(Type)s,%(Port)s,%(Batt_V)s,%(AUX)s,%(Error)s,%(Dev)s,%(CC_mode)s,%(Aux_mode)s,%(In_I)s,%(Out_I)s,%(In_V)s,%(Out_kWh)s,%(Out_AH)s);",cc1)
conn.commit()
mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_outback_cc_direct",cc1,ip_wlan0)
print("MQTT Success for CC1")
time.sleep(0.5)
 
cc2= mate['devstatus']['ports'][2]
cc2['nodeid']=14
error=cc2['Error'][0]
cc2['Error']=error
cur.execute("INSERT INTO inverterData(nodeid,type,port,battVoltage,aux,error,dev,cc_mode,aux_mode,in_i,out_i,in_v,out_kwh,out_ah ) VALUES(%(nodeid)s,%(Type)s,%(Port)s,%(Batt_V)s,%(AUX)s,%(Error)s,%(Dev)s,%(CC_mode)s,%(Aux_mode)s,%(In_I)s,%(Out_I)s,%(In_V)s,%(Out_kWh)s,%(Out_AH)s);",cc2)
conn.commit()
mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_outback_cc_direct",cc2,ip_wlan0)
print("MQTT Success for CC2")
time.sleep(0.5)

cc3= mate['devstatus']['ports'][4]
cc3['nodeid']=14
error=cc3['Error'][0]
cc3['Error']=error
cur.execute("INSERT INTO inverterData(nodeid,type,port,battVoltage,aux,error,dev,cc_mode,aux_mode,in_i,out_i,in_v,out_kwh,out_ah ) VALUES(%(nodeid)s,%(Type)s,%(Port)s,%(Batt_V)s,%(AUX)s,%(Error)s,%(Dev)s,%(CC_mode)s,%(Aux_mode)s,%(In_I)s,%(Out_I)s,%(In_V)s,%(Out_kWh)s,%(Out_AH)s);",cc3)
conn.commit()
conn.close()
mqttservice.mqtt_publish("192.168.112.110",1883,"datafetch_outback_cc_direct",cc3,ip_wlan0)
print("DB Dump success")
print("MQTT Success for CC3")
