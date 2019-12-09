from socket import *
from os import *
import sys
import androgrd1

file_num = 1
s = socket(AF_INET, SOCK_STREAM)
s.bind(('192.168.1.3',7777))
s.listen(5)
print('server on')
try:
	while 1:
		try:
			conn, addr = s.accept()
			print("connected from : "+ addr[0] + ':' + str(addr[1]))
			try:
				l = conn.recv(1024);
				length = int(l)
				data = bytearray()
				while len(data)<length:
					packet = conn.recv(length - len(data))
					data.extend(packet)
					print length
					print len(data)
				with open(os.path.join('./recv','%06d.apk' % file_num), "w") as fs:
					fs.write(data)
				msg = 'success'
				# try:
				# 	rtn = androgrd1.main()
				# 	print rtn
				# 	msg = str(rtn)
				# except Exception, e:
				# 	print e
				conn.send(msg)
				print("recv done")
				file_num +=1
			except:
				print 'error accept connection'
		finally:
			conn.shutdown(SHUT_WR)
			conn.close()
finally:
	# conn.close()
	s.close()