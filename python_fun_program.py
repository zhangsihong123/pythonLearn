#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#higher-order,function

#函数可以改变指向
abs(-100)
#>>>100
f = abs
f(-100)
#>>>100

#abs = 10
#abs(-100)
#报错，因为abs已经指向了10，所以无法编译通过

#高阶函数，三个参数都是变量，最后那个根据需求传函数名
def add(x,y,fName):
	return fName(x)*fName(y)

#map操作符 接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每一个元素
#并把结果作为新的Iterator返回,示例如下：
def f(x):
	return x*x
r = map(f,[1,2,3,4,54,5,6])
#>>>list(r)
#>>>[1,4,9,16,2916,25,36]

#reduce操作符 同样接收两个参数，一个是函数，一个是Iterable序列，把一个函数作用在一个序列[x1,x2,x3,...]
#reduce与map不同，其把结果继续和序列的下一个元素做累计计算，
#reduce(f,[x1,x2,x3,...]) = f(f(f(x1,x2),x3,...)，示例如下：
number = [1,3,4,5,65]
from functools import reduce
def add(x,y):
	return x+y
reduce(add,number)
#>>>78

DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def fn(x,y):
	return x*10+y
reduce(fn,number)#>>>134565

def char2num(s):
	return DIGITS[s]
reduce(fn,map(char2num,'253465'))#>>>253465 即是str转int类型的数据

#综上整理所得函数str2int (python函数内部也可以定义函数 真是牛X)
def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return DIGITS[s]
	return reduce(fn,map(char2num,s))
#还可以使用lambda进一步简化为：
def str2int(s):
	return reduce(lambda x, y:x*10+y,map(char2num,s))
#其实上面这个函数等价于int()函数，现在这里是为了测试

#练习
#1、利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
L1 = ['adam', 'LISA', 'barT']
#先写一个传化函数，然后再使用map将函数作用到list的每一个元素上
def normalize(name):
    return name[0].upper()+name[1:].lower()
print(list(map(normalize,L1)))

#2、请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):#lambda形式简化
    return reduce(lambda x,y:x*y,L)
#prod([3, 5, 7, 9]) == 945
#这个练习还没完成这个函数有问题
#def str2float(s):
#	i = s.index('.')
#	return reduce(lambda x,y:x*10+y,map(int,[s[i:],s[i+1]])/pow(10,len(s)-i))

#内建函数filter()用于过滤序列,通过定于的函数是否满足条件决定是否保留该数###################################################################
#过滤掉序列中的偶数
def is_odd(n):
	return n%2==1
print(list(filter(is_odd,[1,2,4,54,5,6,7])))
#过滤序列中的空字符
def not_empty(s):
	return s and s.strip()
print(list(filter(not_empty,['A', '', 'B', None, 'C', '  '])))

#生成除1的所有自然数
def  _odd_iter():
	n=1
	while True:
		n=n+2
		yield n
#求素数
def _not_divisible(n):
	return lambda x:x%n>0

#整理函数
def primes():
	yield 2
	it = _odd_iter()#初始化序列
	while True:
	    n=next(it)#返回序列的第一个数
	    yield n
	    it = filter(_not_divisible(n), it)#构造新序列

#打印出结果,由于primes是一个无限序列这里限制一下
for x in primes():
	if x<10:
		print(x)
	else:
		break

#练习
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

def is_palindrome(n):
	s = str(n)
	return s==s[::-1]
output=filter(is_palindrome,range(1,1000))
print(list(output))

#sorted排序，通过接受一个key函数来实现自定义的排序##################################################################
#按绝对值大小排序
L = [36, 5, -12, 9, -21]
print(sorted(L,key=abs))
#>>>[5, 9, -12, -21, 36]
#keys排序结果 => [5, 9,  12,  21, 36]
#                |  |    |    |   |
#最终结果     => [5, 9, -12, -21, 36]

A = ['bob', 'about', 'Zoo', 'Credit']
#将字符串是序列忽略大小写排序，即将字母都转为大写（或变成小写）
print(sorted(A,key=str.lower))
#如果想将序列进行反向排序，只需加入第三个参数reverse=True
print(sorted(A,key=str.lower,reverse=True))

#练习
#假设我们用一组tuple表示学生名字和成绩：
student = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

#sorted排序的时候每次取list中的单个元素，然后函数里面只对单个元素操作 例：('Bob', 75)[0]='Bob'
#根据名字排序
def by_name(t):
	return t[0]
#print(sorted(student,key=by_name))
print(sorted(student,key=lambda t:t[0]))#用lambda表示

#根据成绩排序
def bu_score(t):
	return -t[1]
#print(sorted(student,key=bu_score))
print(sorted(student,key=lambda t:-t[1]))#用lambda表示

from operator import itemgetter

#operator 中的 itemgetter操作符，结果是一样的
print(sorted(student,key=itemgetter(0)))
print(sorted(student,key=itemgetter(1),reverse=True))

#返回函数，不仅可以返回计算结果还可以将计算的结果保存在函数中返回##############################################################
#闭包(Closure)示例：
def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax=ax+n
		return ax
	return sum #返回一个函数

f1 = lazy_sum(1,2,3,4)
f2 = lazy_sum(1,2,3,4)
print(f1==f2) #输出 False,说明每调用一次函数对象都会变

#闭包(Closure)简单，但是实现起来不容易
#错误示例
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())#>>> 9
print(f2())#>>> 9
print(f3())#>>> 9
#理想结果应该是 f1>1,f2>4,f3>9 但是都输出了9 原因如下:
#原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
#解决办法：
#方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count():
	def f(j):
		def g():
			return j*j
		return g
	fs=[]
	for i in range(1,4):
		fs.append(f(i))# f(i)立刻被执行，因此i的当前值被传入f()
	return fs

f1,f2,f3=count()
print(f1())#>>> 1
print(f2())#>>> 4
print(f3())#>>> 9

#练习
#利用闭包返回一个计数器函数，每次调用它返回递增整数：
#nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
def createCounter():
	count=0
	def counter():
		nonlocal count #利用nonlocal来引用作用在外层的count变量，不然直接使用会报无法引用变量错误
		count+=1
		return count
	return counter

counterA = createCounter()
print(counterA(),counterA(),counterA(),counterA(),counterA())

#匿名函数(就是用lambda表达的)################################################################
#练习
#请用匿名函数改造下面的代码：
def is_odd(n):
    return n % 2 == 1

L = list(filter(lambda n:n%2==1, range(1, 20)))
print(L)
#Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数

#装饰器##########################################################################################
@log('execute')
def now():
	print('2018-10-13')
print(now.__name__)#可以拿到函数的名称__name__
#decorator
def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s %s():' %(text,func.__name__))
			return func
		return wrapper
	return decorator



