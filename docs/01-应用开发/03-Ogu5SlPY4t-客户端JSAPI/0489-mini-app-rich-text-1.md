---
title: "rich-text 富文本"
source_url: "https://open.dingtalk.com/document/development/mini-app-rich-text-1"
namespace: "development"
slug: "mini-app-rich-text-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 基础内容 > rich-text 富文本"
doc_id: "KtJOavMTY6"
updated_at: "2025-09-17 20:58:22"
---

> Source: https://open.dingtalk.com/document/development/mini-app-rich-text-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 基础内容 > rich-text 富文本
> Updated: 2025-09-17 20:58:22

# rich-text 富文本

本文介绍富文本组件的使用。

## 使用限制

1. 请使用[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)进行可用性判断。
2. 富文本里面写 js 不支持事件执行。
3. rich-text 支持 a 标签，不支持超链接。

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| nodes | Array | 节点列表。nodes 属性只支持使用 Array 类型。如果需要支持 HTML String，则需要自己将 HTML String 转化为 nodes 数组，可使用 [mini-html-parser](https://github.com/ant-mini-program/mini-html-parser) 转换。  rich-text 组件支持如下事件：   - tap - touchstart - touchmove - touchcancel - touchend   **默认值**：[] |

## **nodes 属性**

现支持两种节点：元素节点和文本节点，通过 type 来区分。

默认是元素节点，在富文本区域里显示的 HTML 节点。

- **元素节点**

  | **属性** | **类型** | 是否必填 | **说明** |
  | --- | --- | --- | --- |
  | type | String | 否 | 节点类型。  **默认值**： node。 |
  | name | String | 是 | 标签名，支持部分受信任的 HTML 节点，该项为必填项。 |
  | attrs | Object | 否 | 属性，支持部分受信任的属性，遵循 Pascal 命名法。 |
  | children | Array | 否 | 子节点列表，结构和 nodes 相同。 |

  下表列举了受信任的 HTML 节点及属性。支持 class 和 style 属性，不支持 id 属性。

  | **节点** | 额外支持的属性 |
  | --- | --- |
  | a | - |
  | abbr | - |
  | b | - |
  | blockquote | - |
  | br | - |
  | code | - |
  | col | span，width |
  | colgroup | span，width |
  | dd | - |
  | del | - |
  | div | - |
  | dl | - |
  | dt | - |
  | em | - |
  | fieldset | - |
  | h1 | - |
  | h2 | - |
  | h3 | - |
  | h4 | - |
  | h5 | - |
  | h6 | - |
  | hr | - |
  | i | - |
  | img | alt，src，height，width |
  | ins | - |
  | label | - |
  | legend | - |
  | li | - |
  | ol | start，type |
  | p | - |
  | q | - |
  | strong | - |
  | sub | - |
  | sup | - |
  | table | width |
  | tbody | - |
  | td | colspan，height，rowspan，width |
  | tfoot | -- |
  | th | colspan，height，rowspan，width |
  | thead | - |
  | tr | - |
  | ul | - |

  下表列举了支持的字符实体，其他字符实体会导致组件无法渲染。

  | **显示结果** | **描述** | **实体名称** |
  | --- | --- | --- |
  |  | 空格。 |  |
  | < | 小于号。 | < |
  | > | 大于号。 | > |
  | & | 和号。 | & |
  | " | 引号。 | " |
  | ' | 撇号。 |  |
- **文本节点**

  | **属性** | **类型** | **是否必填** | **说明** |
  | --- | --- | --- | --- |
  | type | String | 是 | 节点类型，type 为 text。 |
  | text | String | 是 | 文本。 |

## 示例代码

.axml示例代码：

```
<!--page/component/rich-text.axml-->
<view>
  <rich-text nodes="{{nodes}}" onTap="tap"></rich-text>
</view>
```

.js示例代码：

```
//  page/component/rich-text.js
Page({
  data: {
    nodes: [{
      name: 'div',
      attrs: {
        class: 'wrapper',
        style: 'color: orange;',
      },
      children: [{
        type: 'text',
        text: 'Hello World!',
      }],
    }],
  },
  tap() {
    console.log('tap');
  },
});
```

.acss 示例代码：

```
/*  page/component/rich-text.acss */
.wrapper {
  padding: 20rpx;
}
```
