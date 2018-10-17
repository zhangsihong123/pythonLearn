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

s = Car() # 创建新的实例
s.name = '兰博基尼' # 绑定属性'name'
s.price = 1000000 # 绑定属性'price'
#s.score = 99 # 绑定属性'score' ,这个不成立 上面变量里面限制死了

class GraduateCar(Car):
	pass
		
g = GraduateCar()
g.score = 200
print(g.score)
#__slots__对子类不起作用
#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。









