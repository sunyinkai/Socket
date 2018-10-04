import socket
import threading
import time
import sqlite3
def tcplink(sock,addr):
    print 'Accept new connection from %s:%s...'%addr
    sock.send('welcome!')
    t=sqlite3.connect('passwd.db')
    db=t.cursor()#open the database

    while True:
        data=sock.recv(1024)
        if data=='exit':
            break
        #print(data)
        name=(((data.split(':'))[1]).split('\n'))[0]
        passwd=(((data.split(':'))[2]).split('\n'))[0]
        #print name,passwd
        cursor=db.execute("SELECT * FROM INFO WHERE user='%s' "%name)
        tmp=[]
        for row in cursor:
            tmp.append(row)
        #print tmp
        if tmp:
            sock.send('the username already had\n')
        else:
            db.execute("INSERT INTO INFO(user,passwd) \
                       VALUES('%s','%s')"%(name,passwd))
            t.commit()
            sock.send("register complete!the name is %s,the passwd is %s"%(name,passwd))
    sock.close()
    print 'Connection from %s:%s closed.'%addr

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print 'waitting for link'
while True:
    sock,addr =s.accept()
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()