#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image,ImageFilter,ImageDraw,ImageFont
import random

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

#ImageDraw提供了一系列的绘图方法#########

#随机字母
def rndChar():
    return chr(random.randint(65,90))

def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

#240x60:
width = 60*4
height = 60
image = Image.new('RGB',(width,height),(255,255,255))
#创建Font对象  备注：这个字体无法找到暂时没用
font = ImageFont.truetype('/Library/Fonts/Arial.ttf',36)
#创建Draw对象
draw = ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
#输入文字
for t in range(4):
    draw.text((height*t+10,10),rndChar(),font=font,fill=rndColor2())

#模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')

