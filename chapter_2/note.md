## 2.3 套接字 socket

两种类型的套接字

1. 基于文件的: AF_UNIX 代表: address family: Unix, 别名AF_LOCAL

2. 面向网络的: AF_INET, AF_INET6

3. 其他Python支持的AF: AF_NETLINK, AF_TIPC

### host:port

端口号有效范围: 0~65535

/etc/services 预留端口号

默认端口号: `http://www.iana.org/assignments/port-numbers`

### 面向连接的套接字, 无连接的套接字

哪种AF都有这两种socket

#### 面向连接的套接字

> 虚拟电路, 流socket. 面向连接的通信提供序列化的, 可靠的, 不重复的数据交付, 没有保存边界记录.
实现这种连接类型的主要协议是传输控制协议(TCP). 

SOCK_STREAM 类型的

#### 无连接的socket

数据包socket, 在通信开始之前不需要建立连接, 消息作为整体发送.

用户数据报协议UDP, SOCK_DGRAM  datagram(数据报)

## Python中的网络编程

常见的socket对象方法和属性

名称|描述
---|---
服务器socket方法|
s.bind|绑定地址
s.listen|设置并启动TCP监听器
s.accept|被动接收TCP客户端连接, 一直等待知道连接到达
客户端socket方法|
s.connect|


