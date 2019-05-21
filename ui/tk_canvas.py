from tkinter import *

root = Tk()

cv = Canvas(root,bg = 'green')
a = cv.create_rectangle(10,20,365,200,fill='blue')
cv.pack()
vbar=Scrollbar(cv,orient=VERTICAL) #竖直滚动条
vbar.pack(side=RIGHT)
vbar.configure(command=cv.yview)
cv.config(yscrollcommand=vbar.set)
root.mainloop()