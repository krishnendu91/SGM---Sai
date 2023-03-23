#!/usr/bin/python3
# Synthetic Data to generate consumption and generation

import pymysql,random


conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()
bp = 3


def consTarrif(c):
  if c<251:
    if c<51:
      Tc = c*3.15
    elif (c >50 and c<101):
      Tc = c*3.95
    elif (c>100 and c<151):
      Tc = c*5
    elif (c>150 and c<200):
      Tc = c*6.8
    elif (c>200 and c<251):
      Tc = c*8
  elif (c> 251 and c<301):
      Tc = c*6.2
  elif (c>301 and c<400):
      Tc = c*7.35
  elif (c>401 and c<501):
      Tc = c*7.6
  elif (c>500):
      Tc = c*8.5
  return Tc
      


pg1=random.uniform(0.0,999.0)
pe1=random.uniform(0.0,pg1)
pc1=(pg1-pe1)/2
pb1=(pg1-pe1)/2
tp1 = pe1*bp

pg2=random.uniform(0.0,999.0)
pe2=random.uniform(0.0,pg2)
pc2=(pg2-pe2)/2
pb2=(pg2-pe2)/2
tp2 = pe2*bp

pg3=random.uniform(0.0,999.0)
pe3=random.uniform(0.0,pg3)
pc3=(pg3-pe3)/2
pb3=(pg3-pe3)/2
tp3 = pe3*bp

pg4=random.uniform(0.0,999.0)
pe4=random.uniform(0.0,pg4)
pc4=(pg4-pe4)/2
pb4=(pg4-pe4)/2
tp4 = pe4*bp

pg5=random.uniform(0.0,999.0)
pe5=random.uniform(0.0,pg1)
pc5=(pg5-pe5)/2
pb5=(pg5-pe5)/2
tp5 = pe5*bp

c1=random.uniform(0.0,999.0)
Tc1=consTarrif(c1)

c2=random.uniform(0.0,999.0)
Tc2=consTarrif(c2)

c3=random.uniform(0.0,999.0)
Tc3=consTarrif(c3)

Tconsumption = c1+c2+c3
Tgeneration = pe1+pe2+pe3+pe4+pe5

pbal = Tgeneration - Tconsumption

NTp = tp1+tp2+tp3+tp4+tp5
NTc = Tc1+Tc2+Tc3
CostBal = NTc - NTp

data={"pg1":pg1, "pe1":pe1, "pc1":pc1, "pb1":pb1,"tp1":tp1, "pg2":pg2, "pe2":pe2, "pc2":pc2, "pb2":pb2,"tp2":tp2, "pg3":pg3, "pe3":pe3, "pc3":pc3, "pb3":pb3,"tp3":tp3, "pg2":pg4, "pe2":pe4, "pc2":pc4, "pb2":pb4,"tp2":tp4, "pg5":pg5, "pe5":pe5, "pc5":pc5, "pb5":pb5,"tp5":tp5, "c1":c1,"c2":c2,"c3":c3,"Tconsumption":Tconsumption,"Texport":Tgeneration,"pbal":pbal, "tp1":tp1, "tp2":tp2,"tp3":tp3,"tp4":tp4, "tp5":tp5,"Tc1":Tc1,"Tc2":Tc2,"Tc3":Tc3,"NTp":NTp,"NTc":NTc,"CostBal":CostBal }
print(data)

cur.execute("INSERT INTO `synt-bc` (`Tconsumption`, `Texport`, `pe1`, `pe2`, `pe3`, `pe4`, `pe5`, `c1`, `c2`, `c3`, `pbal`,`tp1`, `tp2`, `tp3`, `tp4`, `tp5`, `Tc1`, `Tc2`, `Tc3`, `NTp`, `NTc`, `CostBal`, pg1, pg2, pg3, pg4, pg5, pc1, pc2, pc3, pc4, pc5, pb1, pb2, pb3, pb4, pb5) VALUES (%(Tconsumption)s, %(Tgeneration)s, %(pe1)s, %(pe2)s, %(pe3)s, %(pe4)s, %(pe5)s, %(c1)s, %(c2)s, %(c3)s, %(pbal)s,%(tp1)s, %(tp2)s, %(tp3)s, %(tp4)s, %(tp5)s, %(Tc1)s, %(Tc2)s,%(Tc3)s, %(NTp)s, %(NTc)s, %(CostBal)s, %(pg1)s, %(pg2)s, %(pg3)s, %(pg4)s, %(pg5)s, %(pc1)s, %(pc2)s, %(pc3)s, %(pc4)s, %(pc5)s, %(pb1)s, %(pb2)s, %(pb3)s, %(pb4)s, %(pb5)s);",data)
conn.commit()
conn.close()
