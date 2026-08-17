---
title: "数据类型"
source_url: "https://open.dingtalk.com/document/development/data-type-1"
namespace: "development"
slug: "data-type-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 框架 > SJS语法参考 > 数据类型"
doc_id: "fmBMLuN9DD"
updated_at: "2025-09-17 20:58:03"
---

> Source: https://open.dingtalk.com/document/development/data-type-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 框架 > SJS语法参考 > 数据类型
> Updated: 2025-09-17 20:58:03

# 数据类型

SJS 目前支持如下数据类型：

| **数据类型** | **说明** |
| --- | --- |
| string | 字符串 |
| boolean | 布尔值 |
| number | 数值 |
| object | 对象 |
| function | 函数 |
| array | 数组 |
| date | 日期 |
| regexp | 正则表达式 |

## 判断数据类型

SJS 提供了 constructor 与 typeof 两种方式判断数据类型。

**constructor**

```
const number = 10;
console.log(number.constructor); // "Number"
const string = "str";
console.log(string.constructor); // "String"
const boolean = true;
console.log(boolean.constructor); // "Boolean"
const object = {};
console.log(object.constructor); // "Object"
const func = function(){};
console.log(func.constructor); // "Function"
const array = [];
console.log(array.constructor); // "Array"
const date = getDate();
console.log(date.constructor); // "Date"
const regexp = getRegExp();
console.log(regexp.constructor); // "RegExp"
```

**typeof**

```
const num = 100;
const bool = false;
const obj = {};
const func = function(){};
const array = [];
const date = getDate();
const regexp = getRegExp();
console.log(typeof num); // 'number'
console.log(typeof bool); // 'boolean'
console.log(typeof obj); // 'object'
console.log(typeof func); // 'function'
console.log(typeof array); // 'object'
console.log(typeof date); // 'object'
console.log(typeof regexp); // 'object'
console.log(typeof undefined); // 'undefined'
console.log(typeof null); // 'object'
```

## string

**语法**

```
'hello dingtalk';
"hello taobao";
```

**ES6 语法**

```
// 字符串模板
const a = 'hello';
const str = `${a} dingtalk`;
```

**属性**

- constructor：返回值`"String"`
- length

> **[!NOTE]**
>
> 除 constructor 外属性的具体含义请参考 ES5 标准。

**方法**

| 方法 | 说明 |
| --- | --- |
| toString | 将对象转换为一个字符串。 |
| valueOf | 用于返回指定对象的原始值。 |
| charAt | 返回指定位置的字符。 |
| charCodeAt | 返回指定位置的字符的 Unicode 编码。 |
| concat | 用于连接两个或多个数组。 |
| indexOf | 返回某个指定的字符串值在字符串中首次出现的位置。 |
| lastIndexOf | 返回一个指定的字符串值最后出现的位置。 |
| localeCompare | 使用本地排序规则对两个字符串进行比较。 |
| match | 在字符串内检索指定的值或找到正则表达式的匹配。 |
| replace | 替换字符或替换一个与正则表达式匹配的子串。 |
| search | 检索字符串指定的或与正则表达式相匹配的子字符串。 |
| slice | 从已有的数组中返回选定的元素。 |
| split | 把一个字符串分割成字符串数组。 |
| substring | 返回字符串的子字符串。 |
| toLowerCase | 把字符串转换为小写。 |
| toLocaleLowerCase | 把字符串转换为小写。 |
| toUpperCase | 把字符串转换为大写。 |
| toLocaleUpperCase | 把字符串转换为大写。 |
| trim | 去掉字符串两端的多余的空格。 |

> **[!NOTE]**
>
> 具体使用请参考 ES5 标准。

## number

**语法**

```
const num = 10;
const PI = 3.141592653589793;
```

**属性**

- constructor：返回值`"Number"`

**方法**

| 方法 | 说明 |
| --- | --- |
| toString | 将对象转换为一个字符串。 |
| toLocaleString | 把数组转换为本地字符串。 |
| valueOf | 用于返回指定对象的原始值。 |
| toFixed | 四舍五入为指定小数位数的数字。 |
| toExponential | 把对象的值转换成指数计数法。 |
| toPrecision | 在对象的值超出指定位数时将其转换为指数计数法。 |

> **[!NOTE]**
>
> 具体使用请参考 ES5 标准。

## boolean

布尔值只有两个特定的值：true 和 false。

**语法**

```
const a = true;
```

**属性**

- constructor：返回值`"Boolean"`

**方法**

| 方法 | 说明 |
| --- | --- |
| toString | 将对象转换为一个字符串。 |
| valueOf | 用于返回指定对象的原始值。 |

> **[!NOTE]**
>
> 具体使用请参考 ES5 标准。

## object

**语法**

