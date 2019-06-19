#!/usr/bin/env python

import socket
from time import localtime, strftime

TCP_IP = '172.16.88.193'
TCP_PORT = 10000
BUFFER_SIZE = 1024
MESSAGE = (b'\xFE\x05\x00\x04\xFF\x00\xD9\xF4')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)
a=strftime("%Y-%m-%d %H:%M:%S", localtime())
file = open("/home/pi/record.txt", "a")
file.write("Port 5 open at :	")
file.write(a)
file.write("\n")
file.close()