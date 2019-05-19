# -*- coding: UTF-8 -*-
# 获取ODBC数据源列表
from tkinter import *
from tkinter import ttk
import win32api, win32con


def GetODBCdsn():
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,
                              'SOFTWARE\\ODBC\\ODBC.INI\\ODBC Data Sources', 0, win32con.KEY_ALL_ACCESS)
    # print(key)
    # print(win32api.RegQueryValue(key,''))
    # print('返回项的子项数目、项值数目，以及最后一次修改时间',win32api.RegQueryInfoKey(key))
    subitem, item, opdate = win32api.RegQueryInfoKey(key)
    dsnlist = []
    for i in range(item):
        print('---', win32api.RegEnumValue(key, i))
        dsnName, dsnObject, dsnType = win32api.RegEnumValue(key, i)
        dsnlist.append(dsnName)
    # print(dir(win32api))
    win32api.RegCloseKey(key)
    return dsnlist


class MFrame(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        self.master = master
        self.master.title('获取用户定义的数据源')
        self.combo = ttk.Combobox(self.master)
        self.combo.config(state="readonly")
        self.combo.pack(side=TOP, fill='x', expand=False)
        self.combo.update_idletasks()
        comlist = GetODBCdsn()
        self.combo['values'] = comlist


def test():
    GetODBCdsn()


def main():
    root = Tk()
    mf = MFrame(root)
    root.mainloop()


if __name__ == "__main__":
    # test()
    main()