```
var o = {}; // 生成一个新的空对象
// 生成一个新的非空对象
o = {
  'str': "str",  // 对象的 key 可以是字符串
  constVar: 2,  // 对象的 key 也可以是符合变量定义规则的标识符
  val: {}, // 对象的 value 可以是任何类型
};
// 对象属性的读操作
console.log(1 === o['string']);
console.log(2 === o.constVar);
// 对象属性的写操作
o['string']++;
o['string'] += 10;
o.constVar++;
o.constVar += 10;
// 对象属性的读操作
console.log(12 === o['string']);
console.log(13 === o.constVar);
```

**ES6 语法**

```
// 支持
let a = 2;
o = {
  a, // 对象属性
  b() {}, // 对象方法
};
const { a, b, c: d, e = 'default'} = {a: 1, b: 2, c: 3}; // 对象解构赋值 & default
const {a, ...other} = {a: 1, b: 2, c: 3}; // 对象解构赋值
const f = {...others}; // 对象解构
```

**属性**

- constructor：返回值`"Object"`

  示例代码：

  ```
  console.log("Object" === {a:2,b:"5"}.constructor);
  ```

**方****法**

| 方法 | 说明 |
| --- | --- |
| toString | 返回字符串 `"[object Object]"`。 |

## function

**语法**

```
// 方法 1：函数声明
function a (x) {
  return x;
}
// 方法 2：函数表达式
var b = function (x) {
  return x;
};
// 方法 3：箭头函数
const double = x => x * 2;
function f(x = 2){} // 函数参数默认
function g({name: n = 'xiaoming', ...other} = {}) {} // 函数参数解构赋值
function h([a, b] = []) {} // 函数参数解构赋值
// 匿名函数、闭包
var c = function (x) {
  return function () { return x;}
};
var d = c(25);
console.log(25 === d());
function 中可以使用 arguments 关键字。
var a = function(){
    console.log(2 === arguments.length);
    console.log(1 === arguments[0]);
    console.log(2 === arguments[1]);
};
a(1,2);
```

输出：

```
true
true
true
```

**属性**

- constructor：返回值`"Function"`
- length：返回函数的形参个数

**方法**

| 方法 | 说明 |
| --- | --- |
| toString | 返回一个表示当前函数源代码的字符串。 |

示例代码：

```
var f = function (a,b) { }
console.log("Function" === f.constructor);
console.log("[function Function]" === f.toString());
console.log(2 === f.length);
```

输出：

```
true
true
true
```

## array

**语法**

```
var a = [];      // 空数组
a = [5,"5",{},function(){}];  // 非空数组，数组元素可以是任何类型
const [b, , c, d = 5] = [1,2,3]; // 数组解构赋值 & 默认值
const [e, ...other] = [1,2,3]; // 数组解构赋值
const f = [...other]; // 数组解构
```

**属性**

- constructor：返回值`"Array"`
- length

> **[!NOTE]**
>
> 除constructor外属性的具体含义请参考 ES5 标准。

**方法**

| 方法 | 说明 |
| --- | --- |
| toString | 将数组转换为字符串并返回结果。 |
| concat | 连接两个或多个数组。 |
| join | 把数组中的所有元素放入一个字符串。 |
| pop | 删除并返回数组的最后一个元素。 |
| push | 向数组的末尾添加一个或多个元素，并返回新的长度。 |
| reverse | 颠倒数组中元素的顺序。 |
| shift | 数组的第一个元素从其中删除并返回第一个元素的值。 |
| slice | 从已有的数组中返回选定的元素。 |
| sort | 对数组的元素进行排序。 |
| splice | 从数组中添加/删除项目，然后返回被删除的项目。 |
| unshift | 向数组的开头添加一个或更多元素，并返回新的长度。 |
| indexOf | 返回某个指定的字符串值在字符串中首次出现的位置。 |
| lastIndexOf | 返回一个指定的字符串值最后出现的位置。 |
| every | 检测数组所有元素是否都符合指定条件。 |
| some | 检测数组中的元素是否满足指定条件。 |
| forEach | 调用数组的每个元素，并将元素传递给回调函数。 |
| map | 返回一个新数组，数组中的元素为原始数组元素调用函数处理后的值。 |
| filter | 创建一个新的数组，新数组中的元素是通过检查指定数组中符合条件的所有元素。 |
| reduce | 接收一个函数作为累加器，数组中的每个值（从左到右）开始缩减，最终计算为一个值。 |
| reduceRight | 接收一个函数作为累加器，数组中的每个值（从右到左）开始累加，最终计算为一个值。 |

> **[!NOTE]**
>
> 具体使用请参考 ES5 标准。

## **date**

**语法**

生成 date 对象需要使用 `getDate` 函数, 返回一个当前时间的对象。

```
getDate()
getDate(milliseconds)
getDate(datestring)
getDate(year, month[, date[, hours[, minutes[, seconds[, milliseconds]]]]])
```

**参数**

- milliseconds：从 1970年1月1日00:00:00 UTC 开始计算的毫秒数
- datestring：日期字符串，其格式为："month day, year hours:minutes:seconds"

