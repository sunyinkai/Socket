# main.py
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python基础-异步IO的支持 async和await

# asyncio的编程模型就是一个消息循环
import threading
import asyncio
import time


# 把 generator 标记为 coroutine 类型，便于执行 EventLoop
async def func(name):
    # await must be used in async function
    print('Start %s! (%s)' % (name, threading.currentThread()))
    # yield from语法可以让我们方便地调用另一个generator
    if name == "访问百度":
        print("%s 延迟 10秒" % name)
        await asyncio.sleep(10)
    elif name == "访问Google":
        print("%s 延迟 10秒" % name)
        await asyncio.sleep(10)
    else:
        print("%s 延迟 10秒" % name)
        await asyncio.sleep(10)

    print('\n End %s!! (%s)' % (name, threading.currentThread()))


localtime = time.asctime(time.localtime(time.time()))
print("begin time", localtime)
# 获取 EventLoop,创建事件循环
loop = asyncio.get_event_loop()

tasks = [func("访问百度"), func("访问Google"), func("访问Python")]

# 执行 coroutine,
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
nowtime = time.asctime(time.localtime(time.time()))
print("end time", nowtime)

import asyncio
import time

'''
async def await_coroutine(name):
    result = await asyncio.sleep(1) #await挂起自己协程，并等待另外一个协程执行完
    print("%s"%name)

def run(coroutine):
    try:
        coroutine.send(None) #drive function
    except StopIteration as e:
        return e.value

localtime = time.asctime( time.localtime(time.time()) )
print("begin time",localtime)

tasks=[await_coroutine("A"),await_coroutine("B"),await_coroutine("C")]

# loop=asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
#

run(await_coroutine("A"))
print("on the main")
nowtime = time.asctime( time.localtime(time.time()) )
print("end time",nowtime)   
'''