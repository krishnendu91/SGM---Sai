#!/usr/bin/python3
import mysql.connector as pymysql,json
import openpyxl
from openpyxl import Workbook
from datetime import datetime
import smtplib,sys 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
from subprocess import check_output

a=1
fromaddr = "noreply@amrita.ac.in"
toaddr1 = "saishibu38380@gmail.com"
toaddr2 = "akshayachu.20@gmail.com"
toaddr3 = "manu@am.amrita.edu"

timenow = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
filename = 'STPReport_'+timenow+'.xlsx'
conn = pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur = conn.cursor()

wb = Workbook()
while a<13:
  cur.execute('SELECT meterName FROM STP where id= %(a)s ;',{'a':a})
  meterName=cur.fetchone()
  meterName=meterName[0]
  print("Report Generating for "+str(meterName))
  cur.execute('SELECT meterName,timestamp,VLL ,A, PF, F, W, Wh  FROM STPData where meterName = %(meterName)s and timestamp >= DATE_SUB(NOW(),INTERVAL 1 HOUR) order by id desc;',{'meterName':meterName})
  results = cur.fetchall()
  
  sheetName = "STP Report - " + str(meterName)
  ws = wb.active
  ws=wb.create_sheet(sheetName)
  ws.append(cur.column_names)
  for row in results:
    ws.append(row)
     
  a=a+1

wb.remove(wb[sheet])
wb.save(filename)
sheetName=wb.get_sheet_names()
print(sheetName)

message = "Report Generated Successfully on " + timenow
print(message)

# instance of MIMEMultipart 
msg = MIMEMultipart() 

# storing the senders email address 
msg['From'] = 'noreply@amrita.ac.in' 

# storing the receivers email address 
msg['To'] = 'saishibu38380@gmail.com' 

# storing the subject 
msg['Subject'] = datetime.now().strftime('%d-%m-%Y')+" - Daily Report - STP Energy"

# string to store the body of the mail 
body = str(message)+"\n\nPlease Check the Attachments.\n\n Do not reply to this email. This is an autogenerated message \n\n Regards, \n AmritaWNA Report Delivery System"

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 

# open the file to be sent 

attachment = open(filename, "rb") 

# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 

# To change the payload into encoded form 
p.set_payload((attachment).read()) 

# encode into base64 
encoders.encode_base64(p) 

p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

# attach the instance 'p' to instance 'msg' 
msg.attach(p) 

# creates SMTP session 
s = smtplib.SMTP('smtp.amrita.ac.in', 25) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login('noreply@amrita.ac.in','Amrita@123') 

# Converts the Multipart msg into a string 
text = msg.as_string() 

# sending the mail 
s.sendmail(fromaddr, toaddr1, text) 
#s.sendmail(fromaddr, toaddr2, text) 
#s.sendmail(fromaddr, toaddr3, text) 

# terminating the session 
s.quit() 
print("Email Sent")
delete=check_output(["rm *.xlsx"],shell=1)
