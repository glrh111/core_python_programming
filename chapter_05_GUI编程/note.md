# GUI编程

## 简介

### Tcl, Tk, Tkinter

Tcl: Tool Command Language 工具命令语言

Tk 工具包最初为Tcl设计开发, 后移植到很多其他脚本语言. Perl(Perl/Tk), Python(Tkinter)

Python2 Tkinter, Python3: tkinter

### C/S架构

窗口系统是服务器, 运行在该环境中的GUI程序相当于客户端.

## Tkinter

下面5个步骤: 
1.导入 Tkinter 模块(或 from Tkinter import *)
2.创建一个顶层窗口对象,用于容纳整个 GUI 应用。
3.在顶层窗口对象之上(或者“其中”)构建所有的 GUI 组件(及其功能)
4.通过底层的应用代码将这些 GUI 组件连接起来。
5.进入主事件循环

### 窗口和控件

一些独立的GUI组件

Tkinter.Tk() 只是创建了一个根窗口, 用于摆放其他控件.

控件有一些相关的行为, 称为事件, GUI类为这些事件的相应称为回调.

### 事件驱动处理

### 布局管理器

tk提供3种布局管理器帮助控件进行定位

1. Placer 比较原始, 需要提供位置和大小
2. Packer 填充法, 主要使用这个
3. Grid 

布局好后, 就可以进入主循环中了: Tkinter.mainloop() 

## Tkinter 示例

## 其他GUI简介

Tix(Tk扩展), Pmw(Python MegaWidgets Tkinter扩展), wxPython(wxWidgets的Python版本), PyGTK(GTK+的Python版本)

