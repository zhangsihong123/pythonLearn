#-*- coding: utf-8 -*-

import socket

#基于TCP#########################################

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #连接python_server中地址为127.0.0.1 port:8888的服务器
# s.connect(('192.168.56.1',8888))
# print(s.recv(1024).decode('utf-8'))
# while True:
#     data = input('please input:')
#     s.send(data.encode('utf-8'))
#     print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()


#基于UDP#########################################

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    data = input('please input:')
    s.sendto(data.encode('utf-8'),('192.168.56.1',9999))
    if not data or data=='exit':
        break
    print(s.recv(1024).decode('utf-8'))
s.close()








