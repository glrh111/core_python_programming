## 具体内容参见 87 页

## 模块级别的块元素。用于引入模块，声明全局变量，全局函数 等 <%! %>
<%!
    from datetime import datetime
    from itertools import repeat
%>

## 集成某个模板
<%inherit file="base.html" />
## 之后可以调用utils里边的函数，变量等
<%namespace name="utils" file="/utils.html"/>

## python 代码块儿 <% %>
<%
    rows = repeat(range(10), 10)
%>

## 将内容插入到当前位置。
<%include file="/nav.html" />

## 下面是两个函数
<%def name="main()">
    ## this is a comment
    <h2>${utils.strftime(datetime.now())}</h2>
    <table>
        % for row in rows:
            ${}makerow(row)}
        % endfor
    </table>
</%def>

<%def name="makerow(row)">
    <tr>
        %for name in row:
            <td>${name}</td>
        %endfor
    </tr>
</%def>
