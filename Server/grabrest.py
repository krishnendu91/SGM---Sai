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
#conn =pymysql.connect(database="AmritaSGM",user="root",password="amma",host="localhost")
#cur=conn.cursor()
#cur.execute("INSERT INTO server_data(nodeid, METER,v1, v2, v3, i1, i2, i3, w1,w2,w3,va1,va2,va3,var1,var2,var3,wh,vah,varh,wh1,wh2,wh3$
#conn.commit()
#conn.close()
print ("DB Dump success")
