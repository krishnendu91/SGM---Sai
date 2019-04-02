#!/usr/bin/python3
import pymysql,json
import datetime
import csv
from xlsxwriter.workbook import Workbook

conn = pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()
cur.execute('SELECT * FROM STPData where timestamp >= DATE_SUB(NOW(),INTERVAL 1 DAY limit 5);')
r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
print(r)
r=json.dumps(r)
print(r)
workbook = Workbook('./test.xlsx')
sheet1 = workbook.add_worksheet()
sheet1.add_table(r)
workbook.close()
