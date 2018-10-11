#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#函数

#abs()取绝对值函数
# x =  abs(200)
# y = abs(-100)
# print('函数调用x = %d,y = %d' %(x,y))
# print('函数调用x = {0},y = {1}'.format(x,y))
#max(...)，min(...)，sum(...)返回最大的数

# number = [2,5,78,4,6]
# print('最大的数为 ： ',max(number))
# print('最小的数为 ： ',min(number))
# print('总和为 ： ',sum(number))

#int(...),str(...)
# i = 12.45
# text = 'strs'
# print('强转为int',float(i))
# print('强转为int',int(i))
# i = str(i)
# print('强转为str',i)
# print('强转为bool',bool(i))

#自定义函数
# def myAbs(x):
# 	#print('输入的x = ',x)
# 	if not isinstance(x,(int,float)):
# 		raise TypeError('bad operand type')
# 	if x>=0:
# 		return x
# 	else:
# 		return -x

# number1=input('please enter first number: ')
# try:
#   first_number=int(number1)
# except ValueError:
#   print("sorry please enter number ")

#函数的参数
# def power(x):
# 	return x * x

#注释：n=2是默认参数
# def power(x,n=2):
# 	s = 1
# 	while n>0:
# 		n=n-1
# 		s=s*x
# 	return s

def add(L=None):
	if L is None:
		L=[]
	else:
		L.insert(0,'start')#插入
		L.append('end')#向后添加
	return L

#可变参数 
#1.
def calc(n):
	sum = 0
	for i in n:
		sum=sum+i*i
	return sum
#2.
def calc(*n):
	sum = 0
	for i in n:
		sum=sum+i*i
	return sum

#关键字参数
def person(name,gender,city,job):
	print('姓名：',name)
	print('性别：',gender)
	print('城市：',city)
	print('工作：',job)

#关键字参数放最后一个带两个**，随意怎么填
def person(name,gender,**kw):
	if 'city' in kw:
		pass
	if 'job'in kw:
		pass
	print('姓名：',name,'性别：',gender,'其他：',kw)
extra={'city':'hangzhou','job':'engineer'}
#示例：person('zhangsihong',20,'man',city='hangzhou',job='chengxuyuan')
#person('zhangsihong','man',**extra)

#限制关键字
def person(name,gender,*,city,job):
	print('姓名：',name,'性别：',gender,'其他：','city:',city,'job:',job)

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name,gender,*args,city,job):
	print('姓名：',name,'性别：',gender,'其他：','city:',city,'job:',job)

#命名关键字参数也可以有缺省值可以简化为：(中间那个*号只标识后面的参数是关键字，没有*则视为位置参数)
def person(name,gender,*,city='hangzhou',job):
	print('姓名：',name,'性别：',gender,'其他：','city:',city,'job:',job)

#组合参数,必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a,b,c=0,*d,**e):
	print('a:',a,'b:',b,'c:',c,'d:',d,'e:',e)
#调用示例：>>>f1(1,2)
#			 f1(1,2,666)
#			 f1(1,2,666,1,3,2)
#			 f1(1,2,666,1,3,2,e='999')
#还可以传入list,tuple或dict 结果牛逼了
#args=(1,2,3,4）
#kw={x='qqq',y='bbb'}
#			 f1(*args,**kw)

#练习
#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(x, *y):
    sum = 1
    if len(y)==0:
        sum=x;
        return sum;
    else:
        for n in y:
            sum=sum*n
        return x*sum
# 测试 结果成立
# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')

#递归函数
def fact(num,product):
	if num == 1:
		return product
	return fact(num-1,num*product)
#print(fact(5,1))

#######################################高级特性############################################
#切片学习
#一下代码可以实现获取表单中某一段数据，但是这样还是太麻烦
L = ['Michael','Sarah','Tracy','Bob','Jack']
r = []
n = 4
for i in range(n):
	r.append(L[i])
print('r:',r)
#python中提供了切片Slice操作符,同时也支持倒切片,这里有点屌 竟然可以越界
L[0:3]
L[1:4]
L[2:5]
L[3:9]
L[-5:-1]
#所有元素中每隔100个取一个
L[::100]
#前100个元素中每隔20个取一个
L[:100:20]
#甚至什么都不写可以原样复制一个list出来
L[:]
#以此类推tuple也同样可以进行上述操作 只不过tuple是不变的集合
T=('I','love','python')
T[0:2]
T[1:3]
T[::2]
T[:3:2]
#同样字符串也可以使用切片
S = 'hangzhouxihu'
S[0:len(S)]
S[:3]#取前面三个字符
S[::2]#所有字符中每隔2个取一个
S[:10:2]#前面10个字符中每隔2个取一个

####################################高级特性###############################
#迭代
D = {'name':'zsh','age':12,'gender':'man'}
#迭代key
for key in D.keys():
	print(key,":",D.get(key))
#迭代value
for vlaue in D.vlaues():
	print(vlaue)
#同时迭代key和value, 这个真是牛批
for key,vlaue in D.items():
	print(key,":",value)

#类似字符串也可以迭代遍历
S = 'I go home bilibilibili'
for s in S:
	print('char:',s)
#是否是可迭代对象通过collections模块的Iterable类型判断
#示例
from collections import Iterable
isinstance('可迭代对象(判断对象)',Iterable)

#同时迭代list 下标和值
M = [(1,2),(2,4),(3,5)]
for i,v in enumerate(L):
	print(i,v)
#同时引用两个变量
for x,y in M:
	print(x,y)

#练习
#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
#这个函数还没用
def findMaxAndMin(L):
	if L!=[]:
		min=L[0]
		max=L[0]
		for n in L:
			if n<min:
				min = n
			if n>max:
				max = n
		return (min,max)
	else:
		return (None,None)

#list生成式
[x*x for x in range(1,100)]
[x*x for x in range(1,100) if x%2=0]
[m + n for m in 'ABC' for n in 'XYZ']