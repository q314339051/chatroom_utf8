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
y = 30
def rtnkey(event=None):
    print(666)
root = Tk()
root.geometry("260x600+900+40")
canvas = Canvas(root,width=250,height=500,scrollregion=(0,0,520,y*57)) #创建canvas
canvas.place(x=0, y=0,)
frame=Frame(canvas) #把frame放在canvas里
frame.place(x=0,y=0,width=200, height=180) #frame的长宽，和canvas差不多的
vbar=Scrollbar(canvas,orient=VERTICAL) #竖直滚动条
vbar.place(x=240,width=20,height=500)
vbar.configure(command=canvas.yview)
canvas.config(yscrollcommand=vbar.set) #设置
frame.bind("<Double-Button-1>", rtnkey)


# for i in range(y):
#     text3 = Text(frame, width=34, height=4,highlightcolor="red" )
#     text3.pack(side=TOP,)
#     l = text3.index('insert')
#     if i<10 :
#         text3.insert(END, str(i)+"(在线)")
#         text3.tag_add('tag1', l, l[0:-2]+".end")
#         text3.tag_config('tag1', foreground='green',font=("隶书", 18))
#     else:
#         text3.insert(END, str(i) + "(离线)")
#         text3.tag_add('tag1', l, l[0:-2] + ".end")
#         text3.tag_config('tag1', foreground='gray', font=("隶书", 18))
#     text3.config(state=DISABLED)
#     text3.bind("<Double-Button-1>", rtnkey)

f1 = frame=Frame(frame,bg="red").pack()



canvas.create_window(0,y*28, window=frame,anchor=W)  #create_window
root.mainloop()