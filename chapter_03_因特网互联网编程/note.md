# 因特网互联网编程

## 文件传输

### 文件传输互联网协议

1. 文件传输协议: FTP
2. UNIX到UNIX复制协议: UUCP
3. 超文本传输协议: HTTP
4. 远程文件复制协议: rcp, scp, rsync

### 文件传输协议FTP RFC959

用户名密码登录, 或者匿名登录(anonymous)

## 网络新闻

### Usenet 与 新闻组

### 网络新闻传输协议 NNTP :119 RFC977

nntplib

## 电子邮件  RFC2822

电子邮件由头字段(消息标题), 以及后面可选的正文组成.

消息传输代理: MTA

### 发送电子邮件

简单邮件传输协议: SMTP simple mail transfer protocol

为了发送电子邮件, 邮件客户端必须连接到一个MTA, MTA靠某种协议进行通信, 通过MTS(消息传输系统)进行通信.

#### SMTP ESMTP LMTP 

SMTP RFC821 RFC1869 RFC5321

#### MTA

开源MTA: sendmail, postfix, exim, qmail

商业MTA: Exchange, Lotus ....

#### Python的smtplib

### 接收电子邮件

MUA 邮件用户代理 Mail User Agent

可以周期性将邮件下载到本地计算机上

### POP 和 IMAP

POP 一种用于下载邮件的邮局协议: Post Office Protocol RFC918

poplib

目的是让用户的工作站, 可以访问邮箱服务器里面的邮件, 并通过SMTP发送邮件.

IMAP 因特网消息访问协议: Internet Message Access Protocol, 比POP功能更加完善.

imaplib: IMAP4, IMAP4_SSL, IMAP4_stream

### 

