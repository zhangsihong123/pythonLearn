#-*- coding: utf-8 -*-

import asyncio,threading

#协程##########################################################

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n<10:
        n=n+1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()
c = consumer()
produce(c)

#子程序就是协程的一种特例。

#asyncio IO异步#######################################################

# @asyncio.coroutine
# def hello():
#     print('Hello world!')
#     #异步调用asyncio.sleep(1)
#     r = yield from asyncio.sleep(1)
#     print('Hello again!')

# #获取EventLoop
# loop = asyncio.get_event_loop()
# #执行coroutine
# loop.run_until_complete(hello())
# loop.close()



# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s) ' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread)

# loop = asyncio.get_event_loop()
# tasks = [hello(),hello()] #线程不会等待sleep 1秒 只是会直接去执行第二个函数打印出第一句
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

#异步网络连接获取sina,sohu,163网站首页
@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host,80)
    reader,writer = yield from connect
    header = 'GET/HTTP/1.0\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host,line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn','www.sohu.com','www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


#升级(从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。)######################################################
async def hello2():
    print('Hello world!')
    r = await asyncio.sleep(1)
    print('Hello again!')

#貌似这种方法没有，Python版本小于3.5  尴尬####
# lp = asyncio.get_event_loop()
# lp.run_until_complete(hello2())
# lp.close()







