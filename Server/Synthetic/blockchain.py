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
      


p1=random.uniform(0.0,999.0)
tp1 = p1*bp
p2=random.uniform(0.0,999.0)
tp2 = p2*bp
p3=random.uniform(0.0,999.0)
tp3 = p3*bp
p4=random.uniform(0.0,999.0)
tp4 = p4*bp
p5=random.uniform(0.0,999.0)
tp5 = p5*bp
c1=random.uniform(0.0,999.0)
Tc1=consTarrif(c1)
c2=random.uniform(0.0,999.0)
Tc2=consTarrif(c2)
c3=random.uniform(0.0,999.0)
Tc3=consTarrif(c3)
Tconsumption = c1+c2+c3
Tgeneration = p1+p2+p3+p4+p5
pbal = Tgeneration - Tconsumption

NTp = tp1+tp2+tp3+tp4+tp5
NTc = Tc1+Tc2+Tc3
CostBal = NTc - NTp

data={"p1":p1, "p2":p2, "p3":p3,"p4":p4,"p5":p5,"c1":c1,"c2":c2,"c3":c3,"Tconsumption":Tconsumption,"Tgeneration":Tgeneration,"pbal":pbal, "tp1":tp1, "tp2":tp2,"tp3":tp3,"tp4":tp4, "tp5":tp5,"Tc1":Tc1,"Tc2":Tc2,"Tc3":Tc3,"NTp":NTp,"NTc":NTc,"CostBal":CostBal }
print(data)

cur.execute("INSERT INTO `synt-bc` (`Tconsumption`, `Tgeneration`, `p1`, `p2`, `p3`, `p4`, `p5`, `c1`, `c2`, `c3`, `pbal`,`tp1`, `tp2`, `tp3`, `tp4`, `tp5`, `Tc1`, `Tc2`, `Tc3`, `NTp`, `NTc`, `CostBal`) VALUES (%(Tconsumption)s, %(Tgeneration)s, %(p1)s, %(p2)s, %(p3)s, %(p4)s, %(p5)s, %(c1)s, %(c2)s, %(c3)s, %(pbal)s,%(tp1)s, %(tp2)s, %(tp3)s, %(tp4)s, %(tp5)s, %(Tc1)s, %(Tc2)s,%(Tc3)s, %(NTp)s, %(NTc)s, %(CostBal)s);",data)
conn.commit()
conn.close()
