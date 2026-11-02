---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/dingtalk-document-overview"
namespace: "development"
slug: "dingtalk-document-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 文档 > 概述"
doc_id: "1wIYBdj3mq"
updated_at: "2026-05-15 18:18:02"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-document-overview
> Path: 应用开发 / 服务端 API / 文档/文件 > 文档 > 概述
> Updated: 2026-05-15 18:18:02

# 概述

钉钉文档 OpenAPI 提供了一套 RESTful 风格的接口，允许开发者通过程序化方式操作钉钉文档。你可以使用这些接口实现文档内容的自动化读写、块元素的增删改查、内容批量操作等功能，适用于文档自动生成、内容同步、智能写作等场景。

## 什么是钉钉文档

钉钉文档是阿里巴巴集团钉钉自主研发的企业协同办公套件，其包含文档、表格、脑图等在线创作工具。在日常使用中，无需下载文档即可通过电脑、手机或平板直接编辑和查看文档内容，文档内容实时自动保存。

同时，钉钉文档与钉钉深度整合，可基于组织关系与同事高效协作。使用钉钉文档还可以用于信息收集、项目管理、会议、业务汇报和新人入职等日常工作场景。更多功能介绍，请参见[钉钉使用手册-钉钉文档](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/od245kZmnOeW4D4L73YEWYbzxL6R0wMQ)。

![钉钉文档](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3518304361/p338100.png)

## 开放概览

### **开放接口列表**

文档提供了丰富的接口开放能力，开发者通过API接口可以实现文档的基础操作。

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [覆写文档（个人授权）](0579-api-docupdatecontent.md) | 以 Markdown 格式覆写整篇文档内容。  **[!NOTE]**  该方式需要用户授权后，才能调用该接口。 | 新版 |
| [覆写文档（应用授权）](0580-api-doc-updatecontent.md) | 以 Markdown 格式覆写整篇文档内容。  **[!NOTE]**  该方式通过应用凭证appKey、appSecret获取accessToken后即可调用。 | 新版 |
| [获取资源上传信息](0581-api-getresourceuploadinfo.md) | 查询文档指定资源的上传地址。 | 新版 |
| [插入内容](0582-api-insertcontent.md) | 在文档指定位置插入一段 Markdown 内容。 | 新版 |
| [查询块元素](0583-api-docblocksquery.md) | 查询文档根节点下的一级块元素列表。 | 新版 |
| [插入块元素](0584-api-docinsertblocks.md) | 在文档指定位置插入 1 个块元素。 | 新版 |
| [更新块元素](0585-api-docblocksmodify.md) | 更新文档中任意 1 个块元素的内容或属性。 | 新版 |
| [删除块元素](0586-api-docdeleteblock.md) | 删除文档中 1 个特定的块元素。 | 新版 |
| [在段落末尾追加文本](0587-api-docappendtext.md) | 向指定段落末尾追加一段文本。 | 新版 |
| [在段落末尾追加行内元素](0588-api-docappendparagraph.md) | 在指定段落末尾追加一个行内元素。 | 新版 |

### **回调事件列表**

- [文档导出任务完成事件](../04-LFcRvVD08N-事件订阅/0013-events-doc-export-completed.md)

## 名词解释

在使用钉钉文档 OpenAPI 之前，需要了解以下核心概念：

### **dentryUuid**

文档的唯一标识。以`https://alidocs.dingtalk.com/i/nodes/Z90D4da-id`为例，`dentryUuid`就是`Z90D4da-id`。

### **blockId**

块元素的唯一标识，可通过「查询块元素」接口获取。

### **operatorId**

操作人的`unionId`，用于标识执行操作的用户身份和权限校验。

### **BlockElement**

块元素，是文档内容的基本组成单位，如段落、标题、高亮块、表格等。

### **InlineElement**

行内元素，嵌套在块元素内部，如贴纸、图片、链接、插槽等。
