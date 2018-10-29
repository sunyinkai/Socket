import socket
import asyncio
import time
import sqlite3


async def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    await loop.sock_sendall(sock,b'welcome')
    # t = sqlite3.connect('passwd.db')
    # db = t.cursor()  # open the database
    #
    # while True:
    #     data = await loop.sock_recv(sock,1024)
    #     if data == 'exit':
    #         break
    #     print(data)
    #     name = (((data.split(':'))[1]).split('\n'))[0]
    #     passwd = (((data.split(':'))[2]).split('\n'))[0]
    #     # print name,passwd
    #     cursor = db.execute("SELECT * FROM INFO WHERE user='%s' " % name)
    #     tmp = []
    #     for row in cursor:
    #         tmp.append(row)
    #     # print tmp
    #     if tmp:
    #         await loop.sock_sendall(b"error:the username already had\n")
    #     else:
    #         db.execute("INSERT INTO INFO(user,passwd) \
    #                    VALUES('%s','%s')" % (name, passwd))
    #         t.commit()
    #         await loop.sock_sendall(b"register complete!the name is %s,the passwd is %s" % (name, passwd))
    await loop.sock_sendall(sock,b"goodbye!")
    sock.close()
    print('Conn'
          'ection from %s:%s closed.' % addr)

async def server():
    addr = ('127.0.0.1', 12345)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # new a socket

    s.bind(addr)
    s.listen(50)
    s.setblocking(False)
    print(b'waitting for link')
    while True:
        sock, addr = await loop.sock_accept(s)  # ?
        loop.create_task(tcplink(sock, addr))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()  # get a event loop
    loop.create_task(server())
    loop.run_forever()
