#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter
import tkinter.messagebox


def register_window():
    # 创建注册窗口
    win1 = tkinter.Toplevel()
    # 窗口大小
    win1.geometry("350x200")
    # 设置窗口大小固定
    win1.resizable(0, 0)
    # 设置窗口背景图
    photo = tkinter.PhotoImage(file="backgr.gif")
    label = tkinter.Label(win1, image=photo)  # 图片
    label.pack()
    # 创建账号密码标签
    tkinter.Label(win1, text='账号').place(x=50, y=30)
    tkinter.Label(win1, text='密码').place(x=50, y=70)
    tkinter.Label(win1, text='确认密码').place(x=26, y=110)
    # 创建输入框
    sheet_text1 = tkinter.StringVar()
    sheet_text2 = tkinter.StringVar()
    sheet_text3 = tkinter.StringVar()
    tkinter.Entry(win1, textvariable=sheet_text1).place(x=110, y=30)
    tkinter.Entry(win1, show="*", textvariable=sheet_text2).place(x=110, y=70)
    tkinter.Entry(win1, show="*", textvariable=sheet_text3).place(x=110, y=110)
    # 创建按钮
    tkinter.Button(win1, text="确认注册", command=None).place(x=150, y=150)
    # 循环
    win1.mainloop()


def login_window():
    # 创建注册窗口
    tk = tkinter.Tk()
    # 窗口大小
    tk.geometry("350x200")
    # 设置窗口大小固定
    tk.resizable(0, 0)
    # 设置窗口背景图
    photo = tkinter.PhotoImage(file="backgr.gif")
    label = tkinter.Label(tk, image=photo)  # 图片
    label.pack()
    # 创建账号密码标签
    tkinter.Label(tk, text='账号', ).place(x=50, y=40)
    tkinter.Label(tk, text='密码', ).place(x=50, y=80)
    tkinter.Button(tk, text="注册", command=register_window).place(x=120, y=130)
    # 创建输入框
    sheet_text1 = tkinter.StringVar()
    sheet_text2 = tkinter.StringVar()
    tkinter.Entry(tk, textvariable=sheet_text1).place(x=110, y=40)
    tkinter.Entry(tk, show="*", textvariable=sheet_text2).place(x=110, y=80)
    # 创建按钮
    tkinter.Button(tk, text="登录", command=None).place(x=200, y=130)
    # 循环
    tk.mainloop()

def main_window():
    # 创建注册窗口
    main = tkinter.Tk()
    # 窗口大小
    main.geometry("260x600")
    main.mainloop()




login_window()
# register_window()
# main_window()