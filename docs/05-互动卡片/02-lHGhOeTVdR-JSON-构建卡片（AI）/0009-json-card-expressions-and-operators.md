---
title: "表达式与算子"
source_url: "https://open.dingtalk.com/document/development/json-card-expressions-and-operators"
namespace: "development"
slug: "json-card-expressions-and-operators"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "构建卡片结构 > 函数 > 表达式与算子"
doc_id: "ObcClOGN8n"
updated_at: "2026-09-30 09:14:07"
---

> Source: https://open.dingtalk.com/document/development/json-card-expressions-and-operators
> Path: 互动卡片 / JSON 构建卡片（AI） / 构建卡片结构 > 函数 > 表达式与算子
> Updated: 2026-09-30 09:14:07

# 表达式与算子

## add

钉钉扩展函数。两数相加。

返回 `number`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `a` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |
| `b` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |

### 最小示例

```
{
  "call": "add",
  "args": {
    "a": 0,
    "b": 0
  }
}
```

## sub

钉钉扩展函数。两数相减。

返回 `number`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `a` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |
| `b` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |

### 最小示例

```
{
  "call": "sub",
  "args": {
    "a": 0,
    "b": 0
  }
}
```

## mul

钉钉扩展函数。两数相乘。

返回 `number`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `a` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |
| `b` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |

### 最小示例

```
{
  "call": "mul",
  "args": {
    "a": 0,
    "b": 0
  }
}
```

## div

钉钉扩展函数。一个数除以另一个数。

返回 `number`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `a` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |
| `b` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |

### 最小示例

```
{
  "call": "div",
  "args": {
    "a": 0,
    "b": 0
  }
}
```

## mod

钉钉扩展函数。计算两数相除的余数。

返回 `number`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `a` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |
| `b` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |

### 最小示例

```
{
  "call": "mod",
  "args": {
    "a": 0,
    "b": 0
  }
}
```

## eq

判断两个值是否相等。支持与 `null` 比较；用 `eq(arrayFind(...), null)` 判断没有匹配项。

