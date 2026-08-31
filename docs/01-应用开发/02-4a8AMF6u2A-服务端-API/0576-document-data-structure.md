---
title: "文档数据结构"
source_url: "https://open.dingtalk.com/document/development/document-data-structure"
namespace: "development"
slug: "document-data-structure"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 文档 > 数据结构 > 文档数据结构"
doc_id: "texdgg24Fb"
updated_at: "2026-03-31 09:56:49"
---

> Source: https://open.dingtalk.com/document/development/document-data-structure
> Path: 应用开发 / 服务端 API / 文档/文件 > 文档 > 数据结构 > 文档数据结构
> Updated: 2026-03-31 09:56:49

# 文档数据结构

一篇在线文档是由若干个块元素组成的树，不同类型的 `BlockElment` 内部可嵌套的元素的类型是不同，例如 `高亮块` 里可以嵌套任意的 `BlockElement`，但是 `段落块` 下只能其嵌套 `InlineElement`。一篇文档的结构大致如下：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3524684771/p1063438.png)

以这篇文档为例，拆解页面如下：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3524684771/p1063439.png)
