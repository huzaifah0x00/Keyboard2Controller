import time 
import pickle
import socket
import sys
import random 
from getkeys import vk
from _thread import *
import vjoy 

def threaded_client(conn,joystickId):
	vjoy.vj = vjoy.vJoy(joystickId)
	while True:
		# lasttime = time.time()
		data = conn.recv(2048)
		# print("data in ONE CHUCNK = [{}] ".format(data))
		if not data:
			break
			print('break ')
		else:
			try:
				keystates = pickle.loads(data)
			except (pickle.UnpicklingError,ValueError):
				keystates = "nokeys"
			if keystates != "nokeys":
				NewHandleInput(keystates)
		# print('{}s'.format(time.time()-lasttime))
	conn.close()

def NewHandleInput(keystates):
	print(keystates)
	if keystates['UP'] == -0x8000:
		print('up pressed')
	if keystates['DOWN'] == -0x8000:
		print('Down pressed')
	if keystates['LEFT'] == -0x8000:
		print('left pressed')
	if keystates['RIGHT'] == -0x8000:
		print('right pressed')
	if keystates['W'] == -0x8000:
		print('w pressed')
	if keystates['S'] == -0x8000:
		print('s pressed')
	if keystates['A'] == -0x8000:
		print('a pressed')
	if keystates['D'] == -0x8000:
		print('d pressed')
	if keystates['Q'] == -0x8000:
		print('Q pressed')
	if keystates['LCONTROL'] == -0x8000:
		print('LCONTROL pressed')
	if keystates['LSHIFT'] == -0x8000:
		print('LSHIFT pressed')
	if keystates['R'] == -0x8000:
		print('R pressed')
# def handleInput(data,):
# 	for i in data:
# 		# time.sleep(0.0) 
		
# 		if vk['UP'] in data:
# 			if vk['UP'] and vk['RIGHT'] in data:
# 				vjoy.lsUpRight()
# 			elif vk['UP'] and vk['LEFT'] in data:
# 				vjoy.lsUpLeft()
			
# 			else:
# 				print("UP 'cause the data is [{}] and i is [{}]".format(data,i))
# 				start_new_thread(vjoy.lsUp,())
# 				# vjoy.lsUp()
# 			time.sleep(0)
# 			# vjoy.LsReset()
# 		if vk['DOWN'] in data:
# 			if vk['DOWN'] and vk['RIGHT'] in data:
# 				vjoy.lsDownRight()
# 			elif vk['DOWN'] and vk['LEFT'] in data:
# 				vjoy.lsDownLeft()
# 			else:
# 				print("DOWN 'cause the data is [{}] and i is [{}]".format(data,i))
# 				start_new_thread(vjoy.lsDown,())
# 				# vjoy.lsDown()
# 			time.sleep(0)
# 		if vk['LEFT'] in data :
# 			if vk['LEFT'] and vk['DOWN'] in data:
# 				vjoy.lsDownLeft()
# 			elif vk['LEFT'] and vk['UP'] in data:
# 				vjoy.lsUpLeft()
# 			else:
# 				print("LEFT 'cause the data is [{}] and i is [{}]".format(data,i))
# 				start_new_thread(vjoy.lsLeft,())
# 				# vjoy.lsLeft()
# 			time.sleep(0)
# 			# vjoy.LsReset()
		
# 		if vk['RIGHT'] in data:
# 			if vk['RIGHT'] and vk['DOWN'] in data:
# 				vjoy.lsDownRight()
# 			elif vk['RIGHT'] and vk['UP'] in data:
# 				vjoy.lsUpRight()
# 			else:
# 				print("RIGHT 'cause the data is [{}] and i is [{}]".format(data,i))
# 				start_new_thread(vjoy.lsRight,())
# 				# vjoy.lsRight()
# 			time.sleep(0)
# 		vjoy.ultimate_release()

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
		