**属性**

- constructor：返回值`"Date"`

**方法**

| 方法 | 说明 |
| --- | --- |
| toString | 返回字符串 `"[object Object]"`。 |
| toDateString | 把 Date 对象的日期部分转换为字符串，并返回结果。 |
| toTimeString | 把 Date 对象的时间部分转换为字符串，并返回结果。 |
| toLocaleString | 把数组转换为本地字符串。 |
| toLocaleDateString | 把 Date 对象的日期部分转换为字符串，并返回结果。 |
| toLocaleTimeString | 把 Date 对象的时间部分转换为字符串，并返回结果。 |
| valueOf | 用于返回指定对象的原始值。 |
| getTime | 返回距 1970 年 1 月 1 日之间的毫秒数。 |
| getFullYear | 返回一个表示年份的 4 位数字。 |
| getUTCFullYear | 返回根据世界时 (UTC) 表示的年份的四位数字。 |
| getMonth | 可返回表示月份的数字 |
| getUTCMonth | 返回一个表示月份的数字（按照世界时 UTC）。 |
| getDate | 返回月份的某一天。 |
| getUTCDate | 根据世界时返回一个月 (UTC) 中的某一天。 |
| getDay | 返回表示星期的某一天的数字。 |
| getUTCDay | 根据世界时返回表示星期的一天的一个数字。 |
| getHours | 返回时间的小时字段。 |
| getUTCHours | 根据世界时 (UTC) 返回时间的小时。 |
| getMinutes | 返回时间的分钟字段。 |
| getUTCMinutes | 根据世界时 (UTC) 返回时间的分钟字段（0~59）。 |
| getSeconds | 返回时间的秒。返回值是 0 ~ 59 之间的一个整数。 |
| getUTCSeconds | 根据世界时返回时间的秒。 |
| getMilliseconds | 返回时间的毫秒。 |
| getUTCMilliseconds | 根据世界时 (UTC) 返回时间的毫秒。 |
| getTimezoneOffset | 返回格林威治和本地时间的时差，以分钟为单位。 |
| setTime | 以毫秒设置 Date 对象。 |
| setMilliseconds | 设置指定时间的毫秒字段。 |
| setUTCMilliseconds | 根据世界时 (UTC) 设置指定时间的毫秒。 |
| setSeconds | 设置日期对象的秒字段。 |
| setUTCSeconds | 根据世界时 (UTC) 设置指定时间的秒。 |
| setMinutes | 设置指定时间的分钟字段。 |
| setUTCMinutes | 据世界时 (UTC) 来设置指定时间的分钟。 |
| setHours | 设置指定的时间的小时字段。 |
| setUTCHours | 根据世界时 (UTC) 设置小时（0 - 23）。 |
| setDate | 设置一个月的某一天。 |
| setUTCDate | 根据世界时 (UTC) 设置一个月中的某一天。 |
| setMonth | 设置月份中的某一天。 |
| setUTCMonth | 根据世界时 (UTC) 来设置月份。 |
| setFullYear | 用于设置年份。 |
| setUTCFullYear | 根据世界时 (UTC) 设置年份。 |
| toUTCString | 根据世界时把 Date 对象转换为字符串，并返回结果。 |
| toISOString | 使用ISO标准将 Date 对象转换为字符串。 |
| toJSON | 将 Date 对象转换为字符串，并格式化为 JSON 格式。 |

> **[!NOTE]**
>
> 具体使用请参考 ES5 标准。

示例代码：

```
let date = getDate(); //返回当前时间对象
date = getDate(1500000000000);
// Fri Jul 14 2017 10:40:00 GMT+0800 (中国标准时间)
date = getDate('6 29, 2016');
// Fri June 29 2016 00:00:00 GMT+0800 (中国标准时间)
date = getDate(2017, 6, 14, 10, 40, 0, 0);
// Fri Jul 14 2017 10:40:00 GMT+0800 (中国标准时间)
```

## regexp

**语法**

生成 regexp 对象需要使用 getRegExp 函数。

```
getRegExp(pattern[, flags])
```

**参数**

- pattern: 正则的内容
- flags：修饰符，只能包括以下字符: `g` 、`i` 、`m`

**属性**

- constructor：返回字符串 `"RegExp"`
- global
- ignoreCase
- lastIndex
- multiline
- source

> **[!NOTE]**
>
> 除 constructor 外属性的具体含义请参考 ES5 标准。

**方法**

| 方法 | 说明 |
| --- | --- |
| exec | 检索字符串中的正则表达式的匹配。 |
| test | 检测一个字符串是否匹配某个模式。 |
| toString | 返回正则表达式的字符串值。 |

> **[!NOTE]**
>
> 具体使用请参考 ES5 标准。

示例代码：

```
var reg = getRegExp("name", "img");
console.log("name" === reg.source);
console.log(true === reg.global);
console.log(true === reg.ignoreCase);
console.log(true === reg.multiline);
```
