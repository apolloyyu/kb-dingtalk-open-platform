---
title: "Hyperlink"
source_url: "https://open.dingtalk.com/document/development/hyperlink"
namespace: "development"
slug: "hyperlink"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "酷应用 > 文档酷应用 > API参考文档 > Hyperlink"
doc_id: "51JiIiJg0A"
updated_at: "2025-08-27 18:09:35"
---

> Source: https://open.dingtalk.com/document/development/hyperlink
> Path: 应用开发 / 客户端 JSAPI / 酷应用 > 文档酷应用 > API参考文档 > Hyperlink
> Updated: 2025-08-27 18:09:35

# Hyperlink

## API描述

超链接。用于Range.getHyperlink()或者Range.setHyperlink() API中访问超链接。

## 属性说明

| 属性 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 超链接的类型，可选择以下值。   - **path**：网页链接 - **sheet**：表格引用 - **range**：单元格引用 |
| link | string | 是 | 链接的内容。   - 当type为path，是一个普通网页链接。 - 当type为sheet，是一个SheetName，例如sheet1。 - 当type为range，是一个引用，例如Sheet1!A1。 |
| text | string | 否 | 单元格显示的内容，任意文本。 |
