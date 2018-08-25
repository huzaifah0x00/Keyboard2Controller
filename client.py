import socket
import pickle
import getkeys 
import sys
print(sys.argv)
s = socket.socket()
if len(sys.argv) == 3:
	host = sys.argv[1]
	port = int(sys.argv[2])
else:
	host = socket.gethostname()
	port = 64129
i =  0
s.connect((host,port))
while True:
	keys = getkeys.getKeys()
	if keys:
		keys = pickle.dumps(keys)
		s.send(keys)
	else:
		s.send(pickle.dumps("nokeys"))
s.close