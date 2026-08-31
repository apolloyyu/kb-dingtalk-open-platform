---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/development/documentation-faq"
namespace: "development"
slug: "documentation-faq"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 文档 > 常见问题"
doc_id: "XqDrSNSLeu"
updated_at: "2026-03-31 10:01:36"
---

> Source: https://open.dingtalk.com/document/development/documentation-faq
> Path: 应用开发 / 服务端 API / 文档/文件 > 文档 > 常见问题
> Updated: 2026-03-31 10:01:36

# 常见问题

## 内容写入

### 如何将 Markdown 格式的内容写入钉钉文档？

有两种方式可以将 Markdown 内容写入文档：

- **方式一：插入内容（追加，不影响已有内容）**

  调用[插入内容](0582-api-insertcontent.md)接口，将 Markdown 内容插入到文档指定位置：

  ```
  curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{documentId}/content?operatorId={operatorId}' \
  --header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{
    "content": {
      "type": "markdown",
      "content": "# 一级标题\n\n这是一段正文内容。"
    }
  }'
  ```
- **方式二：覆写文档（清空后重写）**

  调用[覆写文档（应用授权）](0580-api-doc-updatecontent.md)接口，以 Markdown 格式覆写文档全部内容：

  ```
  curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/overwriteContent?operatorId={operatorId}' \
  --header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{
    "content": "# 文档标题\n\n正文内容。",
    "dataType": "markdown"
  }'
  ```

  覆写文档会**清空**文档现有全部内容，属于破坏性操作，请谨慎使用。如果只需追加内容，请使用插入内容接口。

## 块元素操作

### 如何插入带内容的段落

调用[插入块元素](0584-api-docinsertblocks.md)接口，在文档中插入一个段落块，并通过`children`字段指定段落内的行内元素：

```
curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{dentryUuid}/blocks?operatorId={operatorId}' \
--header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
--header 'Content-Type: application/json' \
--data '{
  "element": {
    "blockType": "paragraph",
    "paragraph": {},
    "children": [
      {
        "text": "这是一段加粗的红色文字",
        "bold": true,
        "color": "#FF5733"
      },
      {
        "elementType": "sticker",
        "properties": { "code": "大笑" }
      }
    ]
  }
}'
```

如果调用成功，预计将返回以下格式数据：

```
{
  "result": {
    "data": {
      "paragraph": { "text": "这是一段加粗的红色文字" },
      "blockType": "paragraph",
      "index": 0,
      "id": "......"
    }
  },
  "success": true
}
```

`paragraph`对象不能被省略，即使段落无特殊属性，也需要传入空对象`{}`。

### 如何在文档指定位置（而非末尾）插入块元素

调用[插入块元素](0584-api-docinsertblocks.md)接口时，通过`blockId`或`index`指定目标位置，并通过`where`参数控制插入到目标位置之前还是之后：

```
curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks?operatorId={operatorId}' \
--header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
--header 'Content-Type: application/json' \
--data '{
  "element": {
    "blockType": "paragraph",
    "paragraph": {}
  },
  "blockId": "lc4si5p3n84zwqxxx",
  "where": "before"
}'
```

| 参数 | 说明 |
| --- | --- |
| `blockId` | 目标块的唯一标识，插入到该块之前或之后 |
| `index` | 当`blockId`不存在时，使用文档第`index`个一级块作为目标位置（从 0 开始） |
| `where` | `"before"`表示插入到目标位置之前，`"after"`表示之后（默认为`"after"`） |

### 如何插入标题

调用[插入块元素](0584-api-docinsertblocks.md)接口，将`blockType`设置为`heading`，并在`heading`对象中通过`level`指定标题级别（1~6）：

```
curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks?operatorId={operatorId}' \
--header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
--header 'Content-Type: application/json' \
--data '{
  "element": {
    "blockType": "heading",
    "heading": {
      "level": 2,
      "text": "这是一个二级标题"
    }
  }
}'
```

如果调用成功，预计将返回以下格式数据：

```
{
  "success": true
}
```

`heading.level` 与标题级别的对应关系：

| level 值 | 对应标题 |
| --- | --- |
| `1` | 一级标题（H1） |
| `2` | 二级标题（H2） |
| `3` | 三级标题（H3） |
| `4` | 四级标题（H4） |
| `5` | 五级标题（H5） |
| `6` | 六级标题（H6） |

### 如何插入引用块

调用[插入块元素](0584-api-docinsertblocks.md)接口，将`blockType`设置为`blockquote`，并在`blockquote`对象中传入引用内容：

```
curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks?operatorId={operatorId}' \
--header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
--header 'Content-Type: application/json' \
--data '{
  "element": {
    "blockType": "blockquote",
    "blockquote": {
      "text": "这是一段引用内容"
    }
  }
}'
```

如果调用成功，预计将返回以下格式数据：

```
{
  "result": {
    "data": {
      "blockType": "blockquote",
      "index": 4,
      "id": "......"
    }
  },
  "success": true
}
```

### 如何插入高亮块并在其中嵌套段落

