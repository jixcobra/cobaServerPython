import os
from socket import *
from struct import unpack
import time
from androguard.misc import AnalyzeAPK
import sys
from os import system
import pickle
import androgrd1

class ServerProtocol:

    def __init__(self):
        self.socket = None
        self.output_dir = './recv'
        self.input_dir = './recv'
        self.file_num = 1

    def listen(self, server_ip, server_port):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((server_ip, server_port))
        self.socket.listen(5)

    def handle(self):

        try:
            while True:
                (connection, addr) = self.socket.accept()
                try:
                    l = connection.recv(1024);
                    length = int(l)
                    # bs = connection.recv(8)
                    # (length,) = unpack('>Q', bs)
                    data = b''
                    while len(data) < length:
                        to_read = length - len(data)
                        data += connection.recv(
                            4096 if to_read > 4096 else to_read)

                    # send our 0 ack
                    assert len(b'\00') == 1
                    connection.sendall(b'\00')

                    with open(os.path.join(self.output_dir, '%06d.apk' % self.file_num), 'w') as fp:
                        fp.write(data)
                    # rtn = system('python ./proc1.py')
                    # rtn = proc1.fun1()
                    rtn = androgrd1.main()
                    print str(rtn)
                    # dats = pickle.dumps(rtn)
                    # print (dats)
                    # connection.sendall(dats)
                finally:
                    connection.shutdown(SHUT_WR)
                    connection.close()


                # system('python ./proc1.py')

                self.file_num += 1
        finally:
            self.close()

    def close(self):
        self.socket.close()
        self.socket = None

if __name__ == '__main__':
    sp = ServerProtocol()
    sp.listen('192.168.1.3', 7777)
    sp.handle()
    main()