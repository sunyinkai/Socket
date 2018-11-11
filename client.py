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


def client(id):
    print('Start %d! (%s)' % (id, threading.currentThread()))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(addr)
    msg = Msg.encode_message(58, 1, 'tom', '123')
    # msg=b"58\n3\nsunyinkai33\n123456"
    s.send(msg.encode())
    d = s.recv(1024)
    print(d)
    d = s.recv(1024)
    d = d.decode()
    length, command, status, description = Msg.decode_message(d)
    print(description)
    s.close()


if __name__ == "__main__":
    threadingList = []
    for i in range(10):
        threadingList.append(threading.Thread(client(i)))
    for i in threadingList:
        try:
            i.start()

        except  ConnectionResetError:
            pass
    for i in threadingList:
        i.join()
