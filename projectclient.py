import socket
import time 
s = socket.socket()
host = socket.gethostname()
port = 5555
i =  0
s.connect((host,port))
while True:
	message = str(i)
	s.send(message.encode('utf-8'))
	s.send(b"\n")
	reply = s.recv(1024)
	print(reply.decode('utf-8'))
s.close