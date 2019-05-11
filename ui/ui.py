from tkinter import *
from tkinter import ttk
from client import *
import tkinter.messagebox
from tkinter import scrolledtext


class Application:
    def __init__(self, master):
        self.root = master
        # 窗口大小
        self.root.geometry("350x200")
        # 设置窗口标题
        self.root.title("登录")
        # 设置窗口不可变
        self.root.resizable(0, 0)
        self.login_window()
        self.list0 = []

    def login_window(self):  # 创建登录窗口
        # 设置窗口背景图
        self.photo = PhotoImage(file="b.png")
        self.label = Label(self.root, image=self.photo)
        self.label.pack()

        # 创建账号密码标签
        Label(self.root, text='账号', ).place(x=50, y=40)
        Label(self.root, text='密码', ).place(x=50, y=80)

        # 创建输入框
        text1 = StringVar()
        text2 = StringVar()
        Entry(self.root, textvariable=text1, ).place(x=110, y=40)
        Entry(self.root, show="*", textvariable=text2).place(x=110, y=80)
        # 创建按钮
        Button(self.root, text="注册", command=self.register_window).place(x=120, y=130)
        Button(self.root, text="登录", command=lambda: self.send_data(text1.get(), text2.get())).place(x=200, y=130)

    def close_window(self):
        self.list0[0].destroy()
        del self.list0[0]

    def register_window(self):  # 创建注册窗口
        if len(self.list0) > 0:
            self.list0[0].deiconify()
            return
        self.reg = Toplevel()
        # 窗口大小
        self.reg.geometry("350x230")
        # 设置窗口大小固定
        self.reg.resizable(0, 0)
        # 设置窗口标题
        self.reg.title("注册")
        self.list0.append(self.reg)
        # 设置窗口背景图
        photo = PhotoImage(file="b.png")
        label = Label(self.reg, image=photo)  # 图片
        label.pack()
        # 创建账号密码标签
        Label(self.reg, text='昵称').place(x=50, y=30)
        Label(self.reg, text='账号').place(x=50, y=70)
        Label(self.reg, text='密码').place(x=50, y=110)
        Label(self.reg, text='确认密码').place(x=26, y=150)
        # 创建输入框
        text1 = StringVar()
        text2 = StringVar()
        text3 = StringVar()
        text4 = StringVar()
        Entry(self.reg, textvariable=text1).place(x=110, y=30)
        Entry(self.reg, textvariable=text2).place(x=110, y=70)
        Entry(self.reg, show="*", textvariable=text3).place(x=110, y=110)
        Entry(self.reg, show="*", textvariable=text4).place(x=110, y=150)
        # 创建按钮
        Button(self.reg, text="确认注册",
               command=lambda: self.send_data(text2.get(), text3.get(), text4.get(), text1.get())).place(
            x=150, y=180)
        # 点击关闭按钮触发事件
        self.reg.protocol("WM_DELETE_WINDOW", lambda: self.close_window())

        # 循环
        self.reg.mainloop()

    def send_data(self, user, passsword1, passsword2=None, name=None):
        """
            发送数据给客户端
        :param user: 用户名
        :param passsword1: 密码
        :param passsword2: 确认密码
        :return:
        """
        if passsword2 == None:
            # 登录成功
            self.login_successfully()
        else:
            q = ClientManager()
            a = q.register(user, passsword1, passsword2, name)
            tkinter.messagebox.showinfo(title='提示', message=a)
            self.list0[0].deiconify()
        # if passsword2 == None:
        #     # 登录成功
        #     self.login_successfully()
        # if passsword2 != None:
        #     # 注册成功
        #     self.registered_successfully()

    def login_successfully(self):
        # 登录成功
        Message(self.root, text='登录成功，正在跳转，请稍候...', ).place(x=10, y=130)
        # 更新窗口
        self.root.update()
        # sleep(2)
        # 关闭登录窗口
        self.root.destroy()
        # 跳转到主窗口
        MainWindow(self.root)

    def registered_successfully(self):
        # 注册成功
        Label(self.reg, text='注册成功，请关闭本界面返回登录', ).place(x=30, y=140)


