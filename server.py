import socket
import asyncio
import sqlite3


async def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    await loop.sock_sendall(sock, b'welcome')
    t = sqlite3.connect('passwd.db')
    db = t.cursor()  # open the database
    data = await loop.sock_recv(sock, 1024).decode()
    data = data.decode()
    # print(data)
    lenth, command, username, passwd = data.split("\n")
    # print("--------------------->")
    # print(lenth, command, username, passwd)
    if command == '1':
        tmp = []
        msg=''
        for row in db.execute("SELECT * FROM INFO WHERE user='%s' " % username):
            tmp.append(row)
        if tmp:
            msg+='len\n'+'2\n'+'0\n'+'no! the username has exist!'
        else:   #ok
            db.execute("INSERT INTO INFO(user,passwd) VALUES('%s','%s')" % (username, passwd))
            t.commit()
            msg+= 'len\n'+'2\n' + '1\n' + 'ok! username=%s,the password =%s' % (username, passwd)
        await loop.sock_sendall(sock, msg.encode())
    elif command == '3':
        cursor = db.execute("SELECT * FROM INFO WHERE user='%s' " % username)
        tmp = []
        msg=''
        for row in cursor:
            tmp.append(row[1])
        if tmp:
            if(passwd==tmp[0]):
                msg+='len\n'+'4\n'+'1\n'+'ok!login sucessful!'
            else:
                msg+='len\n'+'4\n'+'0\n'+'no!passwd is wrong!'
        else:
            msg+='len\n'+'4\n'+'0\n'+'no!have no such a username!'
        await loop.sock_sendall(sock, msg.encode())
    else:
        pass
    sock.close()
    print('Connection from %s:%s closed.' % addr)


async def main():
    addr = ('127.0.0.1', 12345)
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
