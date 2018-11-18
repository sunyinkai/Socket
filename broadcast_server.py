import asyncio
import socket
import time
from random import randint

f=''
async def generate_num(time=0.25):
    f=open('in.txt','a')
    while True:
        val=randint(0,100)
        f.write(str(val)+'\n')
        await asyncio.sleep(time)


async def send_num(sock,address):
    print('accept a connection from %s:%s'%(address))
    print(type(f))
    for line in f:
        print('tag')
        await loop.sock_sendall(sock,line.encode())


async def main():
    address=('0.0.0.0',12345)
    s=socket.socket()
    s.bind(address)
    s.listen(5)
    s.setblocking(False)
    print('the server is start!')
    while True:
        sock,address=await loop.sock_accept(s)
        loop.create_task(send_num(sock,address))

if __name__=='__main__':
    loop=asyncio.get_event_loop()
    loop.create_task(main())
    loop.create_task(generate_num())
    loop.run_forever()