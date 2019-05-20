"""
from tkinter import *


def rtnkey(event=None):
    print(e.get())


root = Tk()
e = StringVar()
entry = Entry(root, validate='key', textvariable=e, width=50)
entry.pack()
entry.bind("<Double-Button-1>", rtnkey)
root.title('测试回车获取文本框内容')
root.mainloop()
"""
from tkinter import *
from tkinter import scrolledtext

def rtnkey(event=None):
    print(666)
root = Tk()
root.geometry("260x600+900+40")
text1 = scrolledtext.ScrolledText(root, width=70, height=13, )
text1.place( x=10, y=10, width=240, height=500)
text1.config(state=DISABLED)

text2 = Text(root,font=("隶书", 18))
text2.place(in_=text1, x=5, y=5, width=210, height=50)
text2.insert(END, "pius")
text2.config(state=DISABLED)
text2.bind("<Double-Button-1>", rtnkey)
y = 5
for i in range(20):
    text3 = Text(root,font=("隶书", 18))
    text3.place(in_=text1, x=5, y=y, width=210, height=50)
    text3.insert(END, "pius"+"(在线)")
    text3.config(state=DISABLED)
    text3.bind("<Double-Button-1>", rtnkey)
    y += 55
root.mainloop()