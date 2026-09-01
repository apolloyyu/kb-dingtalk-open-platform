---
title: "SJS 语法参考"
source_url: "https://open.dingtalk.com/document/development/variable-1"
namespace: "development"
slug: "variable-1"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 框架 > SJS 语法参考"
doc_id: "0xkAkOqsdP"
updated_at: "2026-09-01 09:16:09"
---

> Source: https://open.dingtalk.com/document/development/variable-1
> Path: 应用开发 / 客户端 JSAPI / 历史文档（不推荐） > 小程序 > 框架 > SJS 语法参考
> Updated: 2026-09-01 09:16:09

# SJS 语法参考

## **概述**

SJS（safe/subset javascript）是小程序一套自定义脚本语言，可以在 AXML 中使用其构建页面结构。 SJS 是 JavaScript 语言的子集，与 JavaScript 是不同的语言，其语法并不与 JavaScript 一致，请勿将其等同于 JavaScript。

### **使用方式**

在 index.sjs 文件中定义 SJS：

```
// pages/index/index.sjs
const message = 'hello dingtalk';
const getMsg = x => x;
export default {
  message,
  getMsg,
};
```

index.js示例代码：

```
// pages/index/index.js
Page({
  data: {
    msg: 'hello taobao',
  },
});
```

index.axml示例代码：

```
<!-- pages/index/index.axml -->
<import-sjs name="m1" from="./index.sjs"/>
<view>{{m1.message}}</view>
<view>{{m1.getMsg(msg)}}</view>
```

页面输出：

```
hello dingtalk
hello taobao
```

> **[!IMPORTANT]**
>
> - sjs 中只支持使用 import、export 管理模块依赖**。**
> - sjs 只能定义在 `.sjs`文件中，然后在 axml 中使用 `<import-sjs>`标签引入。
> - sjs 可以调用其他 sjs 文件中定义的函数。
> - sjs 是 JavaScript 语言的子集，请勿将其等同于 JavaScript。
> - sjs 的运行环境和其他 JavaScript 代码是隔离的，sjs 中不能调用其他 JavaScript 文件中定义的函数，也不能调用小程序提供的 API。
> - sjs 函数不能作为组件事件回调。
> - sjs 不依赖于基础库版本，可以在所有版本小程序中运行。

### **import-sjs 标签**

index.js示例代码：

```
// pages/index/index.js
Page({
  data: {
    msg: 'hello dingtalk',
  },
});
```

index.sjs示例代码：

```
// pages/index/index.sjs
function bar(prefix) {
  return prefix;
}
export default {
  foo: 'foo',
  bar: bar
};
```

namedExport.sjs示例代码：

```
// pages/index/namedExport.sjs
export const x = 3;
export const y = 4;
```

index.axml示例代码：

```
<!-- pages/index/index.axml -->
<import-sjs from="./index.sjs" name="test"></import-sjs>
<!-- 也可以直接使用单标签闭合的写法
<import-sjs from="./index.sjs" name="test" />
-->

<!-- 调用 test 模块里面的 bar 函数，且参数为 test 模块里面的 foo -->
<view> {{test.bar(test.foo)}} </view>
<!-- 调用 test 模块里面的 bar 函数，且参数为 page.js 里面的 msg -->
<view> {{test.bar(msg)}} </view>

<!-- 支持命名导出（named export） -->
<import-sjs from="./namedExport.sjs" name="{x, y: z}" />
<view>{{x}}</view>
<view>{{z}}</view>
```

页面输出：

```
foo
hello dingtalk
3
4
```

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| name | String | 是 | 当前`<import-sjs>` 标签的模块名。 |
| from | String | 是 | 引用 .sjs 文件的相对路径。 |

name 属性指定当前 `<import-sjs>` 标签的模块名。在单个 AXML 文件内，建议将 name 值设为唯一。若有重复模块名则按照先后顺序覆盖（后者覆盖前者）。不同 AXML 文件之间的 `<import-sjs>` 模块名不会相互覆盖。

name 属性可使用一个字符串表示默认模块名，也可使用 `{x}` 表示命名模块的导出。

