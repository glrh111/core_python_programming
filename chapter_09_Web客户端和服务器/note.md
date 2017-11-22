# Web客户端和服务器

## Python Web客户端工具

urlparse 模块: 处理URL字符串的相关函数

## Web 服务器

Django, Google App Engine 都基于 BaseHTTPServer 模块

相关的模块和类

模块| 描述
---|---
BaseHTTPServer | 提供基本的Web服务器和处理程序类, HTTPServer, BaseHTTPRequestHandler
SimpleHTTPServer | 含有SimpleHTTPRequestHandler , 用于处理HEAD 和 GET请求
CGIHTTPServer | 含有CGIHTTPRequestHandler, 用于处理POST请求并执行CGI
http.server | Python3中的, 含有以上三个的功能

### 一个简单的Web服务器


### 一个简单的CGI Web服务器

## 相关模块

模块/包 | 描述
---|---
Web应用程序 | 
cgi | 从标准网关接口(CGI)获取数据
cgitb | 处理CGI返回数据
htmllib | 解析简单的html文件
HTMLparser | 新的HTML, XHTML解析器, 不基于SGML
htmlentitydefs | 一些HTML普通实体定义
Cookie | 服务端cookie
cookielib | HTTP客户端的cookie处理类
webbrowser | 控制器: 向浏览器加载Web文档
sgmllib | 解析sgml
robotparser | 解析robot.txt文件
httplib | 创建HTTP客户端
urllib | 访问服务器
urlparse, urllib.parse | 解析URL的字符串工具
XML处理 | 
xmllib | 已经废弃
xml | 包含很多解析器的xml包
xml.sax | 
xml.dom | dom解析器
xml.etree | 树形的XML解析器
xml.parsers.expat | 非验证型Expat XML解析器接口
xmlrpclib | 通过HTTP提供XML 的RPC客户端
SimpleXMLRPCServer | xml-RPC 基本服务器框架
DocXMLRPCServer | 自描述xml-RPC服务器框架
Web服务器 | 
BaseHTTPServer | 开发Web服务器的抽象类
SimpleHTTPServer | 处理最简单的HTTP请求
CGIHTTPServer |　还可以处理ＣＧＩ请求
ｈｔｔｐ.ｓｅｒｖｅｒ |
wsgiref | 定义Ｗｅｂ服务器和Ｐｙｈｔｏｎ　Ｗｅｂ应用程序标准接口的包
第三方｜
ＨＴＭＬｇｅｎ　｜　协助ＣＧＩ将Ｐｙｔｈｏｎ对象转换为ＨＴＭＬ
ｂｓ　｜　
Mechanize | Ｗｅｂ浏览包

