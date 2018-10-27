#-*- coding: utf-8 -*-

import socket,threading,time

#基于TCP##################################################

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #绑定本地ip地址 由于不是标准端口可以随意使用端口这里用 8888
# s.bind(('192.168.56.1',8888))
# #调用listen()方法监听端口，传入等待连接的最大数量
# s.listen(5)
# print('Waiting for connection...')
# def tcplink(sock,addr):
#     print('Accept new connection from %s:%s...' % addr)
#     sock.send(b'Welcome!')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if not data or data.decode('utf-8')=='exit':
#             break
#         sock.send(('Hello, %s!' %data.decode('utf-8')).encode('utf-8'))
#     sock.close()
#     print('Connection from %s:%s closed.' % addr)


# while True:
#     #接受一个新连接
#     sock,addr = s.accept()
#     #创建新线程来处理TCP连接
#     t = threading.Thread(target=tcplink,args=(sock,addr))
#     t.start()


#基于UDP#######################################################

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('192.168.56.1',9999))
print('Bind UDP on 9999')
while True:
    #接收来自任何客户端的数据
    data, addr = s.recvfrom(1024)
    if not data or data.decode('utf-8')=='exit':
        break
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello,%s!' % data, addr)
s.close()
























