#-*- coding: UTF-8 -*-
"""
    tkinter测试
"""


from tkinter import *
# root = Tk() # 初始化Tk()
# root.title("label-test")    # 设置窗口标题
# root.geometry("200x300")    # 设置窗口大小 注意：是x 不是*
# root.resizable(width=True, height=False) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
# l = Label(root, text="label", bg="pink", font=("Arial",12), width=8, height=3)
# l.pack(side=LEFT)   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
# root.mainloop() # 进入消息循环

# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)        
#         self.pack()
#         self.createWidgets() 
 
#     def createWidgets(self):
#         self.loginLabel = Label(self, text='登录')
#         self.loginLabel.pack()
#         self.registLabel = Label(self, text='注册')
#         self.registLabel.pack()
#         self.quitButton = Button(self, text='Quit', command=self.quit) 
#         self.quitButton.pack()


# app = Application() 
# # 设置窗口标题: 
# app.master.title('qq') 
# # 主消息循环: 
# app.mainloop()

# 初始化tk
# root = Tk()
# root.title("hello world")
# root.geometry('300x300') 

# from tkinter import *

# import tkinter.messagebox as messagebox


# class Application(Frame):

#     def __init__(self, master=None):

#         Frame.__init__(self, master)

#         self.pack()

#         self.createWidgets()



#     def createWidgets(self):

#         self.nameInput = Entry(self)

#         self.nameInput.pack()

#         self.alertButton = Button(self, text='Hello', command=self.hello)

#         self.alertButton.pack()


#     def hello(self):

#         name = self.nameInput.get() or 'world'

#         messagebox.showinfo('Message', 'Hello, %s' % name)



# app = Application()

# # 设置窗口标题:

# app.master.title('Hello World')

# # 主消息循环:

# app.mainloop()