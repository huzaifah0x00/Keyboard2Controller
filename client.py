import random
import socket
import pickle
import getkeys 
import sys
import time
print(sys.argv)
s = socket.socket()
if len(sys.argv) == 3:
	host = socket.gethostbyname(sys.argv[1])
	port = int(sys.argv[2])
else:
	host = socket.gethostname()
	port = 4444
print("Connecting to host: {} on port: {}".format(host,port))
i =  0
try:
	s.connect((host,port))
	print("Connected succesfully")
except:
	print("Error Connecting")

lastkeys = ""
while True:
	keys = getkeys.getKeys() 
	if keys != lastkeys :
		s.send(pickle.dumps(keys))
		# print(f"sent keys at {time.time()}")
	else:
		pass
	lastkeys = keys.copy()
	time.sleep(0.0005)
print("closing socket")
s.close
