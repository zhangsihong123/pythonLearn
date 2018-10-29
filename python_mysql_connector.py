#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(user='root',password='password',database='test')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert init user(id,name) values(%s,%s)',['1','zhangsihong'])
print(cursor.rowcount)
conn.commit()
cursor.close()

#查询
cursor = conn.cursor()
cursor.execute('select * from user where id =%s',('1',))
values = cursor.fetchall()
print('查询数据得：',values)
cursor.close()
conn.close()























