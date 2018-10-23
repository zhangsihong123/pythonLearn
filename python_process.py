#-*- coding: utf-8 -*-
from multiprocessing import Process
import os
#os.getpid() 获取进程的ID
#os.getppid() 子进程获取父进程的ID
# print('Process(%s)start...' % os.getpid())
#由于Windows没有fork调用
#pid = os.fork()
#if pid==0:
#    print('I am child process (%s) and my parent is %s.' %(os.getpid(),os.getppid()))
#else:
#    print('I (%s) just create a child process (%s).' %(os.getpid(),pid))

def run_proc(name):
    print('Run child process %s (%s)...' %(name,os.getpid()))

if __name__=='__main__':
    print('Parent process %s.'% os.getpid())
    p=Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join() #等待子进程结束再继续往下运行，通常用于进程间的同步
    print('Child process end.')

#Pool(进程池)#############
#如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
from multiprocessing import Pool,Process,Queue
import os,time,random
def long_time_task(name):
    print('Run task %s (%s)...' % (name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s runs %0.2f seconds.' % (name,(end-start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p=Pool(5) #线程池限制可以创建5个子进程
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocess done...')
    p.close()
    p.join()  #调用这个join()函数时必须要等进程都执行完毕，否则下边这句将提前打印
    print('All subprocess done.')

#执行顺序 有join()方法的顺序
#Parent process 8860.
#Child process will start.
#Run child process test (10268)...
#Parent process 8860.
#Waiting for all subprocess done...
#Run task 0 (12144)...
#Run task 1 (9764)...
#Run task 2 (11364)...
#Run task 3 (11288)...
#Task 3 runs 0.41 seconds.
#Run task 4 (11288)...
#Task 0 runs 0.76 seconds.
#Task 4 runs 1.18 seconds.
#Task 2 runs 2.33 seconds.
#Task 1 runs 2.87 seconds.
#All subprocess done.

#执行顺序 没有join()方法的顺序
#Parent process 9828.
#Child process will start.
#Run child process test (11836)...
#Parent process 9828.
#Waiting for all subprocess done...
#All subprocess done.


#子进程

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

#如果子进程还需要输入，可以通过communicate()方法输入：
# print('$ nslookup')
# p=subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# output,err=p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:',p.returncode)

#进程间通信(包已经上面导入了)
#在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：

#写数据进程执行的代码
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


#读数据进程执行的代码
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value =q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    #父进程创建Queue，并传给各个子进程
    q=Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    #启动子进程pw，写入
    pw.start()
    #启动子进程pr，读取
    pr.start()
    #等待pw结束
    pw.join()
    #pr进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()

#运行结果如下:
#Process to write: 7228
#Put A to queue...
#Exit code: 0
#Process to read: 3240
#Get A from queue.
#ut B to queue...
#Get B from queue.
#Put C to queue...
#et C from queue.
#可以看出进程间通讯可以通过Queue(消息队列)来完成

#小结
#在Unix/Linux下，可以使用fork()调用实现多进程。
#要实现跨平台的多进程，可以使用multiprocessing模块。
#进程间通信是通过Queue、Pipes等实现的。



