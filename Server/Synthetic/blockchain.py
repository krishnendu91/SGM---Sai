# Synthetic Data to generate consumption and generation

import pymysql,random


conn =pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()

p1=random.uniform(0.0,9.9)*100
p2=random.uniform(0.0,9.9)*100
p3=random.uniform(0.0,9.9)*100
p4=random.uniform(0.0,9.9)*100
p5=random.uniform(0.0,9.9)*100

c1=random.uniform(0.0,9.9)*100
c2=random.uniform(0.0,9.9)*100
c3=random.uniform(0.0,9.9)*100

Tconsumption = c1+c2+c3
Tgeneration = p1+p2+p3+p4+p5
pbal = Tgeneration - Tconsumption


data={"p1":p1, "p2":p2, "p3":p3,"p4":p4,"p5":p5,"c1":c1,"c2":c2,"c3":c3,"Tconsumption":Tconsumption,"Tgeneration":Tgeneration,"pbal":pbal}
print(data)

cur.execute("INSERT INTO `synt-bc` (`Tconsumption`, `Tgeneration`, `p1`, `p2`, `p3`, `p4`, `p5`, `c1`, `c2`, `c3`, `pbal`) VALUES (%(Tconsumption)s, %(Tgeneration)s, %(p1)s, %(p2)s, %(p3)s, %(p4)s, %(p5)s, %(c1)s, %(c2)s, %(c3)s, %(pbal)s);",data)
conn.commit()
conn.close()
