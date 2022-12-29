
#!/usr/bin/python3
# Synthetic Data to generate anomaly

import pymysql,random


conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()

Power = random.uniform(0.0,1500.0)

if Power == 0:
  powerTheft=0
  lineFault=1
  tieline=1
else: 
  powerTheft=0
  lineFault=0
  tieline=0

if Power >800:
  powerTheft=1
  lineFault=0
  tieline=0
else:
  powerTheft=0
  lineFault=0
  tieline=0
  
data={"Power":Power,"powerTheft":powerTheft,"lineFault":lineFault,"tieline":tieline}
print(data)

cur.execute("INSERT INTO `anomalySynt` (`lineFault`, `powerTheft`, `Power`, `tieline`) VALUES (%(lineFault)s, %(powerTheft)s, %(Power)s, %(tieline)s);",data)
conn.commit()
conn.close()
