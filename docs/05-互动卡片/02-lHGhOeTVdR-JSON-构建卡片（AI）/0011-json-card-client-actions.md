---
title: "客户端动作"
source_url: "https://open.dingtalk.com/document/development/json-card-client-actions"
namespace: "development"
slug: "json-card-client-actions"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "构建卡片结构 > 客户端动作"
doc_id: "Pyvd3rvKl8"
updated_at: "2026-09-30 09:14:09"
---

> Source: https://open.dingtalk.com/document/development/json-card-client-actions
> Path: 互动卡片 / JSON 构建卡片（AI） / 构建卡片结构 > 客户端动作
> Updated: 2026-09-30 09:14:09

# 客户端动作

## catalogId

客户端动作写在 `action.functionCall` 中，每次调用都必须显式写客户端 catalogId：

```
{
  "call": "copyText",
  "catalogId": "urn:dingtalk:a2ui:host:v1",
  "args": { "text": "要复制的内容" }
}
```

> **[!NOTE]**
>
> - `createSurface` 或组件上的 `catalogId` 不能代替它。
> - 漏写或写成公共 catalogId，结构校验会直接报错。
> - 客户端也只按这个值识别客户端动作。
> - 校验通过后，客户端授权与客户端支持仍需真机确认。

## copyText

复制文本。返回 `void`只能用于 `action.functionCall`，并声明客户端 `catalogId`

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `text` | string | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl) | 是 |  |

### 最小示例

```
{
  "call": "copyText",
  "args": {
    "text": "REPLACE_TEXT"
  },
  "catalogId": "urn:dingtalk:a2ui:host:v1"
}
```

### 返回结果

```
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "status": {
          "const": "success"
        },
        "data": {
          "additionalProperties": false,
          "properties": {},

          "required": [ ],

          "type": "object"
        }
      },
      "required": [
        "status",
        "data"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "status": {
          "const": "failed"
        }
      },
      "required": [
        "status"
      ],
      "additionalProperties": false
    }
  ]
}
```

## openChat

打开一个会话/聊天窗口

返回 `void`只能用于 `action.functionCall`，并声明客户端 `catalogId`

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `openConversationId` | string | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl) | 是 |  |

### 最小示例

```
{
  "call": "openChat",
  "args": {
    "openConversationId": "REPLACE_TEXT"
  },
  "catalogId": "urn:dingtalk:a2ui:host:v1"
}
```

### 返回结果

```
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "status": {
          "const": "success"
        },
        "data": {
          "additionalProperties": false,
          "properties": {},

          "required": [ ],

          "type": "object"
        }
      },
      "required": [
        "status",
        "data"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "status": {
          "const": "failed"
        }
      },
      "required": [
        "status"
      ],
      "additionalProperties": false
    }
  ]
}
```

## previewImages

预览 1–100 张图片。提供 `current` 时，它必须对应预先给定的 `urls` 数组中的某一项。

返回 `void`只能用于 `action.functionCall`，并声明客户端 `catalogId`

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `urls` | string | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl)[] | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl) | 是 |  |
| `current` | string | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl) | 否 |  |

### 最小示例

```
{
  "call": "previewImages",
  "args": {
    "urls": [
      "REPLACE_TEXT"
    ]
  },
  "catalogId": "urn:dingtalk:a2ui:host:v1"
}
```

### 返回结果

```
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "status": {
          "const": "success"
        },
        "data": {
          "additionalProperties": false,
          "properties": {},

          "required": [ ],

          "type": "object"
        }
      },
      "required": [
        "status",
        "data"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "status": {
          "const": "failed"
        }
      },
      "required": [
        "status"
      ],
      "additionalProperties": false
    }
  ]
}
```

## previewVideo

Previews a video.

返回 `void`只能用于 `action.functionCall`，并声明客户端 `catalogId`

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `url` | string | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl) | 是 |  |
| `posterUrl` | string | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl) | 否 |  |

### 最小示例

```
{
  "call": "previewVideo",
  "args": {
    "url": "https://example.com/REPLACE_WITH_RESOURCE"
  },
  "catalogId": "urn:dingtalk:a2ui:host:v1"
}
```

### 返回结果

```
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "status": {
          "const": "success"
        },
        "data": {
          "additionalProperties": false,
          "properties": {},

          "required": [ ],

          "type": "object"
        }
      },
      "required": [
        "status",
        "data"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "status": {
          "const": "failed"
        }
      },
      "required": [
        "status"
      ],
      "additionalProperties": false
    }
  ]
}
```

## promptText

打开单行输入面板。

- 预填文字用 `args.initialValue`。
- `text` 是确认后返回的结果字段，不能作为入参。
- 允许静态绑定和预先求值的字符串函数。
- 不支持客户端表达式和 `maxLength`。
- 取消时不回写。

返回 `object`只能用于 `action.functionCall`，并声明客户端 `catalogId`

- 入参是 `initialValue`，`text` 是输出字段，不是入参。

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `initialValue` | string | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl) | 否 | 输入面板打开时预填的文字。可以是字符串、数据绑定，或预先求值为字符串的值函数。  **[!NOTE]**  省略时输入框初始为空。 |
| `message` | string | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl) | 否 | 桌面端输入面板显示的提示语。它不会插入到输入值中，移动端目前不显示。 |
| `title` | string | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl) | 否 | 输入面板的标题。 |

### 最小示例

```
{
  "call": "promptText",
  "args": {},
  "catalogId": "urn:dingtalk:a2ui:host:v1"
}
```

### 返回结果

```
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "status": {
          "const": "success"
        },
        "data": {
          "additionalProperties": false,
          "properties": {
            "text": {
              "description": "Text entered by the user and returned after confirmation. This is a result field, not the input parameter for prefilled text.",
              "maxLength": 65536,
              "type": "string"
            }
          },
          "required": [
            "text"
          ],
          "type": "object"
        }
      },
      "required": [
        "status",
        "data"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "status": {
          "const": "failed"
        }
      },
      "required": [
        "status"
      ],
      "additionalProperties": false
    }
  ]
}
```

## showConfirm

显示确认对话框。`message` 为空且省略 `title` 时，调用会被拒绝。取消时返回 `confirmed=false`。

返回 `object`只能用于 `action.functionCall`，并声明客户端 `catalogId`

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `message` | string | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl) | 是 |  |
| `cancelText` | string | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl) | 否 |  |
| `confirmText` | string | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl) | 否 |  |
| `title` | string | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl) | 否 |  |

### 最小示例

```
{
  "call": "showConfirm",
  "args": {
    "message": "REPLACE_TEXT"
  },
  "catalogId": "urn:dingtalk:a2ui:host:v1"
}
```

### 返回结果

```
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "status": {
          "const": "success"
        },
        "data": {
          "additionalProperties": false,
          "properties": {
            "confirmed": {
              "type": "boolean"
            }
          },
          "required": [
            "confirmed"
          ],
          "type": "object"
        }
      },
      "required": [
        "status",
        "data"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "status": {
          "const": "failed"
        }
      },
      "required": [
        "status"
      ],
      "additionalProperties": false
    }
  ]
}
```

## showModal

显示带自定义按钮的对话框。目前支持 1–2 个按钮，参数必须预先求值。桌面端额外加的取消按钮返回空的 `selectedId`。

返回 `object`只能用于 `action.functionCall`，并声明客户端 `catalogId`

### 参数说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `buttons` | object | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl)[] | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl) | 是 |  |
| `message` | string | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl) | 是 |  |
| `title` | string | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl) | 否 |  |

### 最小示例

```
{
  "call": "showModal",
  "args": {
    "message": "REPLACE_TEXT",
    "buttons": [
      {
        "id": "REPLACE_TEXT",
        "title": "REPLACE_TEXT"
      }
    ]
  },
  "catalogId": "urn:dingtalk:a2ui:host:v1"
}
```

### 返回结果

```
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "status": {
          "const": "success"
        },
        "data": {
          "additionalProperties": false,
          "properties": {
            "selectedId": {
              "maxLength": 4096,
              "type": "string"
            }
          },
          "required": [
            "selectedId"
          ],
          "type": "object"
        }
      },
      "required": [
        "status",
        "data"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "status": {
          "const": "failed"
        }
      },
      "required": [
        "status"
      ],
      "additionalProperties": false
    }
  ]
}
```
