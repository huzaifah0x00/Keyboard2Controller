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
	shared_items = {k: keys[k] for k in keys if k in lastkeys and keys[k] == lastkeys[k]}
	print(len(shared_items))
	print(shared_items)
	if keys != lastkeys:
		keystosend = pickle.dumps(keys)
		# print("sending [{}]".format(keys))
		s.send(pickle.dumps(keystosend))
		# print("sending keys")
	else:
		# print('lastkeys was [{}]\n and currentkeys was [{}]'.format(lastkeys,keys))
		print('not sending keys ')
		time.sleep(0.5)
		# s.send(pickle.dumps("nokeys"))
	lastkeys = keys
print("closing socket")
s.close