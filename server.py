import time 
import pickle
import socket
import sys
from getkeys import vk
from _thread import *
import pyvjoy
j = pyvjoy.VJoyDevice(1)
class Xbox:
	def B(power):
		j.set_button(2,1)
		print(power*0.005)
		time.sleep(power*0.005)
		j.set_button(2,0)
	def Y():
		print(dir(j))
	def LsUp():
		j.set_axis(pyvjoy.HID_USAGE_Y, 0x1)
	def LsRight():
		j.set_axis(pyvjoy.HID_USAGE_X, 0x8000)
	def LsLeft():
		j.set_axis(pyvjoy.HID_USAGE_X, 0x1)
	def LsDown():
		j.set_axis(pyvjoy.HID_USAGE_Y, 0x8000)
	def LsReset():
		j.set_axis(pyvjoy.HID_USAGE_Y, 0x4000)
		j.set_axis(pyvjoy.HID_USAGE_X, 0x4000)
		j.set_axis(pyvjoy.HID_USAGE_X, 0x4000)
		j.set_axis(pyvjoy.HID_USAGE_Y, 0x4000)

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
				#call input function 
	conn.close()


def handleInput(data):
	for i in data:
		time.sleep(0.05)
		if vk['UP'] == i:
			print("UP 'cause the data is [{}] and i is [{}]".format(data,i))
			Xbox.LsUp()
			time.sleep(0.05)
			Xbox.LsReset()

		if vk['LEFT'] == i:
			print("LEFT 'cause the data is [{}] and i is [{}]".format(data,i))
			Xbox.LsLeft()
			time.sleep(0.05)
			Xbox.LsReset()

		if vk['RIGHT'] == i:
			print("RIGHT 'cause the data is [{}] and i is [{}]".format(data,i))

			Xbox.LsRight()
			time.sleep(0.05)
			Xbox.LsReset()

		if vk['DOWN'] == i:
			print("DOWN 'cause the data is [{}] and i is [{}]".format(data,i))
			Xbox.LsDown()
			time.sleep(0.05)
			Xbox.LsReset()

		else:
			Xbox.LsReset()
		# j.reset()
		# j.reset_buttons()
		# j.reset_povs()
while True:
	conn, addr = s.accept()
	print('connected to: '+addr[0]+':'+str(addr[1]))
	start_new_thread(threaded_client,(conn,))