高亮块的`children`只能是`BlockElement`数组。调用[插入块元素](0584-api-docinsertblocks.md)接口时，在`children`中传入子段落：

```
curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks?operatorId={operatorId}' \
--header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
--header 'Content-Type: application/json' \
--data '{
  "element": {
    "blockType": "callout",
    "callout": {
      "sticker": "灯泡",
      "showstk": true,
      "bgcolor": "#FFF9C4",
      "border": "#FFD700"
    },
    "children": [
      {
        "blockType": "paragraph",
        "paragraph": { "text": "这是高亮块内的段落内容" }
      }
    ]
  }
}'
```

不同类型块元素的`children`类型不同：段落块的`children`只能是行内元素；高亮块的`children`只能是块元素。

### 如何插入分栏

调用[插入块元素](0584-api-docinsertblocks.md)接口，将`blockType`设置为`columns`，通过`columns.size`指定分栏数量，并在`children`中传入各栏的块元素内容：

```
curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks?operatorId={operatorId}' \
--header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
--header 'Content-Type: application/json' \
--data '{
  "element": {
    "blockType": "columns",
    "columns": {
      "size": 2,
      "noFill": false
    },
    "children": [
      {
        "blockType": "paragraph",
        "paragraph": { "text": "左栏内容" }
      },
      {
        "blockType": "paragraph",
        "paragraph": { "text": "右栏内容" }
      }
    ]
  }
}'
```

如果调用成功，预计将返回以下格式数据：

```
{
  "result": {
    "data": {
      "columns": { "size": 2 },
      "blockType": "columns",
      "index": 7,
      "id": "......"
    }
  },
  "success": true
}
```

`columns` 对象的字段说明：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `size` | Number | 分栏数量 |
| `noFill` | Boolean | 是否自动填充背景色，默认`false` |

`columns`的`children`只能是 **BlockElement 数组**，不能是行内元素。

### 如何插入有序列表

调用[插入块元素](0584-api-docinsertblocks.md)接口，将`blockType`设置为`orderedList`，并在`orderedList`对象中传入列表属性，在`children`中传入列表项文本：

```
curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks?operatorId={operatorId}' \
--header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
--header 'Content-Type: application/json' \
--data '{
  "element": {
    "blockType": "orderedList",
    "orderedList": {
      "list": {
        "listId": "my-ordered-list-001",
        "level": 0,
        "listStyleType": "decimal",
        "listStyle": {
          "format": "decimal",
          "text": "%1.",
          "align": "left"
        }
      }
    },
    "children": [
      { "text": "有序列表第一项" }
    ]
  }
}'
```

如果调用成功，预计将返回以下格式数据：

```
{
  "result": {
    "data": {
      "blockType": "orderedList",
      "index": 6,
      "id": "......"
    }
  },
  "success": true
}
```

`list` 对象的常用字段说明：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `listId` | String | 列表的唯一标识，同一列表的多个列表项应使用相同的`listId` |
| `level` | Number | 列表缩进层级，从`0`开始 |
| `listStyleType` | String | 列表样式类型，有序列表使用`"decimal"` |

### 如何插入无序列表

调用[插入块元素](0584-api-docinsertblocks.md)接口，将`blockType`设置为`unorderedList`，并在`unorderedList`对象中传入列表属性，在`children`中传入列表项文本：

```
curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks?operatorId={operatorId}' \
--header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
--header 'Content-Type: application/json' \
--data '{
  "element": {
    "blockType": "unorderedList",
    "unorderedList": {
      "list": {
        "listId": "my-unordered-list-001",
        "level": 0,
        "listStyleType": "disc",
        "listStyle": {
          "format": "disc",
          "text": "%1",
          "align": "left"
        }
      }
    },
    "children": [
      { "text": "无序列表第一项" }
    ]
  }
}'
```

如果调用成功，预计将返回以下格式数据：

```
{
  "result": {
    "data": {
      "blockType": "unorderedList",
      "index": 8,
      "id": "......"
    }
  },
  "success": true
}
```

有序列表和无序列表的`listId`用于将多个列表项关联为同一个列表。若要插入同一列表的多个列表项，每个列表项应使用相同的`listId`，可通过 BatchOperate 批量接口一次性插入。

## 查询操作

### 如何获取文档中所有块元素的 blockId？

调用[查询块元素](0583-api-docblocksquery.md)接口，获取文档根节点下的一级块元素列表，每个元素包含其`id`（即`blockId`）：

```
curl --location --request GET 'https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks?operatorId={operatorId}' \
--header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}'
```

如果调用成功，预计将返回以下格式数据：

```
{
  "success": true,
  "result": {
    "data": [
      {
        "heading": { "level": "heading-1", "text": "文档标题" },
        "blockType": "heading",
        "index": 0,
        "id": "......"
      },
      {
        "paragraph": { "text": "正文内容。" },
        "blockType": "paragraph",
        "index": 1,
        "id": "......"
      }
    ]
  }
}
```

目前查询块元素接口**仅支持查询文档根节点下的一级块元素**，不支持递归查询嵌套在高亮块等容器内的子块元素。
