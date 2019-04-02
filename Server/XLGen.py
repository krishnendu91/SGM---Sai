#!/usr/bin/python3
import mysql.connector as pymysql,json
from openpyxl import Workbook
from datetime import datetime
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

fromaddr = "amritawna.pr@gmail.com"
toaddr = "saishibu38380@gmail.com"

timenow = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
filename = 'STPReport'+timenow+'.xlsx'
conn = pymysql.connect(database="AmritaSGM",user="admin",password="admin",host="localhost")
cur = conn.cursor()
cur.execute('SELECT meterName,VLL ,A, PF, F, W, Wh  FROM STPData where timestamp >= DATE_SUB(NOW(),INTERVAL 1 DAY);')
results = cur.fetchall()

wb = Workbook()
ws = wb.create_sheet(0)
#ws.title = "STP Energy Usage Report"
ws.append(cur.column_names)

for row in results:
  #print(row)
  #print(cur.description[1][0])
  ws.append(row)
wb.save(filename)

# instance of MIMEMultipart 
msg = MIMEMultipart() 

# storing the senders email address 
msg['From'] = 'amritawna.pr@gmail.com' 

# storing the receivers email address 
msg['To'] = 'saishibu38380@gmail.com' 

# storing the subject 
msg['Subject'] = "Daily Report - STP Energy"

# string to store the body of the mail 
body = "Please Check the Attachments.\n\n Do not reply to this email. This is an autogenerated message \n\n Regards, \n\n AmritaWNA Report Delivery System"

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
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login(fromaddr,'amma@123') 

# Converts the Multipart msg into a string 
text = msg.as_string() 

# sending the mail 
s.sendmail(fromaddr, toaddr, text) 

# terminating the session 
s.quit() 
print("Email Sent")
