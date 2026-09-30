---
title: "核心函数"
source_url: "https://open.dingtalk.com/document/development/json-card-core-functions"
namespace: "development"
slug: "json-card-core-functions"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "构建卡片结构 > 函数 > 核心函数"
doc_id: "1IfOocv2Ai"
updated_at: "2026-09-30 09:14:13"
---

> Source: https://open.dingtalk.com/document/development/json-card-core-functions
> Path: 互动卡片 / JSON 构建卡片（AI） / 构建卡片结构 > 函数 > 核心函数
> Updated: 2026-09-30 09:14:13

# 核心函数

## required

校验值不为 `null`、`undefined` 或空。

返回 `boolean`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段。

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `value` | any | 是 | 要校验的值。 |

### 最小示例

```
{
  "call": "required",
  "args": {
    "value": "REPLACE_TEXT"
  }
}
```

## regex

校验值是否匹配正则表达式字符串。

返回 `boolean`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段。

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `value` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | 字符串字面量、数据路径或返回字符串的函数调用。 |
| `pattern` | string | 是 |  |

### 最小示例

```
{
  "call": "regex",
  "args": {
    "value": "REPLACE_TEXT",
    "pattern": "REPLACE_TEXT"
  }
}
```

## length

校验字符串长度约束。

返回 `boolean`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段。

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `value` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | 字符串字面量、数据路径或返回字符串的函数调用。 |
| `min` | integer | 否 |  |
| `max` | integer | 否 |  |

### 最小示例

```
{
  "call": "length",
  "args": {
    "value": "REPLACE_TEXT"
  }
}
```

## numeric

校验数值范围约束。

返回 `boolean`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段。

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `value` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、数据绑定或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |
| `min` | number | 否 |  |
| `max` | number | 否 |  |

### 最小示例

```
{
  "call": "numeric",
  "args": {
    "value": 0
  }
}
```

## email

校验值是否为有效的电子邮箱地址。

返回 `boolean`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段。

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `value` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | 字符串字面量、指向数据模型中字符串的路径、或返回字符串的函数调用。 |

### 最小示例

```
{
  "call": "email",
  "args": {
    "value": "REPLACE_TEXT"
  }
}
```

## formatString

用 `${/path}` 插入数据路径的值。占位符内不支持 `now()`、`formatDate(...)` 这类函数调用。`args.value` 可以使用 JSON 形式的数据绑定或值函数；它先求值为字符串，再进行数据路径插值。

返回 `string`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段。

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `value` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | 字符串字面量、指向数据模型中字符串的路径、或返回字符串的函数调用。 |

### 最小示例

```
{
  "call": "formatString",
  "args": {
    "value": "REPLACE_TEXT"
  }
}
```

## formatNumber

按分组和小数精度格式化数字。

返回 `string`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `value` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |
| `decimals` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 否 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |
| `grouping` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 布尔字面量、数据路径或返回布尔值的函数调用。 |

### 最小示例

```
{
  "call": "formatNumber",
  "args": {
    "value": 0
  }
}
```

## formatCurrency

把数字格式化为货币字符串。

返回 `string`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `value` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |
| `currency` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | ISO 4217 货币代码（例如 USD、EUR、CNY）。 |
| `decimals` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 否 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |
| `grouping` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 布尔字面量、数据路径或返回布尔值的函数调用。 |

### 最小示例

```
{
  "call": "formatCurrency",
  "args": {
    "currency": "REPLACE_TEXT",
    "value": 0
  }
}
```

## formatDate

按 Unicode TR35 日期格式把时间戳格式化为字符串。

返回 `string`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `value` | [DynamicValue](0010-json-card-common-types.md#8d0da86db31ui) | 是 | 通用值：字符串、数字、布尔值、数组、`null`、普通对象、数据绑定或值函数的结果。   - 包含 `call` 的对象按函数调用解析，只有 `path` 一个键的对象按绑定解析。 |
| `format` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | Unicode TR35 格式（例如 `yyyy-MM-dd`、`HH:mm`）。 |

### 最小示例

```
{
  "call": "formatDate",
  "args": {
    "format": "REPLACE_TEXT",
    "value": "REPLACE_TEXT"
  }
}
```

## pluralize

根据数量的 CLDR 复数类别返回本地化字符串。

返回 `string`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `value` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | JSON 数字字面量、指向数值的数据绑定、或返回数值的函数调用。   - 运行时结果必须为 JSON 数字。 - 不接受字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串。 |
| `other` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | 字符串字面量、指向数据模型中字符串的路径、或返回字符串的函数调用。 |
| `zero` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 字符串字面量、指向数据模型中字符串的路径、或返回字符串的函数调用。 |
| `one` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 字符串字面量、指向数据模型中字符串的路径、或返回字符串的函数调用。 |
| `two` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 字符串字面量、指向数据模型中字符串的路径、或返回字符串的函数调用。 |
| `few` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 字符串字面量、指向数据模型中字符串的路径、或返回字符串的函数调用。 |
| `many` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 字符串字面量、指向数据模型中字符串的路径、或返回字符串的函数调用。 |

### 最小示例

```
{
  "call": "pluralize",
  "args": {
    "value": 0,
    "other": "REPLACE_TEXT"
  }
}
```

## openUrl

在浏览器或对应的处理程序中打开指定 URL。

返回 `void`只能用于 `action.functionCall`，不能作为值表达式

- 选择客户端支持的 URL；非 HTTPS 的兼容性由客户端决定，协议本身不会拒绝。

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `url` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | 字符串字面量、指向数据模型中字符串的路径、或返回字符串的函数调用。 |

### 最小示例

```
{
  "call": "openUrl",
  "args": {
    "url": "https://example.com/REPLACE_WITH_RESOURCE"
  }
}
```

## and

对一组布尔值做逻辑与。

返回 `boolean`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `values` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv)[] | 是 |  |

### 最小示例

```
{
  "call": "and",
  "args": {
    "values": [
      false
    ]
  }
}
```

## or

对一组布尔值做逻辑或。

返回 `boolean`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `values` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv)[] | 是 |  |

### 最小示例

```
{
  "call": "or",
  "args": {
    "values": [
      false
    ]
  }
}
```

## not

对布尔值做逻辑非。

返回 `boolean`用于值表达式：写在接受函数调用的动态字段中，返回类型决定它能用在哪种字段

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `value` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 是 | 布尔字面量、数据路径或返回布尔值的函数调用。 |

### 最小示例

```
{
  "call": "not",
  "args": {
    "value": false
  }
}
```
