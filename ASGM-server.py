#Import required libraries
import  urllib2,json,time,pymysql


#Define a page opener using inbuilt function from urllib2
opener=urllib2.build_opener()
#Define the url (http://<node ip>:5000/api)
url='http://192.168.179.231:5000/recent'
#Read the url and save to a variable
api_page=opener.open(url)
#Read the api output from the variable 
api=api_page.read()
#Optional: Convert the output to json
json_api=json.loads(api)
#Optional: Print required data
print 'voltage1: '+str(json_api['Recent data'][-1]['v1']) +'V'
print 'voltage2: '+str(json_api['Recent data'][-1]['v2']) +'V'
print 'voltage3: '+str(json_api['Recent data'][-1]['v3']) +'V'

#insert to DB (requires pymysql package (pip install pymysql))
conn =pymysql.connect(database="AmritaSGM",user="root",password="amma",host="localhost")
cur=conn.cursor()
cur.execute("INSERT INTO node_data(nodeid, METER,v1, v2, v3, i1, i2, i3, w1,w2,w3,va1,va2,va3,var1,var2,var3,wh,vah,varh,wh1,wh2,wh3,v$
conn.commit()
conn.close()
print "DB Dump success"
