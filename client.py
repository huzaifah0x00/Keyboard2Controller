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
s.connect((host,port))
lastkeys = ""
while True:
	keys = getkeys.getKeys() 
	if keys != lastkeys :
		s.send(pickle.dumps(keys))
	else:
		pass
	lastkeys = keys.copy() 
	time.sleep(0.0005)
print("closing socket")
s.close