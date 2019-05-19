from tkinter import ttk
from tkinter import *

root = Tk()
tree = ttk.Treeview(root, columns=("col1", "col2", "col3"))

tree.column("col1", width = 100, anchor ="center")
tree.column("col2", width = 100, anchor ="center")
tree.column("col3", width = 100, anchor ="center")
tree.heading("col1", text ="col1")
tree.heading("col2", text ="col2")
tree.heading("col3", text ="col3")

def onDBClick(event):
    item = tree.selection()[0]
    print
    "you clicked on ", tree.item(item, "values")


for i in range(10):
    tree.insert("", i, values = ("a"+str(i),"b"+str(i),"c"+str(i)))
    tree.bind("<Double-1>", onDBClick)

    tree.pack()
    root.mainloop()
