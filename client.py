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
	keys = getkeys.getKeys() # = 1 
	if keys != lastkeys :
		# time.sleep(0.1)
		print('lastkeys was [{}]\n and currentkeys was [{}]'.format(lastkeys,keys))
		# keystosend = pickle.dumps(keys)
		# print("sending [{}]".format(keys))
		s.send(pickle.dumps(keys))
		# print("sending keys")
	else:
		pass
		# keys = getkeys.getKeys() doesn't work either
		# print('lastkeys was [{}]\n and currentkeys was [{}]'.format(lastkeys,keys))
		# print('not sending keys ')
		# s.send(pickle.dumps("nokeys"))
	lastkeys = keys.copy() # keys.copy() # up = 1 
	# print(type(lastkeys))
print("closing socket")
s.close