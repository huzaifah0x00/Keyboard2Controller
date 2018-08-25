import pickle
import socket
import sys
from _thread import *


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 64129
try:
	s.bind((host, port))
except socket.error as e:
	print(str(e))

s.listen(5)
print('Waiting for a connection.')
def threaded_client(conn):
	conn.send(str.encode('Welcome, type your info\n'))
	i = 1
	while True:
		i = i+1 
		data = conn.recv(2048)
		if not data:
			break	  
		else:
			try:
				data = pickle.loads(data)
			except pickle.UnpicklingError:
				data = "nokeys"

			if data != "nokeys":
				print(data)
				#call input function 
	conn.close()


while True:

	conn, addr = s.accept()
	print('connected to: '+addr[0]+':'+str(addr[1]))

	start_new_thread(threaded_client,(conn,))