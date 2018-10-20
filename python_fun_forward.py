# -*- coding: utf-8 -*-
class Student(object):
    pass

s = Student()
s.name='Michael'#动态给实例绑定一个属性

def set_age(self,age):
	self.age = age

def set_score(self,score):
	self.score=score

Student.set_score=set_score

from types import MethodType
s.set_age=MethodType(set_age,s)
s.set_age(20)#调用实例方法

print('年龄:',s.age)

s2=Student()
#s2.set_age(50) 这种动态添加属性没用
#print('age:',s2.age)
s2.set_score(100)
print('成绩:',s2.score)

#使用__slots__  只允许对Student实例添加name和age属性。
class Car():
    __slots__=('name','price')# 用tuple定义允许绑定的属性名称

c = Car() # 创建新的实例
c.name = '兰博基尼' # 绑定属性'name'
c.price = 1000000 # 绑定属性'price'
#c.score = 99 # 绑定属性'score' ,这个不成立 上面变量里面限制死了

class GraduateCar(Car):
	pass
		
g = GraduateCar()
g.score = 200
print(g.score)
#__slots__对子类不起作用
#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

#使用@property

#class Student(object):
#	def get_score(self):
#		return self._score

#	def set_score(self,score):
#		if not isinstance(score,int):
#			raise ValueError('score must be an integer')
#		if score<0 or score>100:
#			raise ValueError('score must between 0~100')
#		self._score=score

#可以改为：
class ClassMate(object):
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer')
		if value<0 or value>100:
			raise ValueError('score must between 0~100')
		self._score=value

cm = ClassMate()
cm.score=60
print(cm.score)
cm.score=100
print(cm.score)

#@property还可以定义只读属性，即只定义getter方法，不定义setter方法就是一个只读属性:

#练习
#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self,vlaue):
		self._width=vlaue

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self,value):
		self._height=value

	@property
	def resolution(self):
		return self._width*self._height
    
screen = Screen()
screen.width = 1024
screen.height = 768
print('resolution = ',screen.resolution)
if screen.resolution==786432:
	print('测试通过')
else:
	print('测试失败')

#MixIn设计
#多继承（python与java不一样，python中可以实现多继承）
#不需要复杂而庞大的继承链，只需要组合不同的类的功能，就可以快速构造出所需的子类

class Animal(object):
	pass

class Mammal(Animal):
	pass

class Bird(Animal):
    pass

class Dog(Mammal):
    pass	

class Bat(Mammal):
	pass

class Parrot(Bird):
	pass

class Ostrich(object):
	pass

class Runnable(object):
    def run(self):
    	print('Running...')

class Flyable(object):
	def fly(self):
		print('Fiying...')

class RunnableMixIn(object):
    def run(self):
    	print('Running...')

class FlyableMixIn(object):
	def fly(self):
		print('Fiying...')

#MixIn 可以改为：
class Dog(Mammal,RunnableMixIn):
	pass


#定制类
class Person(object):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return 'Person object (name : %s)' % self.name
#__repr__调试用的，
	__repr__=__str__

#print(Person('Michael'))#>>>Person object (name : Michael)
#Person('Michael')#__repr__=__str__可以直接打印出来效果和上面一样

#__iter__
# class Fib(object):
# 	def __init__(self):
# 		self.a, self.b=0,1

# 	def __iter__(self):
# 		return self

# 	def __next__(self):
# 		self.a,self.b=self.b, self.a+self.b
# 		if self.a > 100000:
# 			raise StopIteration()
# 		return self.a
#无法进行索引，切片操作
# for n in Fib():
# 	print(n)

#__getitem__
class Fib(object):
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b=1,1
			for x in range(n):
				a,b=b,a+b
			return a
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a,b=1,1
			L=[]
			for x in range(stop):
				if x>=start:
					L.append(a)
				a,b=b,a+b
			return L
#按下标访问
f=Fib()
print(f[10])
print(f[10:100])
#也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的

#__getattr__ 动态化属性

class Student1(object):
	def __getattr__(self,attr):
		if attr=='age':
			return lambda:25

s1 = Student1();
print('年龄:',s1.age())

#利用动态__getattr__,我们可以写出一个链式调用
class Chain(object):
	def __init__(self,path=''):
		self._path=path

	def __getattr__(self,path):
		return Chain('%s/%s' %(self._path,path))

	def __str__(self):
		return self._path

    #使用__call__其实就是返回自己
	def __call__(self,user_name):
		return Chain('%s/%s' %(self._path,user_name))

	__repr__=__str__

#因为Chain找不到这些属性他会自动创建一个
print(Chain('api').status.use.timeline.list) #>>>/status/user/timeline/list
print(Chain().user('michael').repos)


#枚举################################################################################
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print('month => ',Month.Jan)
for name,member in Month.__members__.items():
	print(name,'==>',member,',',member.value)

#value属性是自动给成员的int常量，默认是从1开始计数的
#如果需要更精确的控制枚举类型，可以从enum派生出定义类：
from enum import Enum, unique

@unique
class Weekday(Enum):
	Sun = 0 #Sun的value被设定为0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6
#unique装饰器可以帮助我们检查保证没有重复值
print(Weekday.Wed.value)
for name, member in Weekday.__members__.items():
	print('name => ',member)

#练习
#把Student的gender属性改造为枚举类型，可以避免使用字符串：
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')


#使用元类：type()  动态构建类metaclass
#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000















