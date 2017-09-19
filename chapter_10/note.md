# Web编程: CGI和WSGI

> WSGI主要有利于Web框架和Web服务器的作者, 不是Web应用的作者. WSGI不是一个应用程序API, 而是框架与服务器之间的粘合API.

CGI: Common Gateway Interface

WSGI: Web Server Gateway Interface

## CGI简介

客户端 <-> Web服务器 <-> CGI应用程序

### 构建Web服务器

生产环境中的服务器: Apache, ligHTTPD, thttpd等

开发人员服务器: `python -m CGIHTTPServer [port]`

`python -c "import CGIHTTPServer; CGIHTTPServer.test()"`

启动服务的目录作为根目录, cgi-bin下的py脚本会在访问时执行; 其他文件作为文本文件返回.

这些文件需要: 
1. x权限
2. \#! 声明
3. 写入头文件神马的


## WSGI简介

### CGI的缺点

1. 每次处理请求时, 需要创建CGI进程, 就是一个Python解释器, 无法同时处理大量请求.
   可以通过服务器集成和外部进程解决.
2. 服务器无法创建动态内容. (这个有疑问)

### 1. 服务器集成

服务器API. 如NSAPI, ISAPI, Apache Web Server

模块: 服务器上插入的编译后的组件, 这些组件可以扩展服务器的功能和用途.

这仨个解决方案, 都将网关集成进入服务器, 生成函数调用, 运行应用程序代码, 在运行过程中响应. 

相当于将语言解释器作为插件集成到服务器里边了, 减少了加载解释器的开销.

### 2. 外部进程

CGI应用在服务器外部一直运行, 当有请求时, 服务器将这个请求传递到外部进程中.

FastCGI

### WSGI PEP333

在Web服务器和Web框架层之间提供一个通用的API标准, 减少之间的互操作性, 并形成统一的调用方式.

wsgi的应用是可调用对象, 参数固定为以下两个: 
1. 含有服务器环境变量的字典
2. 可调用对象(函数..)

### WSGI服务器

wsgiref.simple_server.WSGIServer  提供了一个参考服务器

### 中间件及封装WSGI应用

在应用程序运行之前或者之后运行的一些处理程序, 叫做中间件.

## 生产环境中的Web开发

可以使用现成的框架








