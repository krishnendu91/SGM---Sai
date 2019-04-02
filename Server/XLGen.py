#!/usr/bin/python3
import pymysql
import datetime
import csv
from xlsxwriter.workbook import Workbook

conn = pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur=conn.cursor()
cur.execute('SELECT * FROM STPData where timestamp >= DATE_SUB(NOW(),INTERVAL 1 DAY);')

workbook = Workbook('./test.xlsx')
sheet = workbook.add_worksheet()
for r, row in enumerate(cur.fetchall()):
  for c, col in enumerate(row):
    sheet.write(r, c, col)
workbook.close()
