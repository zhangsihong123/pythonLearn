#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 这个用户输入如果是数字的话 这里默认会编译成字符串类型，导致下面比较出错，解决是将输入的字符转化为数字类型

# age=input('please enter your age:')
# a = 100

# if a >= 0:
#     print(a)
# else:
#     print(-a)
# if age >10:
# 		print('你还小 年龄才',age)
# 	else:
# 		print('你达到我们的标准了 年龄',age)

# age=30
# if age >= 18:
#     print('adult')
# else:
#     print('teenager')

#常量（实际在python是没有常量这回事，只不过是赋值一个写死的值给一个变量，但是这个变量还是可以随意改）
#m = 12.01212121
#print('常量 ： ',m)

#赋值
# a = 123
# a = "ABC"
# print(a)

#除法（有两种 1、精确除 /  2、地板除 //）
#a = 8
#b = 3
#print('a / b = ',a / b)
#print('a // b = ',a // b)

#编码（ASCII编码，ord解码方法,chr编码方法）
# print(ord('S'))
# print(ord('a'))
# print(chr(25991))
#print(b'abc')
#print('abc'.encode('ascii'))#随意编码成哪种格式
#print('张思宏'.encode('utf-8'))
#print('张思宏'.encode('ascii'))#这种编译不了 ASCII无法表示中文
#print(b'\xe4\xb8\xad\xff'.encode('utf-8', errors = 'ignore'))

#格式化（类似C语言）
#####################
#占位符	替换内容 	#
#%d	整数				#
#%f %.3f 浮点数		#
#%s	字符串			#
#%x	十六进制整数		#
#####################

#print('你好！%s' %'python')如果是用户自己输入的数字（因为是字符串类型）下面要用%s表示,%.2f表示浮点数保留几位小数
# name = input('input name: ')
# money = 8888888888.88#input('input money: ')
# houseCount = 1#input('input count: ')
# carCount = 2#input('input count: ')
# print('你好！%s，我有$%.2f，我要用它来买%d幢房子，%d辆车子' %(name,money,houseCount,carCount))
#print('我要用这些钱的 %d%% 买东西' % 7)

#练习({0}}{1}{...})格式化的另一种表示形式
#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
# s1 = 72
# s2 = 85
# percent = (s2-s1)/s2*100
# print('{0}成绩较去年提升了{1:.1f}%'.format('小红',percent))

# q = "我是谁？"
# print(q.encode('utf-8'))
#money = 72
#personCount = 5
#print('今天吃饭一共{0},每人发{1:.2f}红包给我，哈哈哈哈'.format(money,money/personCount))

#################################################################################################################################################

#list数组(包括数组定位取值，-1，-2倒叙取值，元素替换)
# classmates = [1,2,3,4,5]
# print('原始数组为',classmates)
# print('数组长度为：', len(classmates))
# print('第一个元素为：',classmates[0])
# print('最后一个元素为：',classmates[-1])

#替换
# classmates[-2] = 0
# print('替换后的数组为',classmates)

#包括元素(添加、插入)，修改，删除
#(添加)
# classmates.append(-1)
# print('增加值数组为',classmates)

#(插入，可以插入指定位置）

# other = [111,333]
# classmates.insert(3,other)
# print('插入值数组为',classmates)

# print('获取插入的数组other：',classmates[3][0])

#删除(默认删除最后一个)
# classmates.pop(3)
# print('删除值数组为',classmates)

#tuple序列表，跟list很类似，用(小括号表示)但是没有append()，insert(),pop()方法，也无法修改其中的值,一但定义就无法修改
# number = (7,8,9,10,11,12)
# print('tuple 类型数组number：',number)
# print('tuple 类型数组number长度为：',len(number))

#取值
# print('tuple 类型数组取值',number[-1])

#这是种特殊情况，虽然tuple数组不能修改，但是如果元素中有list数组时我们可以对list素组进行随意操作，贼鸡巴六
# l = ['I','Love','Python']
# number2 = (7,8,9,10,11,12,l)
# print('tuple 类型数组number2：',number2)

# number2[-1][0] = 'what'
#number2[-1][1] = 'about'
#number2[-1][2] = 'you'
#print('tuple 类型数组number2：',number2)
#number2[-1].pop(1)
#print('tuple 类型数组number2：',number2)