返回 `boolean`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `a` | [DynamicValue](0010-json-card-common-types.md#8d0da86db31ui) | 是 | 通用值：字符串、数字、布尔值、数组、`null`、普通对象、数据绑定或值函数的结果。   - 包含 `call` 的对象按函数调用解析，只有 `path` 一个键的对象按绑定解析。 |
| `b` | [DynamicValue](0010-json-card-common-types.md#8d0da86db31ui) | 是 | 通用值：字符串、数字、布尔值、数组、`null`、普通对象、数据绑定或值函数的结果。   - 包含 `call` 的对象按函数调用解析，只有 `path` 一个键的对象按绑定解析。 |

### 最小示例

```
{
  "call": "eq",
  "args": {
    "a": "REPLACE_TEXT",
    "b": "REPLACE_TEXT"
  }
}
```

## ne

判断两个值是否不相等。支持与 `null` 比较；用 `ne(arrayFind(...), null)` 判断存在匹配项。

返回 `boolean`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `a` | [DynamicValue](0010-json-card-common-types.md#8d0da86db31ui) | 是 | 通用值：字符串、数字、布尔值、数组、`null`、普通对象、数据绑定或值函数的结果。   - 包含 `call` 的对象按函数调用解析，只有 `path` 一个键的对象按绑定解析。 |
| `b` | [DynamicValue](0010-json-card-common-types.md#8d0da86db31ui) | 是 | 通用值：字符串、数字、布尔值、数组、`null`、普通对象、数据绑定或值函数的结果。   - 包含 `call` 的对象按函数调用解析，只有 `path` 一个键的对象按绑定解析。 |

### 最小示例

```
{
  "call": "ne",
  "args": {
    "a": "REPLACE_TEXT",
    "b": "REPLACE_TEXT"
  }
}
```

## lt

钉钉扩展函数。判断数 A 是否小于数 B。

返回 `boolean`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `a` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |
| `b` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |

### 最小示例

```
{
  "call": "lt",
  "args": {
    "a": 0,
    "b": 0
  }
}
```

## lte

钉钉扩展函数。判断数 A 是否小于等于数 B。

返回 `boolean`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `a` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |
| `b` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |

### 最小示例

```
{
  "call": "lte",
  "args": {
    "a": 0,
    "b": 0
  }
}
```

## gt

钉钉扩展函数。判断数 A 是否大于数 B。

返回 `boolean`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `a` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |
| `b` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |

### 最小示例

```
{
  "call": "gt",
  "args": {
    "a": 0,
    "b": 0
  }
}
```

## gte

钉钉扩展函数。判断数 A 是否大于等于数 B。

返回 `boolean`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `a` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |
| `b` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |

### 最小示例

```
{
  "call": "gte",
  "args": {
    "a": 0,
    "b": 0
  }
}
```

## cond

钉钉扩展函数。条件运算符（三元运算符）。

返回 `any`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `if` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 是 | 布尔字面量、数据路径或返回布尔值的函数调用。 |
| `then` | [DynamicValue](0010-json-card-common-types.md#8d0da86db31ui) | 是 | 通用值：字符串、数字、布尔值、数组、`null`、普通对象、数据绑定或值函数的结果。   - 包含 `call` 的对象按函数调用解析，只有 `path` 一个键的对象按绑定解析。 |
| `else` | [DynamicValue](0010-json-card-common-types.md#8d0da86db31ui) | 是 | 通用值：字符串、数字、布尔值、数组、`null`、普通对象、数据绑定或值函数的结果。   - 包含 `call` 的对象按函数调用解析，只有 `path` 一个键的对象按绑定解析。 |

### 最小示例

```
{
  "call": "cond",
  "args": {
    "else": "REPLACE_TEXT",
    "if": false,
    "then": "REPLACE_TEXT"
  }
}
```

## toDouble

钉钉扩展函数。把数值转换为浮点数。

返回 `number`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `value` | [DynamicValue](0010-json-card-common-types.md#8d0da86db31ui) | 是 | 通用值：字符串、数字、布尔值、数组、`null`、普通对象、数据绑定或值函数的结果。   - 包含 `call` 的对象按函数调用解析，只有 `path` 一个键的对象按绑定解析。 |

### 最小示例

```
{
  "call": "toDouble",
  "args": {
    "value": "REPLACE_TEXT"
  }
}
```

## toLong

钉钉扩展函数。把数值转换为整数。

返回 `number`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `value` | [DynamicValue](0010-json-card-common-types.md#8d0da86db31ui) | 是 | 通用值：字符串、数字、布尔值、数组、`null`、普通对象、数据绑定或值函数的结果。   - 包含 `call` 的对象按函数调用解析，只有 `path` 一个键的对象按绑定解析。 |

### 最小示例

```
{
  "call": "toLong",
  "args": {
    "value": "REPLACE_TEXT"
  }
}
```

## objectGet

按 `key` 读取对象属性。`value` 可以是普通对象字面量、数据绑定或值函数的结果。属性不存在时返回 `null`。

返回 `any`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `value` | [DynamicValue](0010-json-card-common-types.md#8d0da86db31ui) | 是 | 通用值：字符串、数字、布尔值、数组、`null`、普通对象、数据绑定或值函数的结果。   - 包含 `call` 的对象按函数调用解析，只有 `path` 一个键的对象按绑定解析。 |
| `key` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | 字符串字面量、指向数据模型中字符串的路径、或返回字符串的函数调用。 |

### 最小示例

```
{
  "call": "objectGet",
  "args": {
    "key": "REPLACE_TEXT",
    "value": "REPLACE_TEXT"
  }
}
```

## arrayGet

钉钉扩展函数。读取数组中的某一项。

返回 `any`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `value` | [DynamicValue](0010-json-card-common-types.md#8d0da86db31ui) | 是 | 通用值：字符串、数字、布尔值、数组、`null`、普通对象、数据绑定或值函数的结果。   - 包含 `call` 的对象按函数调用解析，只有 `path` 一个键的对象按绑定解析。 |
| `index` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |

### 最小示例

```
{
  "call": "arrayGet",
  "args": {
    "index": 0,
    "value": "REPLACE_TEXT"
  }
}
```

## arrayFind

钉钉扩展函数。在数组中查找匹配项。

返回 `any`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `value` | [DynamicValue](0010-json-card-common-types.md#8d0da86db31ui) | 是 | 通用值：字符串、数字、布尔值、数组、`null`、普通对象、数据绑定或值函数的结果。   - 包含 `call` 的对象按函数调用解析，只有 `path` 一个键的对象按绑定解析。 |
| `target` | [DynamicValue](0010-json-card-common-types.md#8d0da86db31ui) | 是 | 通用值：字符串、数字、布尔值、数组、`null`、普通对象、数据绑定或值函数的结果。   - 包含 `call` 的对象按函数调用解析，只有 `path` 一个键的对象按绑定解析。 |

### 最小示例

```
{
  "call": "arrayFind",
  "args": {
    "target": "REPLACE_TEXT",
    "value": "REPLACE_TEXT"
  }
}
```

## getLength

钉钉扩展函数。返回数组长度。

返回 `number`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `value` | [DynamicValue](0010-json-card-common-types.md#8d0da86db31ui) | 是 | 通用值：字符串、数字、布尔值、数组、`null`、普通对象、数据绑定或值函数的结果。   - 包含 `call` 的对象按函数调用解析，只有 `path` 一个键的对象按绑定解析。 |

### 最小示例

```
{
  "call": "getLength",
  "args": {
    "value": "REPLACE_TEXT"
  }
}
```
