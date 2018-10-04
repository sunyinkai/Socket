import socket
#addr=('45.77.197.135',9999)
addr=('127.0.0.1',9999)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(addr)
msg="userName:YinkaiSun\nPasswd:123456\n"
s.send(msg)
buffer=[]
while True:
    d=s.recv(1024)
    if d:
        print d
    else:
        pass
res=''.join(buffer)
print(res)
s.send("exit")
s.close()
