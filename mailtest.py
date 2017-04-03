#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



me = "mail@gmail.com"
my_password = r"password"

numberOfEmailsByBatch=50
sleepTimeBetweenBatches=120



file1 = open("message.txt", "r") 
message= file1.read() 

file2 = open("recipients.txt", "r")
toaddrs  = file2.read().split()










# Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
s = smtplib.SMTP_SSL('smtp.gmail.com')
# uncomment if interested in the actual smtp conversation
# s.set_debuglevel(1)
# do the smtp auth; sends ehlo if it hasn't been sent already
s.login(me, my_password)


i=0
for c in toaddrs:


	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Message Test"
	msg['From'] = me
	msg['To'] = c
	html = message+" "+str(i)
	part2 = MIMEText(html, 'html')

	msg.attach(part2)

	if(i%numberOfEmailsByBatch==0 and i!=0):
		j=0
		while(j<sleepTimeBetweenBatches):
			if(j%10==0):
				print "Sleeping for ",str(sleepTimeBetweenBatches-j)," more seconds"
			time.sleep(10)
			j=j+10


	s.sendmail(me, c, msg.as_string())
	print i," Mail Send Successfully to", c

	i=i+1




s.quit()
