#!/usr/bin/python3

#Import required libraries
import json,time,pymysql
import sys
from urllib.request import urlopen
#Define a page opener using inbuilt function from urllib2
#opener=urllib2.build_opener()
api=""

def todb(data,dev):
  conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
  cur=conn.cursor()
  if dev==1:
    cur.execute("INSERT INTO nodeData(meterId,nodeId,meterType,V1, V2, V3, I1, I2, I3,F1,F2,F3,PF1,PF2,PF3,W1,W2,W3,VA1,VA2,VA3,VAR1,VAR2,VAR3,WH,VAH,VARH,WH1,WH2,WH3,VAH1,VAH2,VAH3,VARH1,VARH2,VARH3,D1,D2,D3,D4,D5,D6,D7,D8)VALUES( %(meterId)s,%(nodeId)s,%(meterType)s,%(V1)s,%(V2)s,%(V3)s,%(I1)s,%(I2)s,%(I3)s,%(F1)s,%(F2)s,%(F3)s,%(PF1)s,%(PF2)s,%(PF3)s,%(W1)s,%(W2)s,%(W3)s,%(VA1)s,%(VA2)s,%(VA3)s,%(VAR1)s,%(VAR2)s,%(VAR3)s,%(WH)s,%(VAH)s,%(VARH)s,%(WH1)s,%(WH2)s,%(WH3)s,%(VAH1)s,%(VAH2)s,%(VAH3)s,%(VARH1)s,%(VARH2)s,%(VARH3)s,%(D1)s,%(D2)s,%(D3)s,%(D4)s,%(D5)s,%(D6)s,%(D7)s,%(D8)s);",data)
   # print('todb')
   # print(data)
  elif dev==41:
    cur.execute("INSERT INTO inverterData(nodeid,type,port,battVoltage,aux,error,dev,vac1_in_l2,ac_input,vac_out_l2,inv_mode,inv_i_l2,warn,buy_i_l2,vac_in_l2,sell_i_l2,chg_i_l2,ac_mode) VALUES(%(nodeid)s,%(Type)s,%(Port)s,%(Batt_V)s,%(AUX)s,%(Error)s,%(Dev)s,%(VAC1_in_L2)s,%(AC_Input)s,%(VAC_out_L2)s,%(INV_mode)s,%(Inv_I_L2)s,%(Warn)s,%(Buy_I_L2)s,%(VAC2_in_L2)s,%(Sell_I_L2)s,%(Chg_I_L2)s,%(AC_mode)s);",data)
  elif dev==42:
    cur.execute("INSERT INTO inverterData(nodeid,type,port,battVoltage,aux,error,dev,cc_mode,aux_mode,in_i,out_i,in_v,out_kwh,out_ah ) VALUES(%(nodeid)s,%(Type)s,%(Port)s,%(Batt_V)s,%(AUX)s,%(Error)s,%(Dev)s,%(CC_mode)s,%(Aux_mode)s,%(In_I)s,%(Out_I)s,%(In_V)s,%(Out_kWh)s,%(Out_AH)s);",data)
  elif dev==0:
    cur.execute("SELECT id FROM weather ORDER BY id DESC LIMIT 1")
    weatherID=cur.fetchall()
    weatherID=weatherID[0]
    weatherID=weatherID[0]
    cur.execute("INSERT INTO `event` (nodeId,meterId, errorId, errorMsg, errorVal,errorTime,weatherID) VALUES(%(nodeId)s,%(meterId)s,%(errorId)s,%(errorMsg)s,%(errorVal)s,%(errorTime)s,%(weatherID)s);",data)
  elif dev==100:
    cur.execute("INSERT INTO nodeHealth(nodeId,alive,temp,SSID,wlan_ss) VALUES(%(nodeid)s,%(alive)s,%(temp)s,%(ssid)s,%(ss)s);",data)
  elif dev==101:
    cur.execute("INSERT INTO switchState(nodeId,C1,C2,C3,C4) VALUES(%(nodeid)s,%(C1)s,%(C2)s,%(C3)s,%(C4)s);",data)
  elif dev==102:
    cur.execute("INSERT INTO nodeHealth(aggId,alive,temp,SSID,wlan_ss) VALUES(%(aggId)s,%(alive)s,%(temp)s,%(ssid)s,%(ss)s);",data)
  elif dev==2:
    cur.execute("INSERT INTO maximData(nodeid,v1,i1, w1,va1,var1,wh1,vah1,varh1,pf1,f1) VALUES(%(nodeId)s,%(v1)s,%(i1)s,%(w1)s,%(va1)s,%(var1)s,%(wh1)s,%(vah1)s,%(varh1)s,%(pf1)s,%(f1)s);",data)
  elif dev==3:
    cur.execute("INSERT INTO schData(nodeId, A, A1, A2, A3, VLL, VLN, V1, V2, V3, V12, V23, V31, F, PF, PF1, PF2, PF3, W, W1, W2, W3, VA, VA1, VA2, VA3, WH, VAH, INTR) VALUES (%(nodeId)s, %(A)s, %(A1)s, %(A2)s, %(A3)s, %(VLL)s, %(VLN)s, %(V1)s, %(V2)s, %(V3)s, %(V12)s, %(V23)s, %(V31)s, %(F)s, %(PF)s, %(PF1)s, %(PF2)s, %(PF3)s, %(W)s, %(W1)s, %(W2)s, %(W3)s, %(VA)s, %(VA1)s, %(VA2)s, %(VA3)s, %(WH)s, %(VAH)s, %(INTR)s);",data)
  elif dev==103:
    cur.execute("INSERT INTO switchState(nodeId,C1,C2,C3,C4) VALUES(%(nodeid)s,%(C1)s,%(C2)s,%(C3)s,%(C4)s);",data)
  elif dev==4:
    cur.execute("INSERT INTO STPData(nodeId,meterId,A, A1, A2, A3, VLL, VLN, V1, V2, V3, V12, V23, V31, F, PF, PF1, PF2, PF3, W, W1, W2, W3, VA, VA1, VA2, VA3, WH, VAH, INTR) VALUES (%(nodeId)s,%(meterId)s ,%(A)s, %(A1)s, %(A2)s, %(A3)s, %(VLL)s, %(VLN)s, %(V1)s, %(V2)s, %(V3)s, %(V12)s, %(V23)s, %(V31)s, %(F)s, %(PF)s, %(PF1)s, %(PF2)s, %(PF3)s, %(W)s, %(W1)s, %(W2)s, %(W3)s, %(VA)s, %(VA1)s, %(VA2)s, %(VA3)s, %(WH)s, %(VAH)s, %(INTR)s);",data)
  else:
    print("none")

  cur.close()
  conn.commit()
  conn.close()
  print ("DB Dump success")
