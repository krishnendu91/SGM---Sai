#!/usr/bin/python3
import pymysql,json
import datetime
import csv
from openpyxl import Workbook
from datetime import datetime

timenow = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
filename = './STPReport'+timenow+'.xlsx'
conn = pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur = conn.cursor()
cur.execute('SELECT meterName,VLL ,A, PF, F, W, Wh  FROM STPData where timestamp >= DATE_SUB(NOW(),INTERVAL 1 DAY) limit 5;')
#r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
#print(r)


results = cur.fetchall()

wb = Workbook()
ws = wb.create_sheet(0)
ws.title = "STP Energy Usage Report"
#ws.append(cur.description)

for row in results:
  print(cur.description[row][0])
  ws.append(row)
wb.save(filename)    
  
#sheet1 = workbook.add_worksheet()
#sheet1.add_table(r)
#sheet1.write('A1', "Pump Name")
#sheet1.write('B1', "Voltage (V)")
#sheet1.write('C1', "Current (A)")
#sheet1.write('D1', "Power Factor")
#sheet1.write('E1', "Frequency (F)")
#sheet1.write('F1', "Power (W)")
#sheet1.write('G1', "Energy (Wh)")

#for r, row in enumerate(cur.fetchall()):
#  for c, col in enumerate(row):
#    sheet1.write(r, c, col)
#workbook.close()