class MainWindow:
    def __init__(self, master):
        self.root = master
        # 创建主窗口
        self.root = Tk()
        # 窗口大小
        self.root.geometry("260x600")
        # 设置窗口标题
        self.root.title("主窗口")
        # 设置窗口大小固定
        self.root.resizable(0, 0)
        self.dict = {}
        self.start()

    def start(self):
        a = Frame(self.root, width=500, height=600, bg="#FAF0E6")
        a.pack()
        # b = Frame(self.root, bg="red")
        # b.place(in_=a, x=30, y=20, width=300, height=300)
        # 设置窗口背景图
        # self.photo = PhotoImage(file="timg.png")
        # self.label = Label(in_=a, image=self.photo)
        # self.label.pack()
        # text1 = Text(self.root)
        # text1.place(in_=a, width=500, height=300)
        tree = ttk.Treeview(self.root, )
        tree.place(in_=a, x=30, y=20, width=200, height=500)
        treeF1 = tree.insert("", 0, text="我的好友", values=("我的好友"))
        treeF2 = tree.insert("", 1, text="最近联系", values=("最近联系"))
        treeF1_1 = tree.insert(treeF1, 0, text="中国黑龙江", values=("中国黑龙江"))
        reeF1_2 = tree.insert(treeF1, 1, text="中国吉林", values=("中国吉林"))
        reeF1_3 = tree.insert(treeF1, 1, text="中国广东", values=("中国广东"))
        treeF2_1 = tree.insert(treeF2, 0, text="中国黑龙江", values=("中国黑龙江"))
        tree.bind("<Double-1>", self.dblclickAdaptor(self.dblclick, tree=tree))

        Button(self.root, text="添加好友", command=self.add_friend).place(x=30, y=530)
        Button(self.root, text="创建群", command=None).place(x=110, y=530)
        Button(self.root, text="加入群", command=self.join_group).place(x=180, y=530)

    def dblclickAdaptor(self, fun, **kwds):
        return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)

    def dblclick(self, event, tree):
        item = tree.selection()[0]
        name = tree.item(item, "values")[0]
        if name != "我的好友" and name != "最近联系":
            self.chat_window(name)

        # print("you clicked on ", tree.item(item, "values"))
        # print(tree.item(item, "values")[0])

    def window_exist(self, name):  # 判断窗口是否已存在
        # 如果窗口存在，则显示该窗口

        if name in self.dict:
            self.dict[name].deiconify()
            return True

    def chat_window(self, name):  # 创建聊天窗口
        # 判断窗口是否已存在
        if self.window_exist(name):
            # 窗口存在则返回
            return
        # 创建聊天窗口
        self.chat = Toplevel()
        self.dict[name] = self.chat
        # 窗口大小
        self.chat.geometry("580x400")
        # 设置窗口大小固定
        self.chat.resizable(0, 0)
        # 设置窗口标题
        self.chat.title("与%s聊天" % name)

        message_block = Frame(self.chat, width=580, height=400, bg="#D3D0C6")
        message_block.pack()
        # 聊天信息块
        # text1 = Text(self.chat, )
        # text1.place(in_=message_block, x=10,y=10,width=380, height=250)
        # 发送信息块
        text2 = Text(self.chat, )
        text2.place(in_=message_block, x=10, y=270, width=380, height=100)

        text3 = Text(self.chat, )
        text3.place(in_=message_block, x=400, y=10, width=170, height=380)
        self.scroll = Scrollbar()


        scr = scrolledtext.ScrolledText(self.chat, width=70, height=13, font=("隶书", 18))
        scr.place(in_=message_block, x=10, y=10, width=380, height=250)  # 滚动文本框在页面的位置
        # 设置文本框不可编辑
        scr.config(state=DISABLED)

        # 发送按钮
        b = Button(self.chat, text="发送", command=lambda: self.recv_message(scr, text2.get("1.0", END)))
        b.place(in_=message_block, width=30, height=22, x=350, y=375)
        # 更新聊天信息
        # self.recv_message(text1, "3546843")

        # 点击关闭按钮触发事件
        self.chat.protocol("WM_DELETE_WINDOW", lambda: self.close_window(name=name))
        self.chat.mainloop()

    def recv_message(self, text, msg):  # 接收信息
        # 设置文本框可编辑
        text.config(state=NORMAL)
        # 插入信息
        text.insert(END, msg)
        # 显示文本框最近的信息
        text.see(END)
        # 设置文本框不可编辑
        text.config(state=DISABLED)

    def close_window(self, name):  # 关闭窗口
        self.dict[name].destroy()
        del self.dict[name]

    def add_friend(self):
        # 判断窗口是否已存在
        if self.window_exist("添加好友"):
            # 窗口存在则返回
            return
        # 创建加好友窗口
        self.af = Toplevel()
        # 窗口大小
        self.af.geometry("400x130")
        # 设置窗口大小固定
        self.af.resizable(0, 0)
        # 设置窗口标题
        self.af.title("添加好友")
        self.dict["添加好友"] = self.af
        Label(self.af, text='输入好友账号').place(x=50, y=40)
        text1 = StringVar()
        Entry(self.af, textvariable=text1).place(x=130, y=40)
        Button(self.af, text="添加好友", command=None).place(x=300, y=40)
        # 点击关闭按钮触发事件
        self.af.protocol("WM_DELETE_WINDOW", lambda: self.close_window(name="添加好友"))

    def join_group(self):
        # 判断窗口是否已存在
        if self.window_exist("加入群聊"):
            # 窗口存在则返回
            return
        # 创建加群窗口
        self.af = Toplevel()
        # 窗口大小
        self.af.geometry("400x130")
        # 设置窗口大小固定
        self.af.resizable(0, 0)
        # 设置窗口标题
        self.af.title("加入群聊")
        self.dict["加入群聊"] = self.af
        Label(self.af, text='输入群号').place(x=50, y=40)
        text1 = StringVar()
        Entry(self.af, textvariable=text1).place(x=130, y=40)
        Button(self.af, text="加入群聊", command=None).place(x=300, y=40)
        # 点击关闭按钮触发事件
        self.af.protocol("WM_DELETE_WINDOW", lambda: self.close_window(name="加入群聊"))


if __name__ == '__main__':
    root = Tk()
    Application(root)
    root.mainloop()
