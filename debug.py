import asyncio
import time

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