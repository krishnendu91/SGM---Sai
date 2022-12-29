#!/usr/bin/python3
# Synthetic Data to generate smartbuilding data

import pymysql,random


conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()

WSB = 1
User = random.randint(1,3)
Load1 = random.randint(0,1)
Load2 = random.randint(0,1)

if Load1 ==1:
  Load1Power = 20
else:
  Load1Power = 0
if Load2 ==1: 
  Load2Power = random.randint(10,100)
else:
  Load2Power = 0

WSBPower = Load1+Load2
User1Avg = random.randint(0,100)
User2Avg = random.randint(0,100)
User3Avg = random.randint(0,100)

data = {"WSB":WSB,"User":User,"Load1":Load1,"Load2":Load2, "Load1Power":Load1Power, "Load2Power":Load2Power, "WSBPower":WSBPower,"User1Avg":User1Avg,"User2Avg":User2Avg,"User3Avg":User3Avg}
print(data)

cur.execute("INSERT INTO `SmartBuildingSynt` (`WSB`, `User`, `Load1`, `Load2`, `Load1Power`, `Load2Power`, `WSBPower`, `User1Avg`, `User2Avg`, `User3Avg`) VALUES (%(WSB)s, %(User)s, %(Load1)s, %(Load2)s, %(Load1Power)s, %(Load2Power)s, %(WSBPower)s, %(User1Avg)s, %(User2Avg)s, %(User3Avg)s);",data)
conn.commit()
conn.close()
