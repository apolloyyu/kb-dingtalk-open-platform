---
title: "块元素数据结构"
source_url: "https://open.dingtalk.com/document/development/block-data-structure"
namespace: "development"
slug: "block-data-structure"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 文档 > 数据结构 > 块元素数据结构"
doc_id: "sXxRkHsFPf"
updated_at: "2026-03-31 09:57:00"
---

> Source: https://open.dingtalk.com/document/development/block-data-structure
> Path: 应用开发 / 服务端 API / 文档/文件 > 文档 > 数据结构 > 块元素数据结构
> Updated: 2026-03-31 09:57:00

# 块元素数据结构

一篇在线文档是由若干个块元素组成的树，不同类型的 BlockElment 内部可嵌套的元素的类型是不同，例如 高亮块 里可以嵌套任意的`BlockElement`，但是 段落块 下只能其嵌套 InlineElement 。

1 个块元素的数据结构如下：

```
{
  "blockType": enum(BlockType),             // 块元素类型，详见文档底部的 `BlockType` 枚举类型
  /**
   * 以下为所有支持的 Block 类型，如 Heading、Paragraph。 
   * 不同类型的 Block 有自己的 property。
  */
  "blockquote": Object(Callout),
  "callout": Object(Callout),
  "columns": Object(Columns),
  "heading": Object(Heading),
  "paragraph": Object(Paragraph),
  "orderedList": Object(OrderedList)
  "unorderedList": Object(UnorderedList),
  "table": Object(Table),
  // 每1种 Block 都有自己能支持的 BlockChildren，详见每个 Block 类型里的 `children` 的描述

  "children": BlockChildren[ ],

}
```

## 块元素数据结构说明

一篇在线文档由若干**块元素** 组成的树状结构构成。不同类型的块元素内部可嵌套的子元素类型不同：

- `callout`、`columns`的`children`只能是 **BlockElement 数组。**
- `paragraph`、`heading`、`orderedList`、`unorderedList`、`blockquote`的`children`只能是 **InlineElement 数组。**
- `table`暂不支持指定`children`。

### BlockType 枚举

| 枚举值 | 描述 |
| --- | --- |
| paragraph | 段落块。 |
| heading | 标题块。 |
| blockquote | 引用块。 |
| callout | 高亮块。 |
| columns | 分栏块。 |
| orderedList | 有序列表块。 |
| unorderedList | 无序列表块。 |
| table | 表格块。 |
| tableRow | 表格行块（表格块的子块）。 |
| tableCell | 表格单元格块（表格块的子块）。 |

> 暂未支持的元素类型统一返回`Undefined`。

### 段落

```
{
  "blockType": "paragraph",
  "paragraph": {
    "text": "段落文字内容",
    "indent": { "left": 32 },
    "folded": false
  },
  "children": [InlineElement]
}
```

| 字段名 | 类型 | 必填 | 含义 |
| --- | --- | --- | --- |
| text | string | 否 | 段落的文本内容。 |
| indent | object(Indent) | 否 | 缩进值，`left`必须是大于 0 的整数。 |
| folded | boolean | 否 | 是否折叠段落（折叠 indent 值比当前段落大的块元素）。 |

- `children`：**InlineElement 数组**。
- `paragraph`对象**不可省略**，内容为空时须传`{}`。

### 标题

```
{
  "blockType": "heading",
  "heading": {
    "level": 1,
    "text": "一级标题"
  },
  "children": [InlineElement]
}
```

| 字段名 | 类型 | 必填 | 含义 |
| --- | --- | --- | --- |
| text | string | 否 | 标题的文本内容。 |
| level | integer(enum) | 否 | 标题级别，取值`1`～`6`，1 表示一级标题。 |

- `children`：**InlineElement 数组。**

### 引用

```
{
  "blockType": "blockquote",
  "blockquote": {
    "text": "引用内容",
    "indent": { "left": 32 }
  },
  "children": [InlineElement]
}
```

