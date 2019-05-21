from tkinter import *
def a(event):
    print(88)
root=Tk()
frame=Frame(root,width=300,height=300,bg="red")
frame.pack()
x=y =0
for i in range(30):
    L = Label(frame, text=i, font=('', 9), fg='white', bg='green')
    L.place(x=x,y=y,width=30,height=30)
    L.bind("<Double-Button-1>",a)

    y+=30
frame.bind("<Double-Button-1>",a)
root.mainloop()