#-*- coding: utf-8 -*-

#TCP编程


#AF_INET 指定使用IPv4协议
#AF_INET6 指定使用IPv6协议
#SOCK_STREAM 指定使用面向流的TCP协议
#SOCK_DGRAM 指定使用面向流的UDP协议

#客户端 (Socket)
#提供网页服务的标准端口固定在：80端口
#SMTP服务(邮件服务)：25端口
#FTP服务：21端口
#端口号小于1024的是internet标准服务的端口，端口号大于1024的可以任意使用

import socket

#创建一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('www.sina.com.cn',80))
#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#接收数据
buffer = []
while True:
    #每次最多接收1k字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

#关闭连接
s.close()

header, html = data.split(b'\r\n\r\n',1)
#把接收的数据写入文件
print(header.decode('utf-8'))
with open('sina_home.html','wb') as f:
    f.write(html)


















