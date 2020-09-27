#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

email = 'Sender Mail Id'
password = 'Sender Password'
send_to_email = 'Reciever Mail Id'
subject = '!!! Testing Server Report !!!'
message = "Web-Server is not running, debug the code."

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))




server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()

