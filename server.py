import time 
import pickle
import socket
import sys
import random 
import struct
from getkeys import vk
from _thread import start_new_thread
import vjoy 

def threaded_client(conn,joystickId):
	vj = vjoy.vJoy(joystickId)
	while True:
		data = conn.recv(2048)
		if not data:
			print('break ')
			break
		else:
			try:
				keystates = pickle.loads(data)

			except (pickle.UnpicklingError,ValueError):
				keystates = "nokeys"
			if keystates != "nokeys":
				start_new_thread(vj.movement, (keystates,))
				start_new_thread(vj.buttons, (keystates,))
	conn.close()
if __name__ == '__main__':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = socket.gethostname()
	port = 4444
	try:
		s.bind((host, port))
	except socket.error as e:
		print(str(e))
	print("Server IP: {}\n Port: {}".format(host,port))
	s.listen(5)
	print('Waiting for a connection.')
	joystickId = 0
	while True:
		joystickId += 1
		conn, addr = s.accept()
		print('connected to: '+addr[0]+':'+str(addr[1]))
		print('Waiting for Keystrokes From: ' + str(addr[0]))
		start_new_thread(threaded_client,(conn,joystickId),)