#!/usr/bin/python3
import os,time
from urllib.request import urlopen

i=1
while i<14:
	if i<10:
		url="http://192.168.179.23"+str(i)+":5000/restart"
	elif i==10:
                url="http://192.168.179.240:5000/restart"
	elif i==11:
                url="http://192.168.179.241:5000/restart"
	elif i==12:
                url="http://192.168.179.242:5000/restart"
	elif i==13:
                url="http://192.168.179.243:5000/restart"
	else:
		pass
	openurl(url)
	i=i+1
cmd="/home/cs/restartRest.sh"
os.system(cmd)


def openurl(sURL):
        try:    
                api_page = urlopen(sURL) #Python 3
                api=api_page.read()
                message=str(api)
        except:
                pass
                message="Error accessing URL \n "
	time.sleep(0.5)
	print(str(sURL)+message)