| 字段名 | 类型 | 必填 | 含义 |
| --- | --- | --- | --- |
| text | string | 否 | 引用里的文字。 |
| indent | object(Indent) | 否 | 具体的缩进值。 |

- `children`：**InlineElement 数组。**

### 高亮块

```
{
  "blockType": "callout",
  "callout": {
    "sticker": "灯泡",
    "showstk": true,
    "color": "#333333",
    "border": "#FFD700",
    "bgcolor": "#FFF9C4"
  },
  "children": [BlockElement]
}
```

| 字段名 | 类型 | 必填 | 含义 |
| --- | --- | --- | --- |
| sticker | string(enum Emoji) | 否 | 表情编码，详见 [表情（Emoji）枚举值](0578-enumeration-values-of-emojis.md)。 |
| showstk | boolean | 否 | 是否显示表情。 |
| color | string | 否 | 字色。 |
| border | string | 否 | 边框颜色。 |
| bgcolor | string | 否 | 背景色。 |

- `children`：**BlockElement 数组**（不能是 InlineElement）。

### 分栏

```
{
  "blockType": "columns",
  "columns": {
    "size": 2,
    "noFill": false
  },
  "children": [BlockElement]
}
```

| 字段名 | 类型 | 必填 | 含义 |
| --- | --- | --- | --- |
| size | number | 否 | 分栏数量。 |
| noFill | boolean | 否 | 是否自动填充背景色。 |

- `children`：**BlockElement 数组**（不能是 InlineElement）。

### 有序列表

```
{
  "blockType": "orderedList",
  "orderedList": {
    "list": {
      "listId": "list-001",
      "level": 0,
      "listStyleType": "decimal",
      "listStyle": {
        "format": "decimal",
        "text": "%1.",
        "align": "left"
      },
      "symbolStyle": {
        "bold": false
      }
    },
    "indent": { "left": 32 }
  },
  "children": [InlineElement]
}
```

