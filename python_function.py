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