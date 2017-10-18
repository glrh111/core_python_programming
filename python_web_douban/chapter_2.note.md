# 第二章 基本配置

## pip 高级用法

### pip 自动补全

`pip completion --bash >> ~/.profile`

### 作为普通用户安装包

`pip install django --user`

`pip show django | grep Location`

### 编辑模式

可以用在git上下载pip包，使在本地生效

`pip install -e .`

### 使用devpi作为pip缓存代理服务器

`pip install devpi-server`

`devpi-server`

`pip install -i http://localhost:3141/root/pypi tornado`

将缓存服务器设置为特定地址的方法：

`mkdir ~/.config/pip -p`

```
cat ~/.config/pip/pip.conf

[global]
index-url = http://http://localhost:3141/root/pypi/+simple/
```

安装类似pypi的web界面:

`pip install devpi-web`

重启devpi-server服务，即可访问3141端口，访问web界面。

### Pypi完全镜像

bandersnath 可以帮助我们建立一个包含全部包的本地镜像服务器。


