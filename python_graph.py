#-*- coding: utf-8 -*-

#图形界面

#Tkinter Python代码中内置的Tkinter 分装了访问Tk的接口
#Tk是一个图形库，支持多个操作系统，使用Tcl语言开发

from tkinter import *
import tkinter.messagebox as mbox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        mbox.showinfo('Message','Hello, %s' % name)

app = Application()
# 设置窗口标题
app.master.title('Hello World')
# 主消息循环
app.mainloop()











