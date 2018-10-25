#-*- coding: utf-8 -*-
#获取当前的日期和时间
from datetime import datetime
now=datetime.now() #获取当前的时间
print(now) #>>>2018-10-24 10:57:12.057400
print(type(now))

#获取指定的日期和时间
dt = datetime(2018,10,24,10,59,30)
print(dt)

#datetime转换为timestamp
#在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。

tamp = dt.timestamp() #把datetime转换为timestamp
print(tamp)
print(datetime.fromtimestamp(tamp)) #把本地时间timestamp转换为datetime
print(datetime.utcfromtimestamp(tamp)) #UTC时间

#str 转换为datetime
cday = datetime.strptime('2018-10-24 11:15:00','%Y-%m-%d %H:%M:%S')
print(cday)

#datetime转换为str (更多格式https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)
print(now.strftime('%a, %b %d %H:%M'))

#datetime加减
from datetime import timedelta, timezone

datetime(2018,10,24,11,28,23,540997)
now + timedelta(hours=10)
datetime(2018,10,24,11,28,23,540997)
now- timedelta(days=1)
datetime(2018,10,24,11,28,23,540997)
now + timedelta(days=2,hours=12)
print(datetime(2018,10,24,11,28,23,540997))

#本地时间转换为UTC时间
print('本地时间转换为UTC时间:')
tz_utc_8 = timezone(timedelta(hours=8)) #创建时区UTC+8:00
now = datetime.now()
datetime(2018,10,24,11,28,23,840997)
dt = now.replace(tzinfo=tz_utc_8)
print(dt)

#时区转换
print('时区转换:')
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间：
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('北京时间：',bj_dt)
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print('东京时间：',tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print('北京转东京时间：',tokyo_dt2)

#collections###########################################################
#tuple可以表示一个二维坐标 例如：p=(1,2)

#namedtuple
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p)

#Point 其实是 tuple是一种子类
Circle = namedtuple('Circle',['x','y','r'])

#deque 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)
#q.pop() #删除最后一个
q.popleft() #删除第一个
print(q)

#defaultdict
from collections import defaultdict
dd=defaultdict(lambda:'N/A')
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])

#dict 是无序的，在对dict做迭代时，我们无法确定key的顺序
#如果要保持key的顺序，可以用OrderedDict

from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)]) #无法保证key一定就是有序的
print(d)

od = OrderedDict([('a',1),('b',2),('c',3)]) #可以保证key一定就是有序的
print(od)

#OrderedDict会按照插入的顺序排列，不是key本身排序：
od['x'] = 2
od['y'] = 5
od['z'] = 10
print(list(od.keys()))

#ChainMap 可以把一组dict串起来并组成一个逻辑上的dict
from collections import ChainMap
import os, argparse

# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

#Counter 是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)

#base64编码###########################
import base64
b64 = base64.b64encode(b'binary\x00string')
print('编码后:',b64)
print('解码后:',base64.b64decode(b64))

#struct可以用来解决bytes和其他二进制数据类型的转换######################################
import struct
print(struct.pack('>I',10240099))
#unpack把bytes变成相应的数据类型：
print(struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80'))
#根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack('<ccIIIIIIHH',s))

#hashlib
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print('MD5加密之后：',md5.hexdigest()) #>>>d26a53750bc40b38b65a520292f69306

#如果想让MD5加密出来的数据更加安全可以往口令后面加一个复杂的字符串来实现，俗称'加盐'

#hmac 算法
import hmac
message = b'Hello,Python!'
key = b'secret'
h = hmac.new(key,message,digestmod='MD5')
#如果消息很长，可以多次调用h.update(msg)
print('使用hmac算法加密：',h.hexdigest())

#itertools 提供了非常有用的用于操作迭代对象的函数
import itertools
netuals = itertools.count(1)
for n in netuals:
    if n > 10000:
        break
    print('迭代器',n)

cs = itertools.cycle('ABC')
for c in cs:
    if c == 'C':
        break
    print('字符序列:',c)

ns = itertools.repeat('A',3)
for n in ns:
    print('重复:',n)

netuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x<=100,netuals)
print(list(ns))

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ABC','XYZ'):
    print(c)

#groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key,group in itertools.groupby('AAABBBCCDDD'):
    print(key,list(group))

for key,group in itertools.groupby('AAAbBBCCDdDhhhkkk',lambda c : c.upper()):
    print(key,list(group))

def pi(N):
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    digits=itertools.count(1,2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    digits=itertools.takewhile(lambda x: x<2*N,digits)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    digits=map(lambda x: 4/x if x%4 == 1 else -4/x,digits)
    # step 4: 求和:
    pi=sum(digits)
    return pi

#itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。

# @contextmanager 实现上下文管理
from contextlib import contextmanager
class Query(object):
    def __init__(self,name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()

@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)

with tag('h1'):
    print('hello')
    print('python!')

# @closing 对一个对象没有实现上下文，我们不能把它用于with语句。这时候，可以用closing()来把该对象变为上下文对象。
# 例如，用with语句使用urlopen():
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.baidu.com')) as page:
    for line in page:
        print(line)

# closing 也是一个经过@contextmanager装饰的generator，作用就是把任意对象变为上下文对象，并支持with语句

#urllib#################################################################################
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:',f.status,f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k,v))
    print('Data:',data.decode('utf-8'))










