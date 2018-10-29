import threading

import time
def func(name):
    print('Start %s! (%s)' % (name, threading.currentThread()))
    # yield from语法可以让我们方便地调用另一个generator
    if name == "访问百度":
        print("%s 延迟 10秒" % name)
        threading.sleep(10)
    elif name == "访问Google":
        print("%s 延迟 10秒" % name)
        threading.sleep(10)
    else:
        print("%s 延迟 10秒" % name)
        threading.sleep(10)

    print('\n End %s!! (%s)' % (name, threading.currentThread()))

localtime = time.asctime( time.localtime(time.time()) )
print("begin time",localtime)

thread_list=[]
thread_list.append(threading.Thread(target=func,args=("访问百度")))
thread_list.append(threading.Thread(target=func,args=("访问Google")))
thread_list.append(threading.Thread(target=func,args=("访问Python")))
for i in thread_list:
    i.start()
for i in thread_list:
    i.join()
nowtime = time.asctime( time.localtime(time.time()) )
print("end time",nowtime)