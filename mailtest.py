#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib



file1 = open("message.txt", "r") 
message= file1.read() 

file2 = open("recipients.txt", "r")
toaddrs  = file2.read().split()


fromaddr = 'mail@gmail.com'


msg = "\r\n".join([
  "From: Gonçalo Santos",
  "Subject: Just a message",
  message
  ])



username = 'email@gmail.com'
password = 'mailpassword'

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)

for c in toaddrs:
	server.sendmail(fromaddr,c,msg)
	print "Mail Send Successfully to", c

server.quit()
