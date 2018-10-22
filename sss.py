#-*- coding: utf-8 -*-
from com.android.monkeyrunner import MonkeyRunner as mr #调用monkeyrunnery模块中的类，存储在变量mr中
from com.android.monkeyrunner import MonkeyDevice as md #调用monkeyrunnery模块中的类

print("connect devices……")
device = mr.waitForConnection()#调用mr类中连接设备方法，连接设备

print("install app……")
device.installPackage(r"E:\测试文档管理\上架版本集合\Android\2018\10.16\jianzhuang-release(5).apk")
#调用类中的安装设备方法

package = 'com.dingfang.dfjianzhuang'
activity = 'com.dingfang.dfjianzhuang.activity.SplashActivity'
runComponent = package + "/" + activity

print("lanuch App……")
device.startActivity(runComponent)#调用类中的方法启动APP