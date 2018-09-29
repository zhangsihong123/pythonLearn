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
def myAbs(x):
	#print('输入的x = ',x)
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return -x