#排序
#m = ['c','b','a']
#m.sort()
#print('m集合排序',m)

#条件判断(elif 等价于 else if)
#####################
#if <条件判断1>:		#
#    <执行1>			#
#elif <条件判断2>:	#
#    <执行2>			#
#elif <条件判断3>:	#
#    <执行3>			#
#else:				#
#    <执行4>			#
#####################
#一定要注意这个if else 一定不能有空格
# i = input('birth : ')
# birth = int(i)
# if birth <2000 and birth > 1990:
# 	print('你是90后')
# elif birth >= 2000:
# 	print('你是00后')
# else:
# 	print('你太老了，或是太年轻了')

#练习
#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：BMI = 体重kg/身高m^2
#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
# height = 1.75
# weight = 80.5
# bmi = 80.5 // (1.75 * 1.75)
# print('小明的BMI指数为：',bmi)

# if bmi<18.5:
# 	print('过轻')
# elif bmi>=18.5 and bmi<25:
# 	print('正常')
# elif bmi>=25 and bmi < 28:
# 	print('过重')
# elif bmi>=28 and bmi < 32:
# 	print('肥胖')
# else:
# 	print('严重肥胖')

#循环for
# texts = ['I','Love','python']
# index = -1
# for text in texts:
# 	index+=1
# 	temp = text.replace('I','we')
# 	print(text)

# #range(1,10) 表示1-10范围的整数
# count = 0
# for i in range(1,10):
# 	count+=i
# print('\n',count)

# print(list(range(1,100)))

#数据集合dict和set（类似java中的Map,Set）原理差不多
#####################################################################################################
#方法                                  	#描述  														#
#---------------------------------------------------------------------------------------------------#
#D.clear()                              #移除D中的所有项  											#
#D.copy()                               #返回D的副本  												#
#D.fromkeys(seq,val)                  #返回从seq中获得的键和被设置为val的值的字典。可做类方法调用  		#
#D.get(key,default)                   #如果D[key]存在，将其返回；否则返回给定的默认值None  				#
#D.has_key(key)                         #检查D是否有给定键key  										#
#D.items()                              #返回表示D项的(键，值)对列表  									#
#D.iteritems()                          #从D.items()返回的(键，值)对中返回一个可迭代的对象  			#
#D.iterkeys()                           #从D的键中返回一个可迭代对象  									#
#D.itervalues()                         #从D的值中返回一个可迭代对象  									#
#D.keys()                               #返回D键的列表  												#
#D.pop(key,d)                         #移除并且返回对应给定键key或给定的默认值D的值  					#
#D.popitem()                            #从D中移除任意一项，并将其作为(键，值)对返回  					#
#D.setdefault(key,default)            	#如果D[key]存在则将其返回；否则返回默认值None  					#
#D.update(other)                        #将other中的每一项加入到D中。  								#
#D.values()                             #返回D中值的列表												#
#####################################################################################################

d = {'name':'zhangshiong','age':18,'sex':'man'}
print('字典',d)
#查看，取值
key = 'sex'
print('取值',key,' : ',d.items())
for key in d.keys():
	print('取值',key,' : ',d.get(key))
#带默认值的取值
print(d.setdefault('a',111))
print('字典中所有值:',d.values())
#删除
print(d.pop('age'))
#修改
if 'a' in d:
	d['name'] = 'xiaoming';
	print('修改值后字典为 ： ',d)
else:
	print('值不存在请重新键入')

#Set 集合
s = set([1,3,2,5,4,6,6,5])
print('\nset集合',s)
#add()值不可重复
s.add(4)
print('set集合添加之后',s)
#remove(value)
s.remove(4)
print('set集合删除之后',s)
# & 或 | 两个集合可以取交集或并集
n = set([10,6,7,8,9])
print('s交n为',s&n)
print('s并n为',s|n)

#字符串替换，替换是新生成了一个字符串，原来的字符串没有发生改变
#@link https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143167793538255adf33371774853a0ef943280573f4d000
desc = 'I love python'
b = desc.replace('I','we')
print('替换之后字符串：',b)
print('替换之前字符串：',desc)