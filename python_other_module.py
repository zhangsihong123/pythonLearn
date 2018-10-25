#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image,ImageFilter

im=Image.open('14_50_16__09_13_2018.jpg')
w,h = im.size
#获取图片尺寸
print('Original image size: %sx%s' %(w,h))
#缩放到50%

im.thumbnail((w//3,h//3))
print('Resize image to: %sx%s' % (w//3, h//3))
# 把缩放后的图像用jpeg格式保存:
im.save('14_50_16__09_13_2018_thumbnail.jpg', 'jpeg')

im2 = im.filter(ImageFilter.BLUR)
im2.save('14_50_16__09_13_2018_thumbnail.jpg','jpeg')











