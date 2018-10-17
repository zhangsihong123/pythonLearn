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
#xxx #正常的变量(public)
#__xxx__ #特殊变量，我们自己定义变量一般不要用这种变量名
#_xxx #都是非公开的变量(private)
#__xxx #都是非公开的变量(private)


def _private_1(name):
	return 'Hello,%s' % name

def _private_2(name):
	return 'Hi,%s' % name

def greeting(name):
	if len(name)>3:
		return _private_1(name)
	else:
		return _private_2(name)

#外部不需要引用定义为_xxx_

std1={'name':'Michael','score':'98'}
std2={'name':'Bob','score':81}
def print_score(std):
	print('%s:%s' %(std['name'],std['score']))

#(类和实例)使用面向对象程序设计思想
class Student(object):
	"""docstring for Student"""
	def __init__(self, name,score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s:%s' %(self.name,self.score))

	def get_grade(self):
		if self.score>=90:
			return'A'
		elif self.score>=60:
			return'B'
		else:
			return'C'

#实例化对象类似于Java
bart=Student('Bart Simpson', 59)
lisa=Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
print(bart.get_grade())
print(lisa.get_grade())

#访问限制(即，private,public)
class Car(object):
	"""docstring for Car"""
	#私有变量
	def __init__(self, name,price):
	    self.__name = name
	    self.__price = price

    # def get_name(self):
    #     return self.__name
    
    # def set_name(self,name):
    # 	self.__name=name

    # def get_score(self):
    # 	return self.__score

    # def set_score(self,score):
    # 	if 0<=score<=100:
    # 		self.__score=score
    # 	else:
    # 		raise ValueError('bad score')

#Python本身没有任何机制阻止你干坏事，一切全靠自觉，就像__xxx是private变量但是还是一样可以从外部访问，所以需要自己自觉写代码

#继承和多态
class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	def run(self):
		print('Dog is running...')
		
class Cat(Animal):
	def run(self):
		print('Cat is running...')

class Tortoise(Animal):
	def run(self):
		print('Tortoise is running slowly')
		
		
dog = Dog()
dog.run()

cat = Cat()
cat.run()



#多态
def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())

#静态语言 vs 动态语言
#对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
#对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
#这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

#获取对象信息
type(123)#>>>class 'int'
type('123')#>>>class 'str'
type(dog)#>>>class '__main__.Animal'

#比较对象
type(123)==type(4566)#>>>True
type(123)==int#>>>True
#总之各种比
import types
print(type(abs)==types.BuiltinFunctionType)#>>>True
print(type(lambda x:x)==types.LambdaType)#>>>True
print(type((x for x in range(10)))==types.GeneratorType)#>>>True
print('使用isinsatnce函数实现')
#然而使用type判断非常不方便 Python提供了isinstance()函数 判断是哪种数据类型
print(isinstance('abs',str))#>>>True
print(isinstance(123,int))#>>>True
print(isinstance(dog,Dog))#>>>True
print('判断list/tuple')
print(isinstance([1,2,3,4],(list,tuple)))#>>>True
print(isinstance((1,2,3,4),(list,tuple)))#>>>True
print(isinstance({'a':1,'b':2,'c':3,'d':4},(list,tuple,dict)))#>>>True

#使用dir() 返回一个对象的所有属性和方法
#仅仅把属性和方法列出来是不够的，需要配合getattr()、setatter()以及hasatter()
print('判断是否有这个对象属性')
class MyObject(object):
	"""docstring for myObject"""
	def __init__(self):
		self.x=9
	def power(self):
		return self.x*self.x
		
obj = MyObject()
#判断是否有这个对象属性
print(hasattr(obj,'x'),obj.x,hasattr(obj,'y'))
setattr(obj,'y',10)
print(hasattr(obj,'x'),obj.x,hasattr(obj,'y'),getattr(obj,'y'),obj.y)

#获取属性的时候可以传入一个默认值,即使没找到属性也会返回默认值
print(getattr(obj,'e',404))

if hasattr(obj,'power'):
	fn = getattr(obj,'power')#同obj.power()
else:
	fn=None

print(fn())

#这种获取属性的方法在知道对象信息的情况下不要用，否则累死你，尽量简写

#类属性
class Student(object):
	name='Student'

s=Student()

print(s.name) #>>>Student 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name)#>>>Sudent 打印类的name属性
s.name = 'Michael'
print(s.name)#>>> Michael 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name)#>>> Sutdent 但是类属性并未消失，用Student.name仍然可以访问
del s.name # 如果删除实例的name属性
print(s.name) #再次调用s.name,由于实例的name属性没有找到，类的name属性就显示出来了

#通俗点就是：s.name类似全局变量，Student.name类似静态变量








