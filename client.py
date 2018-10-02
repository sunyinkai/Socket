import socket
addr=('45.77.197.135',9999)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(addr)
for data in ['A','B','C']:
    s.send(data)
    print s.recv(1024)
s.send('exit')
s.close()
