import socket
import threading
#addr=('45.77.197.135',9999)
addr=('127.0.0.1',12345)
def client(id):
    print('Start %d! (%s)' % (id, threading.currentThread()))
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(addr)
    msg=b"58\n3\nsunyinkai33\n123456"
    s.send(msg)
    d=s.recv(1024)
    print(d)
    d=s.recv(1024)
    d=d.decode()
    # length,command,status,description=d.split('\n')
    print(d)
    s.close()


if __name__ == "__main__":
    threadingList=[]
    for i in range(10000):
        threadingList.append(threading.Thread(client(i)))
    for i in threadingList:
        try:
            i.start()

        except  ConnectionResetError:
            pass
    for i in threadingList:
        i.join()
