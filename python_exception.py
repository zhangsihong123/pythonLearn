# -*- coding: utf-8 -*-
#异常处理
a = 'b'
try:
	print('try...')
	r=100/int(a)
	print('result:',r)
except ValueError as e:
	print('ValueError:',e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:',e)
else:
	print('no error!')
finally:
	print('finally...')
print('END')

def foo(s):
	return 10/int(s)

def bar(s):
	return foo(s)*2

def main():
	try:
		bar('0')
	except Exception as e:
		print('Error:',e)
	finally:
		print('finally...')

main()
#写程序需要捕获异常

class FooError(ValueError):
	pass

def foo(s):
	n=int(s)
	if n==0:
		raise FooError('invalid value : %s' % s)
	return 10 / n

def bar():
	try:
		foo('0')
	except ValueError as e:
		print('ValueError!')
		raise
#foo()已经捕获了异常但是还是往上抛出，这种处理方式非常常见，在函数不知道该怎么处理该错误的的时候，最恰当的房事继续往上抛，让上级函数处理
#由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。
#bar()

#断言 assert（凡是用print()来辅助查看的地方，都可以用断言(assert)来代替）#####################################################################
def foo(s):
	n = int(s)
	assert n != 0,'s is zero'
	return 10 / n

def main():
	foo('1')

#main()

#logging 把print()替换为logging 和 assert比，logging不会抛出错误，而且可以输出到文件

#这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
#logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
import logging
logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.WARNING)
s = '1'
n=int(s)
logging.info('n = %d' %n)
# logging.warning('n = %d' %n)
print(10/n)

import pdb
#pdb  pdb.set_trace()断点单步调试程序运行到这会自动停在这个方法上
#pdb.set_trace()

class Dict(dict):
	def __init__(self,**kw):
		super.__init__(**kw)
	
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError as e:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

	def __setattr__(self, key,value):
		self[key]=value

import unittest
from python_exception import Dict
class TestDict(unittest.TestCase):
	def test_init(self):
		d=Dict(a=1,b='test')
		self.assertEqual(d.a,1)
		self.assertEqual(d.b,'test')
		self.assertTrue(isinstance(d,dict))
	
	def test_key(self):
		d=Dict()
		d['key']='value'
		self.assertEqual(d.key,'value')

	def test_attr(self):
		d=Dict()
		d.key='value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'],'value')

	def test_keyerror(self):
		d=Dict()
		with self.assertRaises(KeyError):
			value=d['empty']

	def test_attrerror(self):
		d=Dict()
		with self.assertRaises(AttributeError):
			value = d.empty

	def setUp(self):
		print('setUp...')

	def tearDown(self):
		print('tearDown...')

if __name__=='__main__':
	unittest.main()

#文档测试 re示例代码###########################################################
import re
#logging.basicConfig(level=logging.INFO)
m=re.search('(?<=abc)def','abcdef')
m.group(0)












