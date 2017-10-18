# Flask Web 开发

## 概述

### Flask流行的原因

+ 文档齐全，上手方便
+ 扩展方便，全面，实现简单
+ 社区活跃度非常高
+ 微框架形式给开发者更大的选择空间
+ Flask和相关依赖设计优秀

### 主要依赖三个库

+ Jinja2 模板引擎
+ Werkzeug 一个包含WSGI，路由，调试的工具集
+ itsdangerous 给予Django相关模块的签名实现

## 开发简介

### 配置管理

app.config 是一个 flask.config.Config 实例。继承自dict

```python
# 1. 从文件读取
app.config.from_object('settings') # 模块名字

import settings
app.config.from_object(settings)

# 2. 通过文件名字加载
app.config.from_pyfile('settings.py', silent=True)

# 3. 通过环境变量加载
export ENV='wocao.py'
app.config.from_envvar('ENV')
```

### 调试模式

修改代码后自动重启服务

```python
app.debug = True
app.run()

app.run(debug=True)

# 注意调试码 PIN Personal Identification Number 
```

### 动态URL匹配

```python
@app.route(converter:variable_name)
# string 没有 / 的文本。默认
# int    整数
# float  浮点数
# path   和默认相似，接收 /
# uuid   只接受uuid字符串
# any    可以指定多种路径，但是需要传入参数

```

### 自定义URL转换器

自定义的converter。按照某种规则，将variable_name 转换为参数

```python
# 继承一个 werkzeug.routing.BaseConverter 的类，
# 并且实现 to_url __init__ to_python 三个方法

```

### 唯一URL

如果endpoint 末尾带斜线 / 的话，访问时，加不加斜线都可以访问到；

反之则不行。

### 构造URL url_for

```python
url_for('function_name', ...)
# 接受函数名作为第一个参数，位置的变量将作为url末尾的查询参数

from flask import Flask, url_for
app = Flask(__name__)

@app.route('/item/1/')
def item(id):
    pass
    
with app.test_request_context():
    print url_for('item', id=1)
    print url_for('item', id=2, next='/')

# /item/1/?id=1
# /item/1/?id=2&next=%2F
```

### 跳转和重定向

301 永远转移 302 临时转移

```python
from flask import redirect

redirect(location) # 默认302
redirect(location, code=301) # 303, 305, 307
```

### 响应

视图函数的返回值，会被自动转换为一个响应对象，转换逻辑如下：

+ 合法的响应对象，直接返回
+ 字符串，200 text/html 的werkzeug.wrappers.Response
+ 元组，(response, status, headers) 形式。
+ 否则，Flask会假设返回值是一个合法的WSGI应用程序，
通过Response.force_type(rv,request.environ)转换为一个请求对象

```python
# 响应 JSON
from flask import Flask, jsonify
from werkzeug.wrappers import Response
app = Flask(__name__)


class JsonResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, dict):
            response = jsonify(response)
        return super(JsonResponse, cls).force_type(response, environ)
        
app.response_class = JsonResponse
        
@app.route('/')
def hello_world():
    return {'message': 'hello'}


@app.route('/custom_headers')
def cus():
    return {'headers': [1,2,3]}, 201, [('X-Request-Id', '100')]

```

### 静态文件管理

使用 url_for 生成路径：

url_for('static', filename='style.css') -> /static/style.css

定制静态文件真实目录：

app = Flask(__name__, static_folder='/tmp')

url中还是访问 /static/ 会被定位到 tmp 这个真是目录里边。

### 即插视图

灵感来自Django。

#### 标准视图

继承自 flask.views.View 的类

#### 基于调度方法的视图

flask.views.MethodView

### 蓝图 BlurPrint

Blurprint 实现了应用的模块化，使用蓝图让应用层次清晰。

bp = Blueprint('user', __name__, url_preffix='user')

app.register_blueprint(bp)

### 子域名

app.config['SERVER_NAME'] = 'example.com:9000'

...

### 命令行接口

flask 命令 参考page 75

这里有一些问题

### 模板

#### string.Template

```python
from string import Template

s = Template("$who likes what")
s.substitute(who="wang", what="cao")

# 而且支持自定义模板，定制分隔符等
# 不能写控制语句，无法继承重用等。
```

#### Jinja2

仿Django模板的一个模板引擎。优点如下：
+ 让HTML设计者和后端Python开发工作分离
+ 减少使用Python的复杂程度。页面逻辑应该独立于业务逻辑。
+ 模板非常灵活、快速、安全。
+ 提供了控制语句、继承等高级功能。

模板加载器的概念

```python
from jinja2 import Template, Environment, PackageLoader
template = Template("Hello {{name}}")
template.render(name="wanger")

# 用于存储配置、全局对象
env = Environment()
```

#### Jinja2 的基本语法

#### 模板继承

extends

#### 赋值

#### include 包含一个模板

#### import 导入宏

### Mako 

从Django, Jinja2, Genshi 等模板借鉴了很多语法和API。优点如下：
+ 性能和Jinja2相当
+ 有大型网站在使用。Reddit，豆瓣
+ 有知名Web框架支持。Pylons，Pyramid内置Mako。
+ 支持在模板中写几乎原生的Python语法的代码，对Python工程师友好
+ 自带完整的缓存系统。且很容易切换成其他的缓存系统。

与Jinja2最大的区别：
jinja2 不提倡在模板里边 写逻辑，而Mako在这方面没有限制。

