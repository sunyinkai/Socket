import asyncio
import socket
from random import randint

all_cnt = 0  # 目前服务器已经生产了多少个字节的数据


async def generate_num(timer=0.25):
    global all_cnt
    while True:
        with open('in.txt', 'a') as f:
            val = randint(0, 100)
            string = str(val) + '\n'
            f.write(string)
            all_cnt = all_cnt + len(string)
        await asyncio.sleep(timer)  # 挂起当前协程


async def send_num(sock, address):
    print('accept a connection from %s:%s' % (address))
    now_cnt = 0  # 当前sock已经接收到了什么位置
    while True:
        num = ''
        with open('in.txt', 'r') as f:
            if now_cnt < all_cnt:
                f.seek(now_cnt)
                num = f.readline()

        if len(num):
            await loop.sock_sendall(sock, num.encode())
            now_cnt = now_cnt + len(num)
        else:
            await asyncio.sleep(0.0001)   # 挂起当前协程


async def main():
    address = ('0.0.0.0', 12345)
    s = socket.socket()
    s.bind(address)
    s.listen(5)
    s.setblocking(False)
    print('the server is start!')
    while True:
        sock, address = await loop.sock_accept(s)
        loop.create_task(send_num(sock, address))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.create_task(generate_num())
    loop.run_forever()
