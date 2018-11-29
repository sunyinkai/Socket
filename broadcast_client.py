import socket
import os

def connect():
    address = ('127.0.0.1', 12345)
    s = socket.socket()
    s.connect(address)
    while True:
        d = s.recv(1024)
        with open("out{0}.txt".format(os.getpid()), "a") as f:
            f.write(d.decode())


if __name__ == '__main__':
    connect()