#### 基本的API使用

```python
# 使用缓存：
Template(filename='', module_directory='').render(name="wocao")
缓存的文件，是按照模板的文件结构传的
编译后的模板后缀是 .py
```

#### TemplateLookup

处理模板继承，引用...的

```python
from mako.lookup import TemplateLookup
from mako.template import Template
mylookup = TemplateLookup(directories='templates/chapter...')
template = Template('<%include file="hello.mako"/>', lookup=mylookup)

template.render(name="wocao")
```

#### Mako的基本语法

具体参见参考书 87页

#### 过滤器

${ "some text" | u }

常用的过滤器：
+ u: URL 转换
+ h: HTML转换。将< 转换为 &lt 之类
+ trim: 过滤行首尾的空格
+ n: 禁止默认的过滤器

自定义过滤器

```python
<%! 
    def div(text):
       return "<div>" + text + "</div>"
%>
Here's a div ${"wocao" | div }
```

可以指定全局过滤器

#### 模板继承

#### Mako排错

出现NameError 错误的解决方法：

mako.template.py 中 def _compile() 函数末尾加上：

for index, s in enumerate(source.splitlines()):
    print index, s
    
从而便于定位原因。

### 使用MySQL

mysql-python sqlalchemy

#### 记录慢查询

可以利用相关工具，将慢查询记录到日志里边。page104

### 理解Context

应用上下文  请求上下文

#### 本地线程

Thread Local 

本地线程实现原理，在 threading.current_thread().__dict__ 里边添加一个包含对象mydata的id值的key，来保存不同线程的状态。

#### Werkzeug 的Local

Werkzeug实现了自有的本地线程。 werkzeug.local.Local 和 threading.local 的主要区别如下：

+ 使用自定义 __storage__ 保存不同线程的状态
+ 提供了释放本地线程的release_local 方法
+ get_ident 函数。可以使用greenlet轻量级协程

Werkzeug 还实现了两种数据结构：
+ LocalStack 基于werkzeug.local.Local 实现的栈
+ LocalProxy 标准的代理模式。构造此结构时接受一个可以调用的参数（一般是函数），这个函数执行后就是通过LocalStack实例化的栈的栈顶对象。
对于LocalProxy对象的操作，实际上都会转发到这个栈顶对象(也就是一个LocalThread对象上)。

#### flask.request

```python
# 相关代码解析

# 1. 业务代码例子
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def people():
    name = request.args.get('name')

# 疑问：request 如何在运行时获取请求的上下文？
# 2. 这段代码的工作原理

from functools import partial
from werkzeug.local import LocalProxy

def _lookup_req_object(name):
    top = _request_ctx_stack.top
    if top is None:
        raise RuntimeError('working outside of context')
    return getattr(top, name)


request = LocalProxy(partial(_lookup_req_object, 'request'))

# 1）用户访问产生请求
# 2）在发生请求的过程中向 _request_ctx_stack 推入这个请求上下文的对象，它会变成栈顶。
#    request就会称为这个请求的上下文，也就包含了这次请求相关的信息和数据。
# 3）在视图函数中使用request就可以使用 request.args.get('name') 了
```

### 使用上下文 context

使用上下文的典型应用场景，是缓存一些在发生请求之前要使用的资源。
比如生成数据库连接和缓存一些对象；请求上下文发生在HTTP请求开始，WSGI Server 调用 Flask.__call__()之后。

应用上下文不是应用启动之后生成的唯一上下文。

请求上下文和应用上下文，在WEb应用环境中，是一一对应的。都是本地线程的。区分他们的意义如下：
+ 中间件 DiapatcherMiddleware , 支持多个app共存，所以app之间也需要隔离
+ 非Web模式下，一个应用上下文可以有多个请求上下文。

flask的4个上下文变量：
+ flask.current_app 应用上下文。当前app实例对象
+ flask.g 应用上下文。处理请求时用作临时存储的对象
+ flask.request 请求上下文。封装了客户端发出的HTTP请求的内容。
+ flask.session 请求上下文。存储了用户会话

#### 使用LocalProxy 代替 g

自己实现一个全局可访问的 current_user, 感受一下 LocalStack 和 LocalProxy 怎么工作。

```python
# 实现全局可以访问的 current_user

from werkzeug.local import LocalStack, LocalProxy

_user_stack = LocalStack()

def get_current_user():
    top = _user_stack.top
    if top is None:
        raise RuntimeError()
    return top

current_user = LocalProxy(get_current_user)

from flask import Flask
app = Flask(__name__)

@app.before_request
def before_request():
    users = []
    user = 1
    _user_stack.push(user)

@app.teardown_appcontext
def teardown():
    _user_stack.pop()
    
@app.context_processor
def template_extras():
    return { 'current_user': current_user, 'enumerate': enumerate }
    
```

## 从0开始，实现一个文件托管服务

+ 上传后的文件可以永久存放
+ 上传后的文件有一个功能完备的预览页面。文件大小，文件类型，上传时间，下载地址，短链接等信息。
+ 可以通过参数对图片进行上传和剪切
+ 相同文件不重复上传

依赖如下包：
+ ubuntu: libjpeg8-dev
+ pip: 
  - python-magic
  - Pillow PIL的继承和替代品 
  - cropresize2 剪切和调整图片大小
  - short_url 创建短链接
  









