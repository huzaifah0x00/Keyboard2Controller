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
		j.data.wAxisX = 0x8000
		j.update()
	def LsRight():
		j.data.wAxisY = 0x8000
		j.update()
	def LsLeft():
		j.data.wAxisY = 0x1
		j.update()
	def LsDown():
		j.data.wAxisX = 0x1
		j.update()
	def LsReset():
		j.data.wAxisX = 0x4000
		j.data.wAxisY = 0x4000
		j.data.wAxisY = 0x4000
		j.data.wAxisY = 0x4000
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
		print("data in ONE CHUCNK = [{}] ".format(data))
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
	while True:
		if vk['UP'] in data:
			print("UP 'cause the data is [{}]".format(data))
			Xbox.LsUp()
		if vk['LEFT'] in data:
			print("LEFT")
			Xbox.LsLeft()
		if vk['RIGHT'] in data:
			print("RIGHT")
			Xbox.LsRight()
		if vk['DOWN'] in data:
			print("DOWN")
			Xbox.LsDown()
		else:
			Xbox.LsReset()
		# j.reset()
		# j.reset_buttons()
		# j.reset_povs()
while True:
	conn, addr = s.accept()
	print('connected to: '+addr[0]+':'+str(addr[1]))
	start_new_thread(threaded_client,(conn,))