---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/ai-table-overview"
namespace: "development"
slug: "ai-table-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "AI 表格 > 概述"
doc_id: "lv0jsiuxbw"
updated_at: "2026-05-15 09:02:57"
---

> Source: https://open.dingtalk.com/document/development/ai-table-overview
> Path: 应用开发 / 服务端 API / AI 表格 > 概述
> Updated: 2026-05-15 09:02:57

# 概述

## **什么是AI 表格**

AI表格是钉钉开放平台提供的一种智能化数据管理工具，本质上是一篇包含多个数据表（Sheet）的文档（Base），用于高效存储、处理和自动化业务流程。

AI 表格支持丰富的自动化场景，例如包装批次码与出库编码的智能比对、电商评价实时同步至群聊并沉淀到多维表等，大幅提升企业数据处理效率。自2025年9月1日起，AI表格的服务端OpenAPI已纳入钉钉企业自建应用的付费计量体系，标准版组织每月享有固定免费调用额度，用尽后提供最长5天的缓冲保护期。开发者可结合自动化模板、机器人触发器等能力，快速构建定制化业务流。

## **开放概览**

AI 表格提供了丰富的接口开放能力，开发者通过API接口可以实现AI 表格的管理。

### 数据表

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建数据表](0459-api-createsheet.md) | 在AI表格中创建一个新的数据表。 | 新版 |
| [获取数据表](0460-api-notable-getsheet.md) | 获取AI表格中一个数据表的信息。 | 新版 |
| [获取所有数据表](0461-api-notable-getallsheets.md) | 获取AI表格所有的数据表。 | 新版 |
| [更新数据表](0462-api-noatable-updatesheet.md) | 更新一个数据表的信息。 | 新版 |
| [删除数据表](0463-api-noatable-deletesheet.md) | 在AI表格中删除一个数据表。 | 新版 |

### 字段

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建字段](0464-api-noatable-createfield.md) | 在数据表中创建一个字段。 | 新版 |
| [更新字段](0465-api-noatable-updatefield.md) | 在数据表中更新一个字段。 | 新版 |
| [获取所有字段](0466-api-noatable-getallfields.md) | 获取在数据表中的所有字段。 | 新版 |
| [删除字段](0467-api-noatable-deletefield.md) | 在AI表格中删除一个字段。 | 新版 |

### 记录

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [新增记录](0468-api-notable-insertrecords.md) | 在AI表格里的指定数据表中新增行记录。 | 新版 |
| [获取记录](0469-api-getrecord.md) | 获取AI表格中的一行记录。 | 新版 |
| [列出多行记录](0470-api-notable-listrecords.md) | 获取AI表格里指定数据表的多行记录。 | 新版 |
| [更新多行记录](0471-api-noatable-updaterecords.md) | 在数据表中更新多行记录。 | 新版 |
| [删除多行记录](0472-api-noatable-deleterecords.md) | 删除数据表中的多行记录。 | 新版 |
