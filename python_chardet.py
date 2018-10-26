#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import chardet

#检测bytes编码,
print(chardet.detect(b'Hello, world!'))

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))

data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))

#可以检测是哪种语言







