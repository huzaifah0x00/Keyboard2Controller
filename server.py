import pickle
import socket
import sys
from getkeys import vk
from _thread import *
import pyvjoy 
j = pyvjoy.VJoyDevice(1)
def B(power):
	j.set_button(2,1)
	print(power*0.005)
	time.sleep(power*0.005)
	j.set_button(2,0)
def Y():
	print(dir(j))
def Up():
	j.data.wAxisX = 0x8000
	j.update()
def Right():
	j.data.wAxisY = 0x8000
	j.update()
def Down():
	j.data.wAxisX = 0x1
	j.update()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 64129
try:
	s.bind((host, port))
except socket.error as e:
	print(str(e))
print("Server IP: {}\n Port: {}".format(host,port))
s.listen(5)
print('Waiting for a connection.')
def threaded_client(conn):
	conn.send(str.encode('Welcome, type your info\n'))
	while True:
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

def inputFunction(data):
	for i in data:
		if vk['UP'] in data:
			print("UP")
			UP()

while True:
	conn, addr = s.accept()
	print('connected to: '+addr[0]+':'+str(addr[1]))
	start_new_thread(threaded_client,(conn,))