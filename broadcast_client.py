import socket


def connect():
    address=('127.0.0.1',12345)
    s=socket.socket()
    s.connect(address)
    while True:
        d=s.recv(1024)
        with open("out.txt","a") as f:
            f.write(d.decode())
if __name__ =='__main__':
    connect()
