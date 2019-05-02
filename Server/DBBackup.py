#!/usr/bin/python3
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

fromaddr = "noreply@amrita.ac.in"
toaddr1 = "saishibu38380@gmail.com"

filename ='AmritaSGM.sql'

# instance of MIMEMultipart 
msg = MIMEMultipart() 

# storing the senders email address 
msg['From'] = 'noreply@amrita.ac.in' 

# storing the receivers email address 
msg['To'] = 'saishibu38380@gmail.com' 

# storing the subject 
msg['Subject'] = datetime.now().strftime('%d-%m-%Y')+" - Daily Database Backup - AmritaSGM"

body = "\nPlease find the attached Backup file"

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
#s.sendmail(fromaddr, toaddrs, text) 
s.sendmail(fromaddr, 'saishibu38380@gmail.com', text) 
#s.sendmail(fromaddr, toaddr3, text) 

# terminating the session 
s.quit() 
print("Email Sent")
