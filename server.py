import socket
import asyncio
import sqlite3
import hashlib
import environ


class Msg:
    @staticmethod
    def encode_message(lenth, command, status, description):
        msg = ''
        msg += chr(0)*3  + chr(lenth)
        msg += chr(0)*3 + chr(command)
        msg += chr(status)
        msg += description+chr(0)*(64-len(description))
        return msg

    @staticmethod
    def decode_message(data):
        information = []
        information.append(ord(data[3]))
        information.append(ord(data[7]))
        s = ''
        for i in range(8, 28):
            if ord(data[i]) == 0:
                break
            else:
                s += data[i]
        information.append(s)
        s = ''
        for i in range(28, 58):
            if ord(data[i]) == 0:
                break
            else:
                s += data[i]
        information.append(s)
        return information


async def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    # await loop.sock_sendall(sock, b'welcome')
    t = sqlite3.connect('passwd.db')
    db = t.cursor()  # open the database

    data = await loop.sock_recv(sock, 1024)
    data = data.decode()
    lenth, command, username, passwd = Msg.decode_message(data)
    print(lenth, command, username, passwd)
    m = hashlib.md5()
    m.update(passwd.encode())
    m.update(environ.SECRETKEY.encode())  # add salt
    passwd = m.hexdigest()
    if command == 1:
        tmp = []
        msg = ''
        for row in db.execute("SELECT * FROM INFO WHERE user='%s' " % username):
            tmp.append(row)
        if tmp:
            msg = Msg.encode_message(73, 2, 0, 'no!the username has exist!')
        else:  # ok
            db.execute("INSERT INTO INFO(user,passwd) VALUES('%s','%s')" % (username, passwd))
            t.commit()
            msg = Msg.encode_message(73, 2, 1, 'ok! username=%s,the password =%s' % (username, passwd))
        await loop.sock_sendall(sock, msg.encode())
    elif command == 3:
        cursor = db.execute("SELECT * FROM INFO WHERE user='%s' " % username)
        tmp = []
        msg = ''
        for row in cursor:
            tmp.append(row[1])
        if tmp:
            if (passwd == tmp[0]):
                msg = Msg.encode_message(73, 4, 1, 'ok!login sucessful!')
            else:
                msg = Msg.encode_message(73, 4, 0, 'no!passwd is wrong!')
        else:
            msg += Msg.encode_message(73, 4, 0, 'no!have no such a username!')
        await loop.sock_sendall(sock, msg.encode())
    else:
        pass
    # await asyncio.sleep(10)
    sock.close()
    print('Connection from %s:%s closed.' % addr)


async def main():
    addr = ('0.0.0.0', 12345)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # new a socket
    s.bind(addr)
    s.listen(5)
    s.setblocking(False)
    print('the server is start!')
    while True:
        sock, addr = await loop.sock_accept(s)
        loop.create_task(tcplink(sock, addr))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()  # get a event loop
    loop.create_task(main())
    loop.run_forever()

