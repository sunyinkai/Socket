import socket
import threading
#addr=('45.77.197.135',9999)

def client(id):
    print('Start %d! (%s)' % (id, threading.currentThread()))
    addr=('127.0.0.1',12345)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(addr)
    msg=b"userName:YinkaiSun\nPasswd:123456\n"
    s.send(msg)
    buffer=[]
    # while True:
    #     d=s.recv(1024)
    #     if d:
    #         print(d)
    #     else:
    #         break
    d=s.recv(1024)
    if d:
        print(d)
    #s.send(b"exit")
    s.close()
if __name__ == "__main__":
    threadingList=[]
    for i in range(10000):
        threadingList.append(threading.Thread(client(i)))
    for i in threadingList:
        i.start()
    for i in threadingList:
        i.join()
