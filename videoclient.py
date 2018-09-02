import mss
import numpy as np
import socket
import sys
import pickle
import time
from io import BytesIO as StringIO

mon = {'top':30, 'left' : 10, 'width': 600 ,'height':430}
sct = mss.mss()
# last_time = time.time()
# print((time.time() - last_time )* 1000)
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
	orig_img = np.asarray(sct.grab(mon))
	# f = StringIO()
	# orig_img .savez_compressed(f, frame=orig_img)
	# f.seek(0)
	# out = f.read()
	# print(type(out))
	s.sendall(orig_img.tobytes())
	framecount += 1

	# time.sleep(0.0005)
	print(f'Weve sent {framecount} frames So fAr !')
print("closing socket")
s.close