---
title: "esnext"
source_url: "https://open.dingtalk.com/document/development/esnext-1"
namespace: "development"
slug: "esnext-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 框架 > SJS语法参考 > esnext"
doc_id: "FjDHxppEXs"
updated_at: "2025-09-17 20:58:04"
---

> Source: https://open.dingtalk.com/document/development/esnext-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 框架 > SJS语法参考 > esnext
> Updated: 2025-09-17 20:58:04

# esnext

SJS 支持部分 ES6 语法。

## let & const

示例代码:

```
function test(){
  let a = 5;
  if (true) {
    let b = 6;
  }
  console.log(a); // 5
  console.log(b); // 引用错误：b 未定义
}
```

## 箭头函数

示例代码：

```
const a = [1,2,3];
const double = x => x * 2; // 箭头函数
console.log(a.map(double));
var bob = {
  _name: "Bob",
  _friends: [],
  printFriends() {
    this._friends.forEach(f =>
      console.log(this._name + " knows " + f));
  }
};
console.log(bob.printFriends());
```

## 更简洁的对象字面量（enhanced object literal）

示例代码：

```
var handler = 1;
var obj = {
  handler, // 对象属性
  toString() { // 对象方法
return "string";
  },
};
```

> **[!IMPORTANT]**
>
> 不支持 super 关键字，不能在对象方法中使用 super。

## 模板字符串（template string）

示例代码：

```
const h = 'hello';
const msg = `${h} dingtalk`;
```

## 解构赋值（Destructuring）

示例代码：

```
// array 解构赋值
var [a, ,b] = [1,2,3];
a === 1;
b === 3;
// 对象解构赋值
var { op: a, lhs: { op: b }, rhs: c }
       = getASTNode();
// 对象解构赋值简写
var {op, lhs, rhs} = getASTNode();
// 函数参数解构赋值
function g({name: x}) {
  console.log(x);
}
g({name: 5});
// 解构赋值默认值
var [a = 1] = [];
a === 1;
// 函数参数：解构赋值 + 默认值
function r({x, y, w = 10, h = 10}) {
  return x + y + w + h;
}
r({x:1, y:2}) === 23;
```

## Default + Rest + Spread

示例代码：

```
// 函数参数默认值
function f(x, y=12) {
  // 如果不给y传值，或者传值为undefied，则y的值为12
  return x + y;
}
f(3) == 15;
function f(x, ...y) {
  // y 是一个数组
  return x * y.length;
}
f(3, "hello", true) == 6;
function f(x, y, z) {
  return x + y + z;
}
f(...[1,2,3]) == 6; // 数组解构
const [a, ...b] = [1,2,3]; // 数组解构赋值, b = [2, 3]
const {c, ...other} = {c: 1, d: 2, e: 3}; // 对象解构赋值, other = {d: 2, e: 3}
const d = {...other}; // 对象解构
```
