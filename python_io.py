#-*- coding: utf-8 -*-
#文件读写
file_path = '/privateFile/pythonWork/pythonLearn/python_test.txt'
# try:
#     f=open(file_path,'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
with open(file_path,'r') as f:
    print(f.read())
#但是以上写法太繁琐，所以Python引入了with语句来自动帮我调用close()方法
#read()读取所有的字节
#read(size)按字节读取
#readline()每次读取一行
#readlines()一次读取所有内容并按行返回list
#如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
f = open(file_path,'r')
for line in f.readlines():
    print(line.strip())

#file-like Object 读取二进制文件
image_path = '/privateFile/pythonWork/pythonLearn/14_50_16__09_13_2018.jpg'

with open(image_path,'rb') as image_f:#二进制读取文件
    print(image_f.read())

#字符编码
with open(file_path,'r',encoding='utf-8') as f:
    print(f.read())

#open()还接收一个error参数 表示遇到编码错误后如何处理。最简单的方式是直接忽略
with open(file_path,'r',encoding='utf-8',errors='ignore') as f:
    print(f.readline())

#写文件
#f=open(file_path,'a',encoding='utf-8')
#f.write("写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：")
#print(f.readlines())
#f.close()

#StringIO和BytesIO##########################################################
#StringIO顾名思义就是在内存中读写str，要把str写入StringIO，我们需要先创建一个StringIO，然后像文件一样写入即可:
from io import StringIO
f=StringIO()
f.write('Hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

f2=StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s=f2.readline()
    if s=='':
        break
    print('\n',s.strip())

#BytesIO
#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
#BytesIO实现了在内存中读写bytes,我们创建一个BytesIO，然后写入一些bytes:
from io import BytesIO
f3=BytesIO()#b'\xe4\xb8\xad\xe6\x96\x87'
f3.write('人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8'))
print(f3.getvalue())

#操作文件和目录############################################################################
import os
os.name #>>>操作系统类型
#os.uname() #>>>获取更详细的系统信息
#环境变量
os.environ #>>>环境变量
os.environ.get('key') #>>>获取某个环境变量的值(key是环境变量的对应的名称) 例：os.environ.get('key')
os.environ.get('x','default') #>>>默认值default
#操作文件个目录
os.path.abspath('.') #>>>查看当前目录的绝对路径
os.path.join('/privateFile/pythonWork/pythonLearn','testdir') #>>>在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
os.mkdir('/privateFile/pythonWork/pythonLearn/testdir') #>>>然后创建一个目录：
os.rmdir('/privateFile/pythonWork/pythonLearn/testdir') #>>>删除掉一个目录
###
#os.path.join() 可以正确处理不同操作系统的路径分隔符，在Linux/Unix/Mac下，返回part-1/part-2字符串
#而在Windows下会返回part-1\part-2
#所以同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
os.path.split('/privateFile/pythonWork/pythonLearn/testdir/file.txt') #>>>('/privateFile/pythonWork/pythonLearn/testdir/', 'file.txt')
os.path.splitext('/privateFile/pythonWork/pythonLearn/testdir/file.txt') #>>>(/privateFile/pythonWork/pythonLearn/testdir/', '.txt')可以直接让你得到文件扩展名
#os.rename('test.txt','python_test.py') #>>>对当前目录下的文件进行操作，重命名
#os.remove('test.py') #>>> 删除文件
#列出当前目录下所有目录
[x for x in os.listdir('.') if os.path.isdir(x)] #>>>当前目录下所有目录
[x for x in os.listdir('.') if os.path.isfile(x)] #>>>当前目录下所有文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'] #>>>当前目录下所有.py文件

#练习
#1、利用os模块编写一个能实现dir -l输出的程序。
#2、编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
def searchFile(file_name,path=os.curdir):
    for x in os.listdir(path):
        x_path = os.path.join(path,x)
        if os.path.isdir(x_path):
            searchFile(file_name,x_path)
        elif x.find(file_name)!=-1:
            print('found: %s' % os.path.relpath(x_path))



#序列化(我们把变量从内存中变成可存储或传输的过程称之为序列化)
# 在python中叫picking，在其他语言中也称之为serialization，marshalling，fattening等等，都是一个意思#
# 而python提供了pickle模块来实现序列化，unpickle反序列化###################################################
#示例：
import pickle
d=dict(name='Bob',age=20,score=99)
print('序列化：\n',pickle.dumps(d)) #dumps():把任意对象序列化成一个bytes,利用这个方法可以把这个bytes写入文件
#pickle.dump()直接把对象序列化后写入一个file-like Object:

f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()
#load()
f=open('dump.txt','rb')
d=pickle.load(f)
f.close()
print('反序列化:',d)

#Json数据，数据类型对照表
#############################
#JSON类型       Python类型   #
#{}             dict        #
#[]             list        #
#"string"       str         #
#1234.56        int或float  #
#true/false     True/False  #
#null           None        #
#############################

import json #Json标准规定编码是UTF-8
js = json.dumps(d)
print('json 格式为：',js) #>>>json.dumps()是直接返回一个json字符串，json.dump()方法可以直接把json写入一个file-like Object
#json.loads()把json反序列化，json.load()从file-like Object中读取字符串并反序列化
# 示例如下：
json_str='{"age":10,"score":89,"name":"Bill"}'
json_ob=json.loads(json_str)
print('反序列化为：',json_ob)

#定义一个Student类
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

def student2dict(self):
    return{
        'name':self.name,
        'age':self.age,
        'score':self.score
    }
    

s=Student('Bob',20,99)
#print(json.dumps(s)) #>>>这样序列化没用，需要传入第二个参数,示例如下
print('Student序列化为：',json.dumps(s,default=student2dict))

#同时也可以直接简写
print('lambda 表达式：',json.dumps(s,default=lambda obj : obj.__dict__))

#反序列化
def dict2sutdent(d):
    return Student(d['name'],d['age'],d['score'])

#object_hook函数负责吧dict转换为Student,其实还是传一个序列化方法进去
print(json.loads(json_str,object_hook=dict2sutdent))




