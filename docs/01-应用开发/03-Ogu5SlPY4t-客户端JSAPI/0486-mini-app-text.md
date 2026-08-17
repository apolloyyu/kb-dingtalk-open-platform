---
title: "text 文本"
source_url: "https://open.dingtalk.com/document/development/mini-app-text"
namespace: "development"
slug: "mini-app-text"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 基础内容 > text 文本"
doc_id: "AFEBqc9sW8"
updated_at: "2025-09-17 20:58:20"
---

> Source: https://open.dingtalk.com/document/development/mini-app-text
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 基础内容 > text 文本
> Updated: 2025-09-17 20:58:20

# text 文本

本文介绍文本组件的使用。

组件内只支持 <text/> 嵌套。

## 在线体验

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| selectable | Boolean | 是否可选。  **默认值**：false。 |
| class | String | 样式名。 |
| style | String | 内联样式。 |

## 示例代码

```
<view class="page">
  <view class="text-view">
    <text>{{text}}</text>
  </view>
</view>
```

```
Page({
  data: {
    text: `钉钉是一种工作方式。
      酷公司，用钉钉。\n\n:)
    `,
  },
})
```