> **[!IMPORTANT]**
>
> - 引用时务必使用“.sjs”文件后缀。
> - 若定义了一个 .sjs模块，但从未引用，则该模块不会被解析与运行。

## **变量**

### **语法规则**

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

### **变量名**

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

## **注释**

注释方法和 Javascript 一致，可以使用以下方法对 SJS 代码进行注释：

```
// page.sjs
// 方法一：这是一个单行注释

/*  方法二：这是一个多行注释中间的内容都会被注释 */
let h = 'hello';
const w = 'dingtalk';
```

## **运算符**

- **算术运算符**

  ```
  var a = 10, b = 20;
  // 加法运算
  console.log(30 === a + b);   //true
  // 减法运算
  console.log(-10 === a - b);  //true
  // 乘法运算
  console.log(200 === a * b);  //true
  // 除法运算
  console.log(0.5 === a / b);  //true
  // 取余运算
  console.log(10 === a % b);   //true
  加法 + 运算符可用作字符串拼接。
  var a = 'hello', b = 'dingtalk';
  // 字符串拼接
  console.log('hello dingtalk' === a + b);    //true
  ```
- **比较运算符**

  ```
  var a = 10, b = 20;
  // 小于
  console.log(true === (a < b));    //true 
  // 大于
  console.log(false === (a > b));   //true
  // 小于等于
  console.log(true === (a <= b));   //true
  // 大于等于
  console.log(false === (a >= b));   //true
  // 等号
  console.log(false === (a == b));   //true
  // 非等号
  console.log(true === (a != b));     //true
  // 全等号
  console.log(false === (a === b));   //true
  // 非全等号
  console.log(true === (a !== b));   //true
  ```
- **二元逻辑运算符**

  ```
  var a = 10, b = 20;
  // 逻辑与
  console.log(20 === (a && b));  //true
  // 逻辑或
  console.log(10 === (a || b));  //true
  // 逻辑否，取反运算
  console.log(false === !a);    //true
  ```
- **位运算符**

  ```
  var a = 10, b = 20;
  // 左移运算
  console.log(80 === (a << 3));   //true
  // 无符号右移运算
  console.log(2 === (a >> 2));   //true
  // 带符号右移运算
  console.log(2 === (a >>> 2));   //true
  // 与运算
  console.log(2 === (a & 3));   //true
  // 异或运算
  console.log(9 === (a ^ 3));   //true
  // 或运算
  console.log(11 === (a | 3));   //true
  ```
- **赋值运算符**

  ```
  var a = 10;
  a = 10; a *= 10;
  console.log(100 === a);   //true
  a = 10; a /= 5;
  console.log(2 === a);   //true
  a = 10; a %= 7;
  console.log(3 === a);   //true
  a = 10; a += 5;
  console.log(15 === a);   //true
  a = 10; a -= 11;
  console.log(-1 === a);   //true
  a = 10; a <<= 10;
  console.log(10240 === a);   //true
  a = 10; a >>= 2;
  console.log(2 === a);   //true
  a = 10; a >>>= 2;
  console.log(2 === a);   //true
  a = 10; a &= 3;
  console.log(2 === a);   //true
  a = 10; a ^= 3;
  console.log(9 === a);   //true
  a = 10; a |= 3;
  console.log(11 === a);   //true
  ```
- **一元运算符**

  ```
  var a = 10, b = 20;
  // 自增运算
  console.log(10 === a++);   //true
  console.log(12 === ++a);   //true
  // 自减运算
  console.log(12 === a--);   //true
  console.log(10 === --a);   //true
  // 正值运算
  console.log(10 === +a);   //true
  // 负值运算
  console.log(0-10 === -a);   //true
  // 否运算
  console.log(-11 === ~a);   //true
  // 取反运算
  console.log(false === !a);   //true
  // delete 运算
  console.log(true === delete a.fake);   //true
  // void 运算
  console.log(undefined === void a);   //true
  // typeof 运算
  console.log("number" === typeof a);   //true
  ```