| 字段名 | 类型 | 必填 | 含义 |
| --- | --- | --- | --- |
| list | object(ListObject) | 是 | 有序列表的具体属性，详见[ListObject（列表对象）](#e6621bc176irg)说明。 |
| indent | object(Indent) | 否 | 缩进值，`left`必须是大于 0 的整数。 |

- `children`：**InlineElement 数组。**

### 无序列表

```
{
  "blockType": "unorderedList",
  "unorderedList": {
    "list": {
      "listId": "list-002",
      "level": 0,
      "listStyleType": "disc",
      "listStyle": {
        "format": "disc",
        "text": "%1",
        "align": "left"
      },
      "symbolStyle": {
        "bold": false
      }
    },
    "indent": { "left": 32 }
  },
  "children": [InlineElement]
}
```

| 字段名 | 类型 | 必填 | 含义 |
| --- | --- | --- | --- |
| list | object(ListObject) | 是 | 无序列表的具体属性，详见[ListObject（列表对象）](#e6621bc176irg)说明。 |
| indent | object(Indent) | 否 | 缩进值，`left`必须是大于 0 的整数。 |

- `children`：**InlineElement 数组**

### 表格

```
{
  "blockType": "table",
  "table": {
    "rolSize": 3,
    "colSize": 4,
    "cells": [
      ["Row1-Col1", "Row1-Col2", "Row1-Col3", "Row1-Col4"],
      ["Row2-Col1", "Row2-Col2", "Row2-Col3", "Row2-Col4"],
      ["Row3-Col1", "Row3-Col2", "Row3-Col3", "Row3-Col4"]
    ]
  }
}
```

| 字段名 | 类型 | 必填 | 含义 |
| --- | --- | --- | --- |
| rolSize | number | 是 | 行数。 |
| colSize | number | 是 | 列数。 |
| cells | String[][] | 否 | 单元格文本内容，二维String数组。 |

- `children`：**暂不支持**指定 children

## InlineElement 数据结构说明

行内元素用于文本类块元素（段落、标题、列表等）的`children`中。

### InlineType 枚举

| 枚举值 | 描述 |
| --- | --- |
| text | 文本。 |
| sticker | 表情。 |
| image | 图片。 |
| link | 链接。 |

### 文本

```
{
  "text": "加粗红色文字",
  "sz": 16,
  "color": "red",
  "highlight": "yellow",
  "bold": true,
  "italic": false,
  "stike": false,
  "underline": false,
  "fonts": "monospace"
}
```

| 字段名 | 类型 | 必填 | 含义 |
| --- | --- | --- | --- |
| text | string | 是 | 文本内容。 |
| sz | number | 否 | 字号（默认单位 px）。 |
| color | string | 否 | 文字颜色。 |
| highlight | string | 否 | 高亮背景色。 |
| bold | boolean | 否 | 是否加粗。 |
| italic | boolean | 否 | 是否斜体。 |
| stike | boolean | 否 | 是否中划线。 |
| underline | boolean | 否 | 是否下划线。 |
| fonts | string(enum Fonts) | 否 | 字体，枚举值如下：   - **monospace**：等宽字体 - **STSong**：华文宋体 - **Microsoft YaHei**：微软雅黑 - **FangSong\_GB2312**：仿宋 GB2312 - **Helvetica**：Helvetica 字体 - **Helvetica Neue**：Neue Helvetica 字体 - **Consolas**：Consolas 字体 - **宋体**：宋体 - **Impact**：Impact 字体 - **sanrif**：sanrif 字体 - **Calibri**：Calibri 字体 |

### 表情

```
{
  "elementType": "sticker",
  "properties": {
    "code": "大笑"
  }
}
```

| 字段名 | 类型 | 必填 | 含义 |
| --- | --- | --- | --- |
| code | string(enum Emoji) | 是 | 表情编码，详见[表情（Emoji）枚举值](0578-enumeration-values-of-emojis.md)。 |

### 图片

```
{
  "elementType": "image",
  "properties": {
    "src": "https://example.com/image.jpg"
  }
}
```

| 字段名 | 类型 | 必填 | 含义 |
| --- | --- | --- | --- |
| src | string | 否 | 图片资源地址。 |

### 链接

```
{
  "elementType": "link",
  "properties": {
    "href": "https://example.com"
  },
  "children": [
    { "text": "点击跳转链接" }
  ]
}
```

| 字段名 | 类型 | 必填 | 含义 |
| --- | --- | --- | --- |
| href | string | 否 | 链接地址。 |

- `children`：**Text 数组**，插入链接时必须指定`children`，且至少包含 1 个`text`不为空的文本节点。

## 通用数据结构

### Indent（缩进）

| 字段名 | 类型 | 必填 | 含义 | 示例 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 具体缩进值，必须是大于 0 的整数，否则报错。 | `32` |

---

### ListObject（列表对象）

| 字段名 | 类型 | 必填 | 含义 |
| --- | --- | --- | --- |
| listId | string | 否 | 当前列表的 ID；若插入多级有序列表，需确保同组多级列表的`listId`一致，否则展示错误。 |
| level | number | 是 | 列表的层级（从 0 开始）。 |
| listStyleType | string | 是 | 列表样式类型。 |
| listStyle | object(ListStyle) | 是 | 列表的具体样式，详见[ListStyle（列表样式）](#bad921c2ebc3h)说明。 |
| symbolStyle | object(SymbolStyle) | 否 | 列表符的样式，详见[SymbolStyle（列表符样式）](#b16d5427cbutg)说明。 |

---

### ListStyle（列表样式）

| 字段名 | 类型 | 必填 | 含义 |
| --- | --- | --- | --- |
| format | string | 是 | 项目符号格式。 |
| text | string | 是 | 文本。 |
| align | string | 是 | 对齐方式，如`left`、`center`、`right`。 |

---

### SymbolStyle（列表符样式）

| 字段名 | 类型 | 必填 | 含义 |
| --- | --- | --- | --- |
| sz | number | 否 | 项目符号字体大小。 |
| shd | string | 否 | 项目符号背景色。 |
| fonts | string | 否 | 项目符号字体格式。 |
| color | string | 否 | 项目符号字体颜色。 |
| bold | boolean | 否 | 是否加粗。 |
| strike | boolean | 否 | 是否展示删除线。 |
| italic | boolean | 否 | 是否展示斜体。 |

---

## Emoji 枚举值（表情编码完整列表）

以下枚举值可用于`callout.sticker`和行内表情元素`sticker.properties.code`。

|  |  |  |  |
| --- | --- | --- | --- |
| `优先级: 1` | `优先级: 2` | `优先级: 3` | `优先级: 4` |
| `优先级: 5` | `优先级: 6` | `优先级: 7` | `进度: 未开始` |
| `进度: 20%` | `进度: 40%` | `进度: 50%` | `进度: 70%` |
| `进度: 90%` | `进度: 已完成` | `微笑` | `憨笑` |
| `大笑` | `加油` | `色` | `偷笑` |
| `跳舞` | `捂脸哭` | `笑哭` | `流泪` |
| `疑问` | `傻笑` | `流鼻血` | `狗子` |
| `赞` | `OK` | `抱拳` | `向上` |
| `向下` | `向左` | `向右` | `资料` |
| `本子` | `笔记本` | `折线图` | `柱状图` |
| `羽毛笔` | `钢笔` | `警告` | `问号` |
| `禁止` | `禁行` | `锁` | `气泡` |
| `沙漏` | `公文包` | `火箭` | `火` |
| `奖牌` | `灯泡` | `钉子` | `旗子` |
| `茶` | `休假` | `气球` | `锦鲤` |
| `咖啡` | `奶茶` | `调色板` | `感谢` |
| `打招呼` | `666` | `握手` | `胜利` |
| `一点点` | `鼓掌` | `送花花` | `比心` |
| `加一` | `100分` | `KPI` | `对勾` |
| `爱心` | `可爱` | `发呆` | `老板` |
| `害羞` | `闭嘴` | `睡` | `大哭` |
| `尴尬` | `调皮` | `惊讶` | `流汗` |
| `广播` | `自信` | `你强` | `怒吼` |
| `惊愕` | `快哭了` | `无聊` | `吐` |
| `算账` | `晕` | `摸摸` | `飞吻` |
| `鄙视` | `嘘` | `思考` | `亲亲` |
| `感冒` | `对不起` | `再见` | `投降` |
| `哼` | `欠扁` | `坏笑` | `拜托` |
| `可怜` | `舒服` | `爱意` | `财迷` |
| `迷惑` | `PK` | `委屈` | `灵感` |
| `天使` | `鬼脸` | `凄凉` | `郁闷` |
| `吃瓜` | `嘿嘿` | `抠鼻` | `呲牙` |
| `彩虹` | `耶` | `捂眼睛` | `推眼镜` |
| `暗中观察` | `开心` | `惊喜` | `回头` |
| `发怒` | `忍者` | `衰` | `脑暴` |
| `冷笑` | `黑眼圈` | `恭喜` | `费解` |
| `收到` | `炸弹` | `白眼` | `一团乱麻` |
| `无奈` | `敲打` | `专注` | `忙疯了` |
| `鞠躬` | `摊手` | `抱抱` | `举手` |
| `跪了` | `猫咪` | `二哈` | `三多` |
| `承让` | `撒花` | `邮件` | `文档` |
| `演示` | `表格` | `生日快乐` | `心碎` |
| `红包` | `嘴唇` | `鲜花` | `残花` |
| `干杯` | `出差` | `时间` | `福` |
| `月饼` | `礼物` | `幼苗` | `烟花` |
| `灯笼` | `爆竹` | `鸡腿` | `高铁` |
| `三连` | `OKR` | `Done` |  |

---
