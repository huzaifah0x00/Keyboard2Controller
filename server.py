import time 
import pickle
import socket
import sys
from getkeys import vk
from _thread import *
import vjoy 
# j = pyvjoy.VJoyDevice(1)
# class Xbox:
# 	def B(power):
# 		j.set_button(2,1)
# 		print(power*0.001)
# 		time.sleep(power*0.001)
# 		j.set_button(2,0)
# 	def Y():
# 		print(dir(j))
# 	def LsUp():
# 		j.set_axis(pyvjoy.HID_USAGE_Y, 0x1)
# 	def LsRight():
# 		j.set_axis(pyvjoy.HID_USAGE_X, 0x8000)
# 	def LsLeft():
# 		j.set_axis(pyvjoy.HID_USAGE_X, 0x1)
# 	def LsDown():
# 		j.set_axis(pyvjoy.HID_USAGE_Y, 0x8000)
# 	def LsReset():
# 		j.set_axis(pyvjoy.HID_USAGE_Y, 0x4000)
# 		j.set_axis(pyvjoy.HID_USAGE_X, 0x4000)
# 		j.set_axis(pyvjoy.HID_USAGE_X, 0x4000)
# 		j.set_axis(pyvjoy.HID_USAGE_Y, 0x4000)

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
			print("UP 'cause the data is [{}] and i is [{}]".format(data,i))
			vjoy.lsUp()
			# time.sleep(0.05)
			# vjoy.LsReset()
		if vk['LEFT'] in data :
			print("LEFT 'cause the data is [{}] and i is [{}]".format(data,i))
			vjoy.lsLeft()
			# time.sleep(0.05)
			# vjoy.LsReset()
		if vk['DOWN'] in data:
			print("DOWN 'cause the data is [{}] and i is [{}]".format(data,i))
			vjoy.lsDown()
			# time.sleep(0.05)
		if vk['RIGHT'] in data:
			print("RIGHT 'cause the data is [{}] and i is [{}]".format(data,i))

			vjoy.lsRight()
			# time.sleep(0.05)
			# vjoy.LsReset()
		# if vk['DOWN'] == i:
		# 	print("DOWN 'cause the data is [{}] and i is [{}]".format(data,i))
		# 	vjoy.lsDown()
		# 	time.sleep(0.001)
		# 	# vjoy.LsReset()

		
		vjoy.ultimate_release()
		# j.reset()
		# j.reset_buttons()
		# j.reset_povs()
while True:
	conn, addr = s.accept()
	print('connected to: '+addr[0]+':'+str(addr[1]))
	start_new_thread(threaded_client,(conn,))