- **三元运算符**

  ```
  var a = 10, b = 20;
  // 条件运算符
  console.log(20 === (a >= 10 ? a + 10 : b + 10));   //true
  ```
- **逗号运算符**

  ```
  var a = 10, b = 20;
  // 逗号运算符
  console.log(20 === (a, b));   //true
  ```
- **运算符优先级**

  SJS 运算符的优先级与 Javascript 一致。

## **语句**

- **if 语句**

  在 .sjs 文件中，可以使用以下格式的 if 语句 ：

  - if (expression) statement ： 当 expression 为 true 时，执行 statement。
  - if (expression) statement1 else statement2 : 当 expression 为 true 时，执行 statement1。 否则，执行 statement2。
  - if ... else if ... else statementN 通过该句型，可以在 statement1 ~ statementN 之间选其中一个执行。

    示例代码：

    ```
    // if ...
    if (表达式) 语句;
    if (表达式)
      语句;
    if (表达式) {
      代码块;
    }
    // if ... else
    if (表达式) 语句;
    else 语句;
    if (表达式)
      语句;
    else
      语句;
    if (表达式) {
      代码块;
    } else {
      代码块;
    }
    // if ... else if ... else ...
    if (表达式) {
      代码块;
    } else if (表达式) {
      代码块;
    } else if (表达式) {
      代码块;
    } else {
      代码块;
    }
    ```
- **switch 语句**

  示例代码：

  ```
  switch (表达式) {
    case 变量:
      语句;
    case 数字:
      语句;
      break;
    case 字符串:
      语句;
    default:
      语句;
  }
  ```

  > **[!NOTE]**
  >
  > - `default`分支可以省略不写。
  > - `case`关键词后面只能使用：`变量`，`数字`，`字符串`。

  示例代码：

  ```
  var exp = 10;
  switch ( exp ) {
  case "10":
    console.log("string 10");
    break;
  case 10:
    console.log("number 10");
    break;
  case exp:
    console.log("var exp");
    break;
  default:
    console.log("default");
  }
  ```

  输出：

  ```
  number 10
  ```
- **for 语句**

  示例代码：

  ```
  for (语句; 语句; 语句)
    语句;

  for (语句; 语句; 语句) {
    代码块;
  }
  ```

  > **[!NOTE]**
  >
  > 支持使用 `break`，`continue`关键词。

  示例代码：

  ```
  for (var i = 0; i < 3; ++i) {
    console.log(i);
    if( i >= 1) break;
  }
  ```

  输出：

  ```
  0
  1
  ```
- **while 语句**

  示例代码：

  ```
  while (表达式)
    语句;

  while (表达式){
    代码块;
  }

  do {
    代码块;
  } while (表达式)
  ```

  > **[!NOTE]**
  >
  > - 当 `表达式`为 true 时，循环执行 `语句`或`代码块`。
  > - 支持使用`break`，`continue`关键词。

## **数据类型**

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

### **判断数据类型**

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

### **数据类型**

- **string**

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
- **number**

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
- **boolean**

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
- **object**

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

  **方法**

  | 方法 | 说明 |
  | --- | --- |
  | toString | 返回字符串 `"[object Object]"`。 |
- **function**

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
- **array**

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
- **date**

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
- **regexp**

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

## **基础类库**

- **Global**

  > **[!IMPORTANT]**
  >
  > SJS 不支持 JavaScript 的大部分全局属性和方法。

  **属性**

  - Infinity
  - NaN
  - undefined
  > **[!NOTE]**
  >
  > 具体使用请参考 ES5 标准。

  **方法说明**

  | 方法 | 说明 |
  | --- | --- |
  | decodeURI | encodeURI() 函数编码过的 URI 进行解码。 |
  | decodeURIComponent | encodeURIComponent() 函数编码的 URI 进行解码。 |
  | encodeURI | 把字符串作为 URI 进行编码。 |
  | encodeURIComponent | 把字符串作为 URI 组件进行编码。 |
  | isNaN | 检查其参数是否是非数字值。 |
  | isFinite | 检查其参数是否是无穷大。 |
  | parseFloat | 解析一个字符串，并返回一个浮点数。 |
  | parseInt | 将字符串参数作为有符号的十进制整数进行解析。 |

  > **[!NOTE]**
  >
  > 具体使用请参考 ES5 标准。
- **console**

  console.log 方法可在 console 窗口输出信息，可以接受多个参数，将多个参数结果连接起来输出。
- **Date**

  **方法说明**

  | 方法 | 说明 |
  | --- | --- |
  | now | 返回自1970年1月1日00:00:00 UTC以来经过的毫秒数。 |
  | parse | 解析一个日期时间字符串，并返回 1970/1/1 午夜距离该日期时间的毫秒数。 |
  | UTC | 根据世界时返回 1970 年 1 月 1 日 到指定日期的毫秒数。 |

  > **[!NOTE]**
  >
  > 具体使用请参考 ES5 标准。
- **Number**

  **属性**

  - MAX\_VALUE
  - MIN\_VALUE
  - NEGATIVE\_INFINITY
  - POSITIVE\_INFINITY
  > **[!NOTE]**
  >
  > 具体使用请参考 ES5 标准。
- **JSON**

  **方法说明**

  | 方法 | 说明 |
  | --- | --- |
  | stringify | 将 object 对象转换为 JSON 字符串，并返回该字符串。 |
  | parse | 将 JSON 字符串转化成对象，并返回该对象。 |

  **示例代码**

  ```
  console.log(undefined === JSON.stringify());
  console.log(undefined === JSON.stringify(undefined));
  console.log("null"===JSON.stringify(null));
  console.log("222"===JSON.stringify(222));
  console.log('"222"'===JSON.stringify("222"));
  console.log("true"===JSON.stringify(true));
  console.log(undefined===JSON.stringify(function(){}));
  console.log(undefined===JSON.parse(JSON.stringify()));
  console.log(undefined===JSON.parse(JSON.stringify(undefined)));
  console.log(null===JSON.parse(JSON.stringify(null)));
  console.log(222===JSON.parse(JSON.stringify(222)));
  console.log("222"===JSON.parse(JSON.stringify("222")));
  console.log(true===JSON.parse(JSON.stringify(true)));
  console.log(undefined===JSON.parse(JSON.stringify(function(){})));
  ```
- **Math**

  **属性**

  - E
  - LN10
  - LN2
  - LOG2E
  - LOG10E
  - PI
  - SQRT1\_2
  - SQRT2
  > **[!NOTE]**
  >
  > 具体使用请参考 ES5 标准。

  **方法说明**

  | 方法 | 说明 |
  | --- | --- |
  | abs | 返回数的绝对值。 |
  | acos | 返回0和PI对于x-1和1之间弧度的数值。 |
  | asin | 返回一个数的反正弦值。 |
  | atan | 返回数字的反正切值。 |
  | atan2 | 返回从 x 轴到点 (x,y) 之间的角度。 |
  | ceil | 对一个数进行上舍入。 |
  | cos | 返回一个数字的余弦值。 |
  | exp | 可返回 e 的 x 次幂的值。 |
  | floor | 对一个数进行下舍入。 |
  | log | 返回一个数的自然对数。 |
  | max | 返回两个指定的数中带有较大的值的那个数。 |
  | min | 返回指定的数字中带有最低值的数字。 |
  | pow | 返回 x 的 y 次幂的值。 |
  | random | 返回介于 0 ~ 1 之间的一个随机数。 |
  | round | 把一个数字舍入为最接近的整数。 |
  | sin | 返回一个数字的正弦。 |
  | sqrt | 返回一个数的平方根。 |
  | tan | 返回一个表示某个角的正切的数字。 |

  > **[!NOTE]**
  >
  > 具体使用请参考 ES5 标准。

## **esnext**

- **let & const**

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
- **箭头函数**

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
- **更简洁的对象字面量（enhanced object literal）**

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
- **模板字符串（template string）**

  示例代码：

  ```
  const h = 'hello';
  const msg = `${h} dingtalk`;
  ```
- **解构赋值（Destructuring）**

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
- **Default + Rest + Spread**

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
