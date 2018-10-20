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



