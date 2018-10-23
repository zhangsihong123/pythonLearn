#-*- coding: utf-8 -*-
#正则表达规则:
#'00\d'可以匹配'007'，但无法匹配'00A'；
#'\d\d\d'可以匹配'010'；
#'\w\w\d'可以匹配'py3'；
#.可以匹配任意字符，所以：
#'py.'可以匹配'py'、'pyo'、'py!'等等
# *表示任意个字符（包括0个），
# 用+表示至少一个字符，
# 用?表示0个或1个字符，
# 用{n}表示n个字符，
# 用{n,m}表示n-m个字符:
# ^表示行的开头，^\d表示必须以数字开头。
# $表示行的结束，\d$表示必须以数字结束

# re模块 (最好使用python中的r前缀，不用考虑转义的问题)
s = r'ABC\-001'
#对应的正则表达式字符串不变
#'ABC|-001'

import re
if re.match(r'^\d{3}\-\d{3,8}$', '010-12345'):
    print('ok')
else:
    print('failed')

#切分字符串
print('普通分割法：','a b   c'.split(' '))
#上面的方法无法识别连续的空格，下面用正则表达式试试：
print('正则分割法：',re.split(r'\s+','a b  c d'))
print('正则分割法：',re.split(r'[\s\,]+','a, b,  c, d'))
print('正则分割法：',re.split(r'[\s\,\;]+','a, b, ;; c, d')) #加入;依然可以正常识别

#分组###
#除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。比如：
#^(\d{3})-(\d{3,8})$
m=re.match(r'^(\d{3})-(\d{3,8})$','010-1234578')
#group(0) 永远都是原始字符串
#group(1) 分别表示不同的子串
#group(2)
if m != None:
    print('提取字符0：',m.group(0))
    print('提取字符1：',m.group(1))
    print('提取字符2：',m.group(2))
    print(m.groups()) #>>>返回的是一个tuble
else:
    print('m is None')

#贪婪匹配########
#示例如下：
g = re.match(r'^(\d+)(0*)$','1023000').groups() #>>>('1023','')
print('贪婪匹配：',g)
#上面的例子再修改一下(加个?)：
g = re.match(r'^(\d+?)(0*)$','1023000').groups() #>>>('1023','000')
print('贪婪匹配：',g)

#编译(使用compile()可以像java一样创建一个实例)#######
re_tele=re.compile(r'(\d{3,4})-(\d{3,8})$')
print(re_tele.match('010-12345').groups())
print(re_tele.match('0795-87658006').groups())

#练习
#请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
#someone@gmail.com
#bill.gates@microsoft.com

def is_valid_email(addr):
    email_m = re.compile(r'^[a-zA-Z0-9\.]+\@[a-z0-9]+.com$')
    if email_m.match(addr)!=None:
        return True
    else:
        return False

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


#版本二可以提取出带名字的Email地址：
#<Tom Paris> tom@voyager.org => Tom Paris
#bob@example.com => bob

def name_of_email(addr):
    email_m = re.compile(r'<?(\w+\s?\w+)>?.*@\w+.\w{3}')
    name_str = email_m.match(addr)
    if name_str !=None:
        return name_str.group(1)
    else:
        return False
# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')