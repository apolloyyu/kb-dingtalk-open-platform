---
title: "基础类库"
source_url: "https://open.dingtalk.com/document/development/basic-class-library-1"
namespace: "development"
slug: "basic-class-library-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 框架 > SJS语法参考 > 基础类库"
doc_id: "aj3abTXg7N"
updated_at: "2025-09-17 20:58:03"
---

> Source: https://open.dingtalk.com/document/development/basic-class-library-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 框架 > SJS语法参考 > 基础类库
> Updated: 2025-09-17 20:58:03

# 基础类库

## Global

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

## console

console.log 方法可在 console 窗口输出信息，可以接受多个参数，将多个参数结果连接起来输出。

## Date

**方法说明**

| 方法 | 说明 |
| --- | --- |
| now | 返回自1970年1月1日00:00:00 UTC以来经过的毫秒数。 |
| parse | 解析一个日期时间字符串，并返回 1970/1/1 午夜距离该日期时间的毫秒数。 |
| UTC | 根据世界时返回 1970 年 1 月 1 日 到指定日期的毫秒数。 |

> **[!NOTE]**
>
> 具体使用请参考 ES5 标准。

## Number

**属性**

- MAX\_VALUE
- MIN\_VALUE
- NEGATIVE\_INFINITY
- POSITIVE\_INFINITY

> **[!NOTE]**
>
> 具体使用请参考 ES5 标准。

## JSON

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

## Math

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
