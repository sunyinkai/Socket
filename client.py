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
    while True:
        d = s.recv(1024)
        if str(d).find("exit"):
            break
        if d:
            print(d)
        if d==b'exit':
            break
    s.close()


if __name__ == "__main__":
    threadingList=[]
    for i in range(10):
        threadingList.append(threading.Thread(client(i)))
    for i in threadingList:
        try:
            i.start()
        except  ConnectionResetError:
            pass
    for i in threadingList:
        i.join()
