---
title: "SearchOptions"
source_url: "https://open.dingtalk.com/document/development/searchoptions"
namespace: "development"
slug: "searchoptions"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "酷应用 > 文档酷应用 > API参考文档 > SearchOptions"
doc_id: "mTu9X899HT"
updated_at: "2025-08-27 18:09:36"
---

> Source: https://open.dingtalk.com/document/development/searchoptions
> Path: 应用开发 / 客户端 JSAPI / 酷应用 > 文档酷应用 > API参考文档 > SearchOptions
> Updated: 2025-08-27 18:09:36

# SearchOptions

## API描述

搜索选项。用于Sheet.findAll()、Range.find()、Range.findNext()或者Range.findPrevious()等API中指定搜索方式。

## 属性说明

| 属性 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| matchEntireCell | boolean | 否 | 匹配整个单元格。 |
| matchCase | boolean | 否 | 匹配大小写。 |
| useRegExp | boolean | 否 | 使用正则表达式。 |
| matchFormulaText | boolean | 否 | 在公式内搜索。 |
