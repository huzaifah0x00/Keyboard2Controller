import time 
import pickle
import socket
import sys
from getkeys import vk
from _thread import *
import vjoy 

def threaded_client(conn):
	conn.send(str.encode('Welcome, type your info\n'))
	while True:
		data = conn.recv(2048)
		# print("data in ONE CHUCNK = [{}] ".format(data))
		if not data:
			break	  
		else:
			try:
				data = pickle.loads(data)
			except pickle.UnpicklingError:
				data = "nokeys"
			if data != "nokeys":
				handleInput(data)
	conn.close()


def handleInput(data):
	for i in data:
		# time.sleep(0.001) 
		
		if vk['UP'] in data:
			if vk['UP'] and vk['RIGHT'] in data:
				vjoy.lsUpRight()
			elif vk['UP'] and vk['LEFT'] in data:
				vjoy.lsUpLeft()
			
			else:
				print("UP 'cause the data is [{}] and i is [{}]".format(data,i))
				start_new_thread(vjoy.lsUp,())
			time.sleep(0.05)
			# vjoy.LsReset()
		if vk['DOWN'] in data:
			if vk['DOWN'] and vk['RIGHT'] in data:
				vjoy.lsDownRight()
			elif vk['DOWN'] and vk['LEFT'] in data:
				vjoy.lsDownLeft()
			else:
				print("DOWN 'cause the data is [{}] and i is [{}]".format(data,i))
				start_new_thread(vjoy.lsDown,())
			time.sleep(0.05)
		if vk['LEFT'] in data :
			if vk['LEFT'] and vk['DOWN'] in data:
				vjoy.lsDownLeft()
			elif vk['LEFT'] and vk['UP'] in data:
				vjoy.lsUpLeft()
			else:
				print("LEFT 'cause the data is [{}] and i is [{}]".format(data,i))
				start_new_thread(vjoy.lsLeft,())
			time.sleep(0.05)
			# vjoy.LsReset()
		
		if vk['RIGHT'] in data:
			if vk['RIGHT'] and vk['DOWN'] in data:
				vjoy.lsDownRight()
			elif vk['RIGHT'] and vk['UP'] in data:
				vjoy.lsUpRight()
			else:
				print("RIGHT 'cause the data is [{}] and i is [{}]".format(data,i))
				start_new_thread(vjoy.lsRight,())
			time.sleep(0.05)
		vjoy.ultimate_release()

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
	while True:
		conn, addr = s.accept()
		print('connected to: '+addr[0]+':'+str(addr[1]))
		start_new_thread(threaded_client,(conn,))
		