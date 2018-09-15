# import mss
import numpy as np
import socket
import sys
import pickle
import time
from io import BytesIO as StringIO
from mss.windows import MSS as mss
class VideoHandler:
	def __init__(self):
		pass
	def get_frame(self):
		self.mon = {'top':30, 'left' : 10, 'width': 600 ,'height':430}
		self.sct = mss()
		self.frame = np.asarray(self.sct.grab(self.mon))
		return self.frame
	def process_frame(self):
		pass
	def ret_frame(self):
		pass
class VideoSocket:
	def __init__(self):
		pass
	def send_frame(self,ip):
		pass
	def recv_frame(self,ip):
		pass
		
# last_time = time.time()
# print((time.time() - last_time )* 1000)
if __name__ == '__main__':
	s = socket.socket()
	if len(sys.argv) == 3:
		host = socket.gethostbyname(sys.argv[1])
		port = int(sys.argv[2])
	else:
		host = socket.gethostname()
		port = 4444
	print(sys.argv)

	print("Connecting to host: {} on port: {}".format(host,port))
	s.connect((host,port))
	framecount = 0 
	while True:
		frame = VideoHandler().get_frame()

		s.sendall(frame)
		framecount += 1
		print(f'Weve sent {framecount} frames So fAr of type {type(frame)} !')
	print("closing socket")
	s.close