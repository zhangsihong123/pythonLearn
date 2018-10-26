# -*- coding: utf-8 -*-
import psutil

#在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块

count = psutil.cpu_count() # CPU逻辑数量
print(count)
count = psutil.cpu_count(logical=False) # CPU物理核心
print(count)

print(psutil.cpu_times())

for x in range(10):
    psutil.cpu_percent(interval=1,percpu=True)

print(psutil.virtual_memory())#获取物理内存
print(psutil.swap_memory())#获取交换内存

psutil.disk_partitions() # 磁盘分区信息

psutil.disk_usage('/') # 磁盘使用情况

psutil.disk_io_counters() # 磁盘IO

print(psutil.net_io_counters()) # 获取网络读写字节／包的个数

print(psutil.net_if_addrs()) # 获取网络接口信息

print(psutil.net_if_stats()) # 获取网络接口状态

print(psutil.net_connections()) #获取当前网络连接信息

#获取进程信息
#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001511052957192bb91a56a2339485c8a8c79812b400d49000

psutil.pids() # 所有进程ID

p = psutil.Process(3776) # 获取指定进程ID=3776，其实就是当前Python交互环境
p.name() # 进程名称
p.exe() # 进程exe路径
p.cwd() # 进程工作目录
p.cmdline() # 进程启动的命令行
p.ppid() # 父进程ID
p.parent() # 父进程
p.children() # 子进程列表
p.status() # 进程状态
p.username() # 进程用户名
p.create_time() # 进程创建时间
p.terminal() # 进程终端
p.cpu_times() # 进程使用的CPU时间
p.memory_info() # 进程使用的内存
p.open_files() # 进程打开的文件
p.connections() # 进程相关网络连接
p.num_threads() # 进程的线程数量
p.threads() # 所有线程信息
p.environ() # 进程环境变量
p.terminate() # 结束进程

