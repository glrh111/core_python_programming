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

### 常见的socket对象方法和属性

名称|描述
---|---
服务器socket方法|
s.bind|绑定地址
s.listen|设置并启动TCP监听器
s.accept|被动接收TCP客户端连接, 一直等待知道连接到达
客户端socket方法|
s.connect|主动发起TCP连接
s.connect_ex|扩展版本.问题会以错误码的形式返回, 而不是抛出异常
普通的socket方法|
s.recv|接收TCP消息
s.recv_into|接收TCP消息到指定的缓冲区
s.send|发送TCP消息
s.sendall|完整发送TCP消息
s.recvfrom|接收UDP消息
s.recvfrom_into|UDP消息到缓冲区
s.sendto|发送UDP消息
s.getpeername | 连接到socket的远程地址
s.getsockname | 当前socket的地址
s.getsockopt | 返回给定socket选项的值
s.setsockopt | 设置值
s.shutdown | 关闭连接
s.close | 关闭socket
s.detach | 在未关闭文件描述符的情况下, 关闭socket, 并返回文件描述符
s.ioctl | 控制socket模式(win only)
面向阻塞的socket方法|
s.setblocking | 设置阻塞或非阻塞模式
s.settimeout | 超时时间
s.gettimeout
面向文件的socket方法|
s.fileno | 套接字的文件描述符
s.makefile | 创建与socket关联的文件对象
数据属性
s.family| 
s.type |
s.proto |

### TCP服务器

```python
ss = socket() # 创建服务器套接字
ss.bind()     # 套接字与地址绑定
ss.listen()   # 监听连接
inf_loop:                 # 服务器无限循环
  cs = ss.accept()        # 接受客户端连接
  comm_loop:              # 通信循环
    cs.recv()/cs.send()   # 对话(接收/发送)
  cs.close()              # 关闭客户端套接字
ss.close()                # 关闭服务器套接字
```

调用accepy


