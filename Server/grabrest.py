#!/usr/bin/python
#Import required libraries
import json,time,pymysql
import sys
from urllib.request import urlopen
#Define a page opener using inbuilt function from urllib2
#opener=urllib2.build_opener()

#Define the url (http://<node ip>:5000/api)
ip=sys.argv[1]
api_req=sys.argv[2]
url='http://'+str(ip)+':5000/'+str(api_req)
print (url)
#Read the url and save to a variable
# api_page=opener.open(url) For Python 2
api_page = urlopen(url) #Python 3
#Read the api output from the variable 
api=api_page.read()

#Optional: Convert the output to json
json_api=json.loads(api)
data= json_api['Recent data'][-1]

#Optional: Print required data
print ("Website grabbed")
print (data)

#insert to DB (Requires pymysql package) (install it by sudo pip pymysql)
conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()
cur.execute("INSERT INTO nodeData(nodeId,meterType,v1, v2, v3, i1, i2, i3, w1,w2,w3,va1,va2,va3,var1,var2,var3,wh,vah,varh,wh1,wh2,wh3,vah1,vah2,vah3,varh1,varh2,varh3,D1,D2,D3,D4,D5,D6,D7,D8)VALUES(%(nodeId)s,%(meterType)s,%(V1)s,%(V2)s,%(V3)s,%(I1)s,%(I2)s,%(I3)s,%(W1)s,%(W2)s,%(W3)s,%(VA1)s,%(VA2)s,%(VA3)s,%(VAR1)s,%(VAR2)s,%(VAR3)s,%(WH)s,%(VAH)s,%(VARH)s,%(WH1)s,%(WH2)s,%(WH3)s,%(VAH1)s,%(VAH2)s,%(VAH3)s,%(VARH1)s,%(VARH2)s,%(VARH3)s,%(PF1)s,%(PF2)s,%(PF3)s,%(F1)s,%(F2)s,%(F3)s,%(D1)s,%(D2)s,%(D3)s,%(D4)s,%(D5)s,%(D6)s,%(D7)s,%(D8)s);",data)
conn.commit()
conn.close()
print ("DB Dump success")
#value=json.dumps(value)



conn.commit()
conn.close()
print ("DB Dump success")
