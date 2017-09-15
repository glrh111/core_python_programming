#! /usr/bin/env python
# coding: utf-8

import Tkinter

def resize(ev=None):
    label.config(font="Helvetica -{} bold".format(scale.get()))
    pass

root = Tkinter.Tk()
root.geometry('250x150')

# 一个标签
label = Tkinter.Label(root, text="hello, world!", font="Helvetica -12 bold")
label.pack()

# 一个滑块
scale = Tkinter.Scale(root, from_=10, to=40, orient=Tkinter.HORIZONTAL, command=resize)
scale.pack(fill=Tkinter.X, expand=1)

# 退出按钮
quit = Tkinter.Button(root, text="quit", command=root.quit, bg='green', fg='white')
quit.pack(fill=Tkinter.X, expand=1)

Tkinter.mainloop()