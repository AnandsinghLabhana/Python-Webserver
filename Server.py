#!/usr/bin/python 

import socket

s = socket.socket()		
hostname= socket.gethostname()
port = 62232
s.bind((hostname,port))

s.listen(3)
while True:
	c, addr=s.accept()
	print 'Got connection from', addr
	c.send('Thank you for the connection')
	c.close()
	
