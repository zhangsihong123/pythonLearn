#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#第一行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2注释表示.py文件本身使用标准UTF-8编码
'a test module'
__author__='Michael Liao'

import sys
def test():
	args=sys.argv
	if len(args)==1:
		print('Hello, world!')
	elif len(args)==2:
		print('Hello,%s!'%args[0])
	else:
		print('Too many arguments!')

#print(__name__=='__main__')主线程

if __name__=='__main__':
	test()

#这个模块可以直接通过命令行导入执行，执行代码如下：
#import python_module
#python_module.test()

#作用域
#正常的变量都是公开的(public)
xxx #正常的变量(public)
__xxx__ #特殊变量，我们自己定义变量一般不要用这种变量名
_xxx #都是非公开的变量(private)
__xxx #都是非公开的变量(private)















