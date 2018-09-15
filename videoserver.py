import cv2
import numpy as np
import socket
import sys
import pickle
import time
from io import BytesIO as StringIO
from _thread import start_new_thread
def threaded_client(conn):
	framecount = 0 
	while True:
		pixdata = conn.recv(2048)
		if not pixdata:
			print('break ')
			break
		else:
			try:
				pixels = pixdata
				# pixels  = pixdata
			except:
				pixels = "Nope"
				print("error UnpicklingError")
			if pixels != "Nope":
				framecount += 1
				print(f"We've Recieved {framecount} frames So Far ! of type {type(pixels)} looking like \n[{pixels}]\n")
				cv2.imshow('a', pixels)
	conn.close()
if __name__ == '__main__':
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
	while True:
		conn, addr = s.accept()
		print('connected to: '+addr[0]+':'+str(addr[1]))
		print('Waiting for Frames From: ' + str(addr[0]))
		start_new_thread(threaded_client,(conn,),)