---
title: "公共类型"
source_url: "https://open.dingtalk.com/document/development/json-card-common-types"
namespace: "development"
slug: "json-card-common-types"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "构建卡片结构 > 公共类型"
doc_id: "ZR7VXtkVeZ"
updated_at: "2026-09-30 09:14:12"
---

> Source: https://open.dingtalk.com/document/development/json-card-common-types
> Path: 互动卡片 / JSON 构建卡片（AI） / 构建卡片结构 > 公共类型
> Updated: 2026-09-30 09:14:12

# 公共类型

## 基础类型

### ComponentId

组件唯一标识，同一画布内不可重复。

```
{"type": "string"}
```

### AccessibilityAttributes

为读屏软件等辅助技术提供名称和详细描述。

协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `label` | [DynamicString](#6b74f28968uj6) | 否 | 一个简短的字符串，通常 1 到 3 个词，辅助技术用它传达元素的用途或意图。例如输入框的无障碍标签可以是「用户 ID」，按钮可以是「提交」。 |
| `description` | [DynamicString](#6b74f28968uj6) | 否 | 辅助技术为元素提供的补充信息，例如操作说明、格式要求或操作结果。例如静音按钮的标签是「静音」，描述是「关闭该会话的通知提醒」。 |

### ComponentCommon

| 属性 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| `id` | [ComponentId](#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容 |
| `visible` | [DynamicBoolean](#e82066479fgkv) | 否 | 可见性（布尔表达式或字面量）。 |
| `metadata` | any | 否 |  |

### Child

对单个子组件 ID 的引用。

```
{"$ref": "#/$defs/ComponentId"}
```

### ChildList

```
{
  "oneOf": [
    {"type": "array", "items": {"$ref": "#/$defs/ComponentId"}, "description": "静态的子组件 ID 列表。"},
    {
      "type": "object",
      "description": "按数据模型中的列表动态生成子组件的模板。`componentId` 是用作模板的组件。",
      "properties": {
        "componentId": {"$ref": "#/$defs/ComponentId"},
        "path": {"type": "string", "description": "数据模型中组件属性对象列表的路径。"}
      },
      "required": ["componentId", "path"],
      "additionalProperties": false
    }
  ]
}
```

### DataBinding

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `path` | string | 是 | 数据模型路径，模板内可以使用相对路径，~ 只能写成 ~0 或 ~1。  求值上下文、路径规范化以及目标是否存在在运行时检查 |

### DynamicValue

通用值：字符串、数字、布尔值、数组、`null`、普通对象、数据绑定或值函数的结果。包含 `call` 的对象按函数调用解析；只有 `path` 一个键的对象按绑定解析。

```
{
  "oneOf": [
    {"type": "string"},
    {"type": "number"},
    {"type": "boolean"},
    {"type": "array"},
    {"type": "null"},
    {"$ref": "#/$defs/LiteralObject"},
    {"$ref": "#/$defs/DataBinding"},
    {"$ref": "#/$defs/FunctionCall"}
  ]
}
```

### DynamicString

取值可以是字符串字面量、指向数据模型中字符串的路径，或返回字符串的函数调用。

```
{"oneOf": [{"type": "string"}, {"$ref": "#/$defs/DataBinding"}, {"$ref": "#/$defs/FunctionCall"}]}
```

### DynamicNumber

数值型动态值：可以是 JSON 数字字面量、指向数值的数据绑定，或返回数值的函数调用。绑定和函数的运行时结果也必须是 JSON 数字；不会把字符串隐式转换为数字，数字字符串和 ISO 8601 日期时间字符串都无效。

```
{"oneOf": [{"type": "number"}, {"$ref": "#/$defs/DataBinding"}, {"$ref": "#/$defs/FunctionCall"}]}
```

### DynamicBoolean

布尔值，可以是字面量、路径，或返回布尔值的函数调用。

```
{"oneOf": [{"type": "boolean"}, {"$ref": "#/$defs/DataBinding"}, {"$ref": "#/$defs/FunctionCall"}]}
```

### DynamicStringList

取值可以是字符串数组字面量、指向数据模型中字符串数组的路径，或返回字符串数组的函数调用。

```
{
  "oneOf": [
    {"type": "array", "items": {"type": "string"}},
    {"$ref": "#/$defs/DataBinding"},
    {"$ref": "#/$defs/FunctionCall"}
  ]
}
```

### FunctionCommon

| 属性 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| `catalogId` | string | 否 | 函数 Catalog 标识。省略时使用所在画布的默认 Catalog。这不是 Schema 文件路径。 |

### FunctionCall

A2UI v1.0 的 `FunctionCall`：调用当前画布 Catalog 中注册的渲染器函数。

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `call` | string | 是 | 要调用的函数名。 |
| `catalogId` | string | 否 | 该函数的 Catalog ID，覆盖画布级别的默认 `catalogId`。 |
| `args` | object | 否 | 传给函数的参数。 |

### CheckRule

应用于输入组件的单条校验规则。

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `condition` | [DynamicBoolean](#e82066479fgkv) | 是 | 布尔值，可以是字面量、路径，或返回布尔值的函数调用。 |
| `message` | string | 是 | 校验不通过时显示的错误信息。 |

### Action

定义交互处理器，可以触发 Agent 侧事件，也可以执行渲染器本地函数。

```
{
  "oneOf": [
    {
      "type": "object",
      "description": "触发 Agent 侧事件。",
      "properties": {
        "event": {
          "type": "object",
          "description": "要派发给 Agent 的事件。",
          "properties": {
            "name": {"type": "string", "description": "要派发给 Agent 的动作名称。"},
            "context": {
              "type": "object",
              "description": "包含动作上下文键值对的 JSON 对象。取值可以是字面量或路径。除非取值必须动态绑定到数据模型，否则请使用字面量。不要用路径表示静态 ID。",
              "additionalProperties": {"$ref": "#/$defs/DynamicValue"}
            },
            "wantResponse": {
              "type": "boolean",
              "description": "请求响应的元数据。当前公开接入不保证标准的响应闭环；不要依赖设为 `true` 来自动生成响应。",
              "default": false
            },
            "responsePath": {
              "type": "string",
              "description": "标准的事件响应路径元数据。当前公开接入不保证自动回写。宿主函数的结果通过 `metadata.extensions.dt_actionBindingsV1` 回写；业务更新请使用 `updateDataModel` 或 `updateComponents`。"
            }
          },
          "required": ["name"],
          "additionalProperties": false
        }
      },
      "required": ["event"],
      "additionalProperties": false
    },
    {
      "type": "object",
      "description": "在渲染器本地执行函数。",
      "properties": {"functionCall": {"$ref": "#/$defs/FunctionCall"}},
      "required": ["functionCall"],
      "additionalProperties": false
    }
  ]
}
```

### Surface

保留的消息层类型，不代表开放了新的组件或主题能力。它是代表 A2UI 画布的保留容器组件。`Surface` 组件不可修改，其 `child` 始终为 `root`。

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容 |
| `visible` | [DynamicBoolean](#e82066479fgkv) | 否 | 可见性（布尔表达式或字面量）。 |
| `metadata` | any | 否 |  |
| `child` | root | 否 |  |

### IndexSystemFunction

从模板渲染动态列表时，返回当前项从 0 开始的下标。该函数只能在列表上下文中求值模板项时使用。

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `call` | @index | 是 |  |
| `args` | object | 否 |  |

### Extensions

可选的扩展元数据。键必须是 Unicode 标识符（UAX #31）。以 `a2ui_` 开头的键保留给官方扩展。

```
{
  "type": "object",
  "patternProperties": {"^[\\p{XID_Start}_][\\p{XID_Continue}]*$": {}},
  "additionalProperties": false
}
```

## 扩展类型

### LiteralObject

普通对象字面量。包含 `call` 的对象保留给函数调用，只有 `path` 一个键的对象保留给绑定，以免与动态表达式混淆。

```
{
  "type": "object",
  "not": {"anyOf": [{"required": ["call"]}, {"required": ["path"], "maxProperties": 1}]}
}
```

### HostStaticValueTree

对宿主参数子树求值阶段的约束；实际的值类型、路径和表达式是否合法，仍由现有运行时检查。

```
{
  "additionalProperties": {"$ref": "#/$defs/HostStaticValueTree"},
  "items": {"$ref": "#/$defs/HostStaticValueTree"}
}
```

### HostCompiledValueTree

对宿主参数子树求值阶段的约束；实际的值类型、路径和表达式是否合法，仍由现有运行时检查。

```
{
  "additionalProperties": {"$ref": "#/$defs/HostCompiledValueTree"},
  "items": {"$ref": "#/$defs/HostCompiledValueTree"},
  "not": {
    "type": "object",
    "properties": {
      "call": {
        "not": {
          "enum": [
            "eq",
            "ne",
            "lt",
            "lte",
            "gt",
            "gte",
            "add",
            "sub",
            "mul",
            "div",
            "mod",
            "cond",
            "and",
            "or",
            "not",
            "objectGet",
            "arrayGet",
            "arrayFind",
            "getLength",
            "toDouble",
            "toLong"
          ]
        }
      }
    },
    "required": ["call"]
  }
}
```

### HostResultPath

结果回写路径。只允许 `/ui/` 下的对象键，最多 256 个 ASCII 字符、16 段（含 `ui`）。禁止空段、纯数字段和转义序列。

```
{
  "type": "string",
  "maxLength": 256,
  "pattern": "^/ui/(?=[^/]*[A-Za-z_-])[A-Za-z0-9_-]+(?:/(?=[^/]*[A-Za-z_-])[A-Za-z0-9_-]+){0,14}$"
}
```

### HostActionBinding

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `resultPath` | [HostResultPath](#b3288d6c284iz) | 是 | 结果回写路径。   - 只允许 `/ui/` 下的对象键，最多 256 个 ASCII 字符、16 段（含 `ui`）。 - 禁止空段、纯数字段和转义序列。 |

### HostActionOwner

```
{
  "type": "object",
  "allOf": [
    {
      "if": {
        "properties": {
          "action": {
            "type": "object",
            "properties": {
              "functionCall": {
                "type": "object",
                "properties": {
                  "call": {
                    "enum": [
                      "copyText",
                      "openChat",
                      "previewImages",
                      "previewVideo",
                      "promptText",
                      "showConfirm",
                      "showModal"
                    ]
                  }
                },
                "required": ["call"]
              }
            },
            "required": ["functionCall"]
          }
        },
        "required": ["action"]
      },
      "then": {
        "properties": {
          "metadata": {
            "anyOf": [
              {"type": "null"},
              {
                "type": "object",
                "properties": {
                  "extensions": {
                    "type": "object",
                    "patternProperties": {"^dt_actionBindings(?!V1$)": false},
                    "properties": {
                      "dt_actionBindingsV1": {
                        "type": "object",
                        "properties": {"action": {"$ref": "#/$defs/HostActionBinding"}},
                        "required": ["action"]
                      }
                    }
                  }
                }
              }
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "onComplete": {
            "type": "object",
            "properties": {
              "functionCall": {
                "type": "object",
                "properties": {
                  "call": {
                    "enum": [
                      "copyText",
                      "openChat",
                      "previewImages",
                      "previewVideo",
                      "promptText",
                      "showConfirm",
                      "showModal"
                    ]
                  }
                },
                "required": ["call"]
              }
            },
            "required": ["functionCall"]
          }
        },
        "required": ["onComplete"]
      },
      "then": {
        "properties": {
          "metadata": {
            "anyOf": [
              {"type": "null"},
              {
                "type": "object",
                "properties": {
                  "extensions": {
                    "type": "object",
                    "patternProperties": {"^dt_actionBindings(?!V1$)": false},
                    "properties": {
                      "dt_actionBindingsV1": {
                        "type": "object",
                        "properties": {"onComplete": {"$ref": "#/$defs/HostActionBinding"}},
                        "required": ["onComplete"]
                      }
                    }
                  }
                }
              }
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "onLinkClick": {
            "type": "object",
            "properties": {
              "functionCall": {
                "type": "object",
                "properties": {
                  "call": {
                    "enum": [
                      "copyText",
                      "openChat",
                      "previewImages",
                      "previewVideo",
                      "promptText",
                      "showConfirm",
                      "showModal"
                    ]
                  }
                },
                "required": ["call"]
              }
            },
            "required": ["functionCall"]
          }
        },
        "required": ["onLinkClick"]
      },
      "then": {
        "properties": {
          "metadata": {
            "anyOf": [
              {"type": "null"},
              {
                "type": "object",
                "properties": {
                  "extensions": {
                    "type": "object",
                    "patternProperties": {"^dt_actionBindings(?!V1$)": false},
                    "properties": {
                      "dt_actionBindingsV1": {
                        "type": "object",
                        "properties": {"onLinkClick": {"$ref": "#/$defs/HostActionBinding"}},
                        "required": ["onLinkClick"]
                      }
                    }
                  }
                }
              }
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "onPreview": {
            "type": "object",
            "properties": {
              "functionCall": {
                "type": "object",
                "properties": {
                  "call": {
                    "enum": [
                      "copyText",
                      "openChat",
                      "previewImages",
                      "previewVideo",
                      "promptText",
                      "showConfirm",
                      "showModal"
                    ]
                  }
                },
                "required": ["call"]
              }
            },
            "required": ["functionCall"]
          }
        },
        "required": ["onPreview"]
      },
      "then": {
        "properties": {
          "metadata": {
            "anyOf": [
              {"type": "null"},
              {
                "type": "object",
                "properties": {
                  "extensions": {
                    "type": "object",
                    "patternProperties": {"^dt_actionBindings(?!V1$)": false},
                    "properties": {
                      "dt_actionBindingsV1": {
                        "type": "object",
                        "properties": {"onPreview": {"$ref": "#/$defs/HostActionBinding"}},
                        "required": ["onPreview"]
                      }
                    }
                  }
                }
              }
            ]
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "onTap": {
            "type": "object",
            "properties": {
              "functionCall": {
                "type": "object",
                "properties": {
                  "call": {
                    "enum": [
                      "copyText",
                      "openChat",
                      "previewImages",
                      "previewVideo",
                      "promptText",
                      "showConfirm",
                      "showModal"
                    ]
                  }
                },
                "required": ["call"]
              }
            },
            "required": ["functionCall"]
          }
        },
        "required": ["onTap"]
      },
      "then": {
        "properties": {
          "metadata": {
            "anyOf": [
              {"type": "null"},
              {
                "type": "object",
                "properties": {
                  "extensions": {
                    "type": "object",
                    "patternProperties": {"^dt_actionBindings(?!V1$)": false},
                    "properties": {
                      "dt_actionBindingsV1": {
                        "type": "object",
                        "properties": {"onTap": {"$ref": "#/$defs/HostActionBinding"}},
                        "required": ["onTap"]
                      }
                    }
                  }
                }
              }
            ]
          }
        }
      }
    }
  ]
}
```

## 视觉 Token

### SizeToken

DDesign 原生字号 Token ID，用于 `Text`.`sizeToken`。请按具体用途优先选择带 \_\_font\_size 后缀的 ID；实际字号由当前宿主解析，不保证各平台的字号或行高一致，也不会自动套用同名的 UIFont 样式。font-size/body 这类设计名、不带后缀的样式名以及 \_\_line\_height 键都不是这里的字号 ID。

| **取值** | **说明** |
| --- | --- |
| `common_largetitle_text_style__font_size` | 大标题，用作页面或主要内容区的标题。 |
| `common_supertitle_text_style__font_size` | 特大标题，用作页面或模块的主标题。 |
| `common_h1_text_style__font_size` | 一级标题，用于卡片或内容区的标题。 |
| `common_h2_text_style__font_size` | 二级标题，用于内容分组的标题。 |
| `common_h3_text_style__font_size` | 三级标题，用于更小层级的内容标题。 |
| `common_h4_text_style__font_size` | 四级标题，用于副标题或标题下的补充信息。 |
| `common_body_text_style__font_size` | 正文，用于主要内容。 |
| `common_action_text_style__font_size` | 操作文字，用于按钮、链接等操作类文案。 |
| `common_description_text_style__font_size` | 辅助说明，用于次要信息和补充说明。 |
| `common_footnote_text_style__font_size` | 脚注，用于来源、备注、图片说明或状态标签。 |
| `common_tiny_text_style__font_size` | 小号提示文字，用于空间受限场景中的轻提示。 |
| `common_subhead_text_style__font_size` | 副标题，用于标题下方的补充信息。 |
| 其他字符串 | 兼容已有的字符串输入。上面各项是已知原生 Token 的选用说明，并不是封闭枚举；使用其他 Token 前须确认客户端已注册。Schema 接受字符串不代表该 Token 可用，客户端找不到时会回落到 variant 对应的样式。 |

### ColorToken

只能使用下表列出的 57 个 Token ID，名称区分大小写。说明中写明了用途和状态含义；实际色值与透明度由宿主按当前平台和主题解析，本协议不固定色值。

| **取值** | **说明** |
| --- | --- |
| `extended_yellow0_color` | 黄色背景色；用于该色系区域的背景填充。 |
| `extended_yellow1_color` | 黄色边框色；用于该色系区域的描边。 |
| `extended_yellow6_color` | 黄色文字色；用于该色系的文字强调。 |
| `extended_orange0_color` | 橙色背景色；用于该色系区域的背景填充。 |
| `extended_orange1_color` | 橙色边框色；用于该色系区域的描边。 |
| `extended_orange6_color` | 橙色文字色；用于该色系的文字强调。 |
| `extended_red0_color` | 红色背景色；用于该色系区域的背景填充。 |
| `extended_red1_color` | 红色边框色；用于该色系区域的描边。 |
| `extended_red6_color` | 红色文字色；用于该色系的文字强调。 |
| `extended_magenta0_color` | 品红背景色；用于该色系区域的背景填充。 |
| `extended_magenta1_color` | 品红边框色；用于该色系区域的描边。 |
| `extended_magenta6_color` | 品红文字色；用于该色系的文字强调。 |
| `extended_purple0_color` | 紫色背景色；用于该色系区域的背景填充。 |
| `extended_purple1_color` | 紫色边框色；用于该色系区域的描边。 |
| `extended_purple6_color` | 紫色文字色；用于该色系的文字强调。 |
| `extended_deeppurple0_color` | 深紫背景色；用于该色系区域的背景填充。 |
| `extended_deeppurple1_color` | 深紫边框色；用于该色系区域的描边。 |
| `extended_deeppurple6_color` | 深紫文字色；用于该色系的文字强调。 |
| `extended_blue0_color` | 蓝色背景色；用于该色系区域的背景填充。 |
| `extended_blue1_color` | 蓝色边框色；用于该色系区域的描边。 |
| `extended_blue6_color` | 蓝色文字色；用于该色系的文字强调。 |
| `extended_darkgreen0_color` | 深绿背景色；用于该色系区域的背景填充。 |
| `extended_darkgreen1_color` | 深绿边框色；用于该色系区域的描边。 |
| `extended_darkgreen6_color` | 深绿文字色；用于该色系的文字强调。 |
| `extended_green0_color` | 绿色背景色；用于该色系区域的背景填充。 |
| `extended_green1_color` | 绿色边框色；用于该色系区域的描边。 |
| `extended_green6_color` | 绿色文字色；用于该色系的文字强调。 |
| `common_level1_base_color` | 一级文字与图标；用于标题、正文等主要信息。 |
| `common_level2_base_color` | 二级文字与图标；用于次要信息和辅助图标。 |
| `common_level3_base_color` | 三级文字与图标；用于更弱的补充信息。 |
| `common_level4_base_color` | 禁用状态的文字与图标颜色；只表达视觉状态。 |
| `common_stamp_color` | 水印色；用于低干扰的水印内容。 |
| `common_link_color` | 超链接文字与高亮边框颜色。 |
| `common_bg_color` | 区域背景色；用于页面或内容区的背景。 |
| `common_fg_z1_color` | 前景区域背景色；用于叠在基础背景之上的内容区。 |
| `common_line_light_color` | 弱分割线；用于较轻的内容分隔。 |
| `common_line_hard_color` | 强分割线；用于需要更清晰边界的内容分隔。 |
| `common_red1_color` | 危险状态色；用于传达危险或错误的语义。 |
| `common_orange1_color` | 警示状态色；用于需要用户注意的提示。 |
| `common_green1_color` | 成功状态色；用于成功或完成的反馈。 |
| `common_white1_color` | 白色蒙层；用于白色叠加，实际透明度由客户端主题资源决定。 |
| `common_white2_color` | 白色蒙层（设计为 40% 档）；用于白色叠加，实际透明度由客户端主题资源决定。 |
| `common_white3_color` | 白色蒙层（设计为 30% 档）；用于白色叠加，实际透明度由客户端主题资源决定。 |
| `common_white4_color` | 白色蒙层（设计为 20% 档）；用于白色叠加，实际透明度由客户端主题资源决定。 |
| `common_white5_color` | 白色蒙层（设计为 10% 档）；用于白色叠加，实际透明度由客户端主题资源决定。 |
| `common_white6_color` | 白色蒙层（设计为 5% 档）；用于白色叠加，实际透明度由客户端主题资源决定。 |
| `common_black1_color` | 黑色蒙层；用于黑色叠加，实际透明度由客户端主题资源决定。 |
| `common_black2_color` | 黑色蒙层（设计为 40% 档）；用于黑色叠加，实际透明度由客户端主题资源决定。 |
| `common_black3_color` | 黑色蒙层（设计为 30% 档）；用于黑色叠加，实际透明度由客户端主题资源决定。 |
| `common_black4_color` | 黑色蒙层（设计为 20% 档）；用于黑色叠加，实际透明度由客户端主题资源决定。 |
| `common_black5_color` | 黑色蒙层（设计为 10% 档）；用于黑色叠加，实际透明度由客户端主题资源决定。 |
| `common_black6_color` | 黑色蒙层（设计为 5% 档）；用于黑色叠加，实际透明度由客户端主题资源决定。 |
| `theme_primary3_color` | 主题背景色；用于承载主题样式的区域背景。 |
| `theme_primary2_color` | 浅主题色；用于较浅的主题色高亮和辅助装饰。 |
| `theme_primary_hover_color` | 主题悬停色；用于指针悬停时主题色的视觉反馈。 |
| `theme_primary1_color` | 主题主色；用于主要的主题强调。 |
| `theme_primary_press_color` | 主题按下色；用于按下时主题色的视觉反馈。 |

### IconName

公共类型 `IconName`：`Icon.name` 引用的 24 个公开字体图标名，区分大小写。下面列出每个图标的视觉含义和用途。

| **取值** | **说明** |
| --- | --- |
| `Search_L_outlined` | 搜索。用于搜索、搜索内容、搜索文件、搜索图片。 |
| `Language_L_outlined` | 语言切换图标，常用于联网搜索。 |
| `CodeProgram_L_outlined` | 代码。用于在终端中运行命令。 |
| `Picture_L_outlined` | 图片。用于生成图片。 |
| `Folder_L_outlined` | 文件夹。用于读取文件。 |
| `Edit_L_outlined` | 编辑或笔图标。用于写入和创建文件。 |
| `ListView_L_outlined` | 列表视图 1。用于列出文件。 |
| `ManagementBackground_L_outlined` | 管理后台图标，常用于浏览器访问。 |
| `Tool_L_outlined` | 工具。用于调用工具、Workspace 工具集、MCP 工具集、DWS 工具集、MCP 调用，以及通用兜底。 |
| `Delete_L_outlined` | 删除。用于删除文件。 |
| `SpinLoading_L_outlined` | 加载中图标。用于 Skill 加载等加载状态；图标名本身不会开启旋转动画。 |
| `UploadOne_L_outlined` | 上传。用于上传文件。 |
| `DownloadAndSave_L_outlined` | 下载并保存。用于下载文件。 |
| `Check_L_outlined` | 对勾。用于表示完成或成功。 |
| `Copy_L_outlined` | 复制。用于复制文字、内容或结果。 |
| `Close_L_outlined` | 关闭、叉号。用于关闭弹窗、面板或页面。 |
| `More_L_outlined` | 更多、省略号、三个点。用于打开更多操作菜单。 |
| `Error_L_outlined` | 警告、错误提醒、带感叹号的圆圈。用于表示操作失败或异常状态。 |
| `InformationThere_L_outlined` | 信息提示，圆形字母 i。用于显示说明或附加信息。 |
| `Setting_L_outlined` | 设置、齿轮。用于打开设置或调整配置。 |
| `ExpandThere_L_outlined` | 展开。用于放大内容区或展开面板。 |
| `Collapse_L_outlined` | 收起。用于缩小内容区或收起面板。 |
| `Link_L_outlined` | 链接、链条。用于插入链接或打开相关地址。 |
| `Share_L_outlined` | 分享、转发。用于分享内容、会话或结果。 |
