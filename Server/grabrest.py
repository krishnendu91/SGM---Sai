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
cur.execute("INSERT INTO nodeData(nodeId,meterType,v1, v2, v3, i1, i2, i3, w1,w2,w3,va1,va2,va3,var1,var2,var3,wh,vah,varh,wh1,wh2,wh3,vah1,vah2,vah3,varh1,varh2,varh3,D1,D2,D3,D4,D5,D6,D7,D8)VALUES(%(nodeId)s,%(meterType)s,%(v1)s,%(v2)s,%(v3)s,%(i1)s,%(i2)s,%(i3)s,%(w1)s,%(w2)s,%(w3)s,%(va1)s,%(va2)s,%(va3)s,%(var1)s,%(var2)s,%(var3)s,%(wh)s,%(vah)s,%(varh)s,%(wh1)s,%(wh2)s,%(wh3)s,%(vah1)s,%(vah2)s,%(vah3)s,%(varh1)s,%(varh2)s,%(varh3)s,%(pf1)s,%(pf2)s,%(pf3)s,%(f1)s,%(f2)s,%(f3)s,%(D1)s,%(D2)s,%(D3)s,%(D4)s,%(D5)s,%(D6)s,%(D7)s,%(D8)s);",data)
conn.commit()
conn.close()
print ("DB Dump success")
#value=json.dumps(value)



conn.commit()
conn.close()
print ("DB Dump success")
