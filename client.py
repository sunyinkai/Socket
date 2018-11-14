import socket
import threading
import pickle

# addr=('45.77.197.135',9999)
addr = ('127.0.0.1', 12345)


class Msg:
    @staticmethod
    def encode_message(lenth, command, username, password):
        msg = chr(0) + chr(0) + chr(0) + chr(lenth)
        msg += chr(0) + chr(0) + chr(0) + chr(command)
        msg += username
        for i in range(0, 20 - len(username)):
            msg += chr(0)
        msg += password
        for i in range(0, 30 - len(password)):
            msg += chr(0)
        return msg

    @staticmethod
    def decode_message(data):
        information = []
        information.append(ord(data[3]))
        information.append(ord(data[7]))
        information.append(ord(data[8]))
        s = ''
        for i in range(9, 73):
            if ord(data[i]) == 0:
                break
            else:
                s += data[i]
        information.append(s)
        return information


mutex = threading.Lock()


def client(id):
    print('Start %d! (%s)' % (id, threading.currentThread()))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(addr)
    msg = Msg.encode_message(58, 3, 'tddfom', '123')

    s.send(msg.encode())
    d = s.recv(1024)
    d = d.decode()
    if mutex.acquire(1):
        length, command, status, description = Msg.decode_message(d)
        mutex.release()
    print(description)
    s.close()


if __name__ == "__main__":
    threadingList = []
    for i in range(1):
        i = threading.Thread(client(i))
        i.start()
    for i in threadingList:
        i.join()
