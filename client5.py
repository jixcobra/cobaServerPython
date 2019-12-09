import socket
import os
import sys
import time

sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sok.connect(('192.168.1.3',7777))
data = None
try:
	user_input = raw_input("Masukkan Lokasi File: ")
	assert os.path.exists(user_input), "file tidak ditemukan pada, "+str(user_input)
	with open(user_input, 'r') as fp:
	    data = fp.read()
	l = len(data)
	print l
	sok.send(str(l))
	sok.sendall(data)
	print sok.recv(1024)

	deadline = time.time() + 30.0
	while not data_received:
		if time.time() >= deadline:
			raise Exception()
		sok.settimeout(deadline - time.time())
		sok.read()
except Exception, e:
	# raise e
	print 'connection error'
finally:
	sok.close()