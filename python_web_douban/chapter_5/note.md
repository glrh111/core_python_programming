# REST 和 Ajax

## REST 架构风格最主要的5个约束

+ 客户端/服务端. 基本的分布式。
+ 无状态. 通信的会话状态应该全部由客户端维护，即请求中包含了全部必要的信息。
+ 缓存. 无状态表示可能出现重复的请求，这些请求只需要第一次真正的执行。。。
+ 统一接口. 每个REST应用都共享一套通用架构。
+ 分层系统. 将系统划分为几个部分，每个部分负责一部分相对单一的职责，
然后通过上层对下层的依赖和调用组成一个完整的系统。通常可以划分为如下三层：
  + 应用层：负责返回JSON数据和其他业务逻辑
  + 服务层：为应用层提供服务支持，如全站的账号系统，以及文件托管服务等
  + 数据访问层：提供数据访问和存储的服务，如数据库，缓存系统，文件系统，搜索引擎

REST就是这一系列设计约束的集合，如果一个架构符合REST原则，就称它为RESTful架构。

## RESTful API 设计指南
 
### 使用名词表示资源 URI里边不应该含有动词

+ GET /getusers/1 错误
+ GET /users/1/get 错误
+ GET /users/1
+ PUT /users/

### 关注请求头

如果服务端只返回JSON数据，而客户端的Accept为application/xml, 那么应该返回406

### 合理使用请求方法和状态码

+ PUT 完整替换资源，或者创建指定身份的资源
+ PATCH 用于局部更新资源
+ DELETE 删除资源，之后返回204 Not Content

### 正确地使用REST

以分页功能为例，服务端需要返回 X-Total-Count 这个头来通知符合条件的条数；
Link头来告知返回相邻页码的信息

### 对输出结果不再包装

body中应该直接放数据，不要多层封装。不恰当的例子如下：

```
HTTP/1.1 200 OK
{
    "success": true,
    "data": { "id": 1, "name": "wocao" }
}

应该如下：
{
    "id": 1, "name": "wocao"
}

因为请求资源是否成功，通过状态码可以得知。
```

### 不要做出错误的提示

如果方位出错，不应该返回200，因为客户端可能对此做缓存；尽管body里边可能包含错误原因。

### 使用嵌套对象

对象的所有字段不应该只在一个层次上。

### 版本

常见的区分版本的方法有三种：
+ 保存在URI中：http://aaa.com/api/v2
+ 放在请求头中：Accept: application/vnd.github.v3+json
+ 自定义请求头：X-API-Version: 1

第三种方式不推荐，推荐第一种

### URI 失效和迁移

随着业务发展，会出现一些API失效或者迁移，
对失效的API，应该返回404 Not Found 或者 401 Gone；
对迁移的API，应该返回301重定向。(并带上Location)

### 信息过滤

URL最好越简短越好。对结果的过滤，排序和搜索相关的功能，都应该通过参数实现。

+ offset=0&limit=10 指定返回记录的数量
+ offset=10 指定返回记录的开始位置
+ page=2&perpage=200 指定第几页
+ sortby=name&order=asc
+ sort=age,asc

### 速度限制

为了避免请求泛滥，给API设置速度限制很重要。
RFC 6585 引入了HTTP状态码429(Too Many Request).
下面是一些提示：
+ X-RateLimit-Limit: 当前时间段允许的并发请求数
+ X-RateLimit-Remaining: 剩余的
+ X-RateLimit-Reset: 当前时间段剩余的秒数

### 缓存

数据内容在一段时间内不会变动，这个时候我们就可以合理减少HTTP相应内容。
应该在响应头中携带: Last-Modified, ETag, Vary, Date 等信息，
客户端可以再随后请求这些资源时，在请求头中使用If-Modified-Since,
If-None-Match 等来确认资源是否经过修改。
如果资源没有做过修改，那么就可以响应 304 Not Modified, 并且不在响应实体中返回任何内容。

当生成请求的时候，在HTTP头里边加上ETag，其中包含请求的校验和Hash值，
这个值在输入变化的时候也应该变化。此时API应该返回 304 Not Modified
而不是常规的输出结果。

### 并发控制

缺少并发控制的PUT和PATCH请求，可能导致更新丢失。这个时候可以使用
Last-Modified 和 ETag头来实现t条件请求。具体原则如下：
+ 客户端请求中如果没有 If-Unmodified-Since或者If-Match 头，
就返回状态码403 Forbidden ,在body里边解释为何
+ 客户端发起的请求所提供的 If-Unmodified-Since或者If-Match头，
与服务器记录的实际修改时间，或者ETag，不匹配，返回
412 Precondition Failed
+ 客户端发起的请求所提供的 If-Unmodified-Since或者If-Match头，
与服务器记录的实际修改时间或者ETag的历史值匹配，但资源已经被修改过，
返回409 Conflict
+ 条件符合实际值，就更新资源；响应200 Ok或者204 No Content
并且包含更新过的Last-Modified 或者ETag头，同时包含
Content-Location , 值为更新后的资源URI

### 以上内容参考来源

```
# HTTP接口设计指北
http://bit.ly/2azgIBP
即
https://github.com/bolasblack/http-api-guide
```

## 使用Ajax

### 使用fetch来实现ajax

```javascript
// 原生XHR
var data = FormData();
data.append('username', $username);
data.append('password', $password);

var xhr = new XMLHttpRequest();
xhr.open('POST', '/signin');

xhr.onreadystagechange = function() {
  if (xhr.readyState == 4 && xhr.status == 200) {
      var data = JSON.parse(xhr.responseText);
      if (!data.r) {
          $result.html(data.rs);
      } else {
          $result.html(data.error);
      }
  }
};

xhr.send(data);

// 使用fetch的写法 ES6(ES2015)
fetch('/signin', {
    method: 'POST',
    body: data
}).then(function(response) {
  return response.json();
}).then(function(data) {
  if (!data.r) {
      $result.html(data.rs);
  } else {
      $result.html(data.error);
  }
});

// polyfill
// github.com/github/fetch
// 这个文件：
// https://github.com/github/fetch/blob/master/fetch.js
 
// 使用ES7的写法 async/await
try {
    let response = await fetch('/signin', {
        method: 'POST',
        body: data
    });
    let data = await response.json();
    if (!data.r) {
      $result.html(data.rs);
    } else {
      $result.html(data.error);
    }
} catch(e) {
    console.log("Opps, error", e);
}
```



