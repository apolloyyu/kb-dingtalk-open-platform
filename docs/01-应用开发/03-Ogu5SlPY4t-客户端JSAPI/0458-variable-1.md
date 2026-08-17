---
title: "变量"
source_url: "https://open.dingtalk.com/document/development/variable-1"
namespace: "development"
slug: "variable-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 框架 > SJS语法参考 > 变量"
doc_id: "0xkAkOqsdP"
updated_at: "2025-09-17 20:58:01"
---

> Source: https://open.dingtalk.com/document/development/variable-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 框架 > SJS语法参考 > 变量
> Updated: 2025-09-17 20:58:01

# 变量

SJS 中的变量均为值的引用。

## 语法规则

- var 与 JavaScript 中表现一致，会有变量提升。
- 支持 const 与 let，与 JavaScript 表现一致。
- 没有声明的变量直接赋值使用，会被定义为全局变量。
- 只声明变量而不赋值，默认值为 `undefined`。

示例代码：

```
var num = 1;
var str = "hello dingtalk";
var undef; // undef === undefined
const n = 2;
let s = 'string';
globalVar = 3;
```

## 变量名

**命名规则**

变量命名必须符合下面两个规则：

- 首字符必须是：字母（a-z,A-Z），下划线（\_）。
- 首字母以外的字符可以是：字母（a-z,A-Z），下划线（\_），数字（0-9）。

**保留标识符**

与 Javascript 语法规则一致，以下标识符不能作为变量名：

```
arguments
break
case
continue
default
delete
do
else
false
for
function
if
Infinity
NaN
null
require
return
switch
this
true
typeof
undefined
var
void
while
```
