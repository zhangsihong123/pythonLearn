#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

#requests 通过GET访问一个网页
r = requests.get('https://www.douban.com/')#豆瓣首页
print('status_code:',r.status_code,'Text:',r.text)

#对于带参数的URL，传入一个dict作为params参数
r = requests.get('https://www.douban.com/search',params={'q':'python','cat':'1001'})
print(r.url,'code',r.encodeing)

#无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：
print('content:',r.content)

#requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取：
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())

#需要传入HTTP Header时，我们传入一个dict作为headers参数：
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})

#POST请求 (只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：)
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})

#requests默认使用application/x-www.form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数
url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
params = {'key':'value'}
r=requests.post(url,json=params)#内容自动序列化为JSON

#类似的上传文件需要更为复杂的编码格式，但是requests把它简化为files参数
upload_files = {'file':open('14_50_16__09_13_2018.jpg','rb')}
r = requests.post(url,files=upload_files)

#注意：读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。

#同时requests还有好几个方法即：put(),delete()
#requests还可以获取响应头
r.headers

#requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie:
r.cookies['ts']

#要在请求头中传入Cookie，只需准备一个dict传入cookies参数：
cs={'token':'12345','status':'working'}
r=requests.get(url,cookies=cs)

#可以传入以秒为单位的timeout参数
r=requests.get(url,timeout=2.5)#2.5秒后请求超时

















