#!/bin/python3
import os,time
from urllib.request import urlopen

cmd="/home/cs/restartRest.sh"
os.system(cmd)
time.sleep(0.5)

nodeId={'1':{'url':"http://192.168.179.231:5000/"},'2':{'url':"http://192.168.179.232:5000/"},'3':{'url':"http://192.168.179.233:5000/"},
  '4':{'url':"http://192.168.179.234:5000/"},
  '5':{'url':"http://192.168.179.235:5000/"},
  '6':{'url':"http://192.168.179.236:5000/"},
  '7':{'url':"http://192.168.179.237:5000/"},
  '8':{'url':"http://192.168.179.238:5000/"},
  '9':{'url':"http://192.168.179.239:5000/"},
  '10':{'url':"http://192.168.179.240:5000/"},
  '11':{'url':"http://192.168.179.241:5000/"},
  '12':{'url':"http://192.168.179.242:5000/"},
  '13':{'url':"http://192.168.179.243:5000/"},}

for url in nodeId:
  
  openurl(url)

def openurl(sURL):
        try:    
                api_page = urlopen(sURL) #Python 3
                api=api_page.read()
                message=str(api)
        except:
                pass
                message="Error accessing URL \n " 
        print(str(sURL)+message)
