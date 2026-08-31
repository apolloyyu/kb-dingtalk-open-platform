---
title: "SetValueOptions"
source_url: "https://open.dingtalk.com/document/development/setvalueoptions"
namespace: "development"
slug: "setvalueoptions"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "酷应用 > 文档酷应用 > API参考文档 > SetValueOptions"
doc_id: "VraSXCyFXb"
updated_at: "2025-08-27 18:09:31"
---

> Source: https://open.dingtalk.com/document/development/setvalueoptions
> Path: 应用开发 / 客户端 JSAPI / 酷应用 > 文档酷应用 > API参考文档 > SetValueOptions
> Updated: 2025-08-27 18:09:31

# SetValueOptions

## API描述

设置值的选项。用于 Range.setValue()或者Range.setValues() API中指定设置值时的选项。

## 属性说明

| 属性 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| parseType | String | 是 | 值的解析类型。   - **raw**：表示设置值的时候不解析。 - **useEntered**：表示策略和用户输入一致，例如输入 100%，会被解析成值为1，数字格式为%。 |
