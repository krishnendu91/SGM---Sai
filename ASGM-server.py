#Import required libraries
import  urllib2,json,time


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
