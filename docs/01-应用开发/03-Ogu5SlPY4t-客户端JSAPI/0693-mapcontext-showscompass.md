---
title: "设置指南针是否可见(showsCompass)"
source_url: "https://open.dingtalk.com/document/development/mapcontext-showscompass"
namespace: "development"
slug: "mapcontext-showscompass"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 地图 > MapContext > 设置指南针是否可见(showsCompass)"
doc_id: "iJdWuvpVlt"
updated_at: "2025-09-17 21:00:43"
---

> Source: https://open.dingtalk.com/document/development/mapcontext-showscompass
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 地图 > MapContext > 设置指南针是否可见(showsCompass)
> Updated: 2025-09-17 21:00:43

# 设置指南针是否可见(showsCompass)

使用**MapContext.showsCompass**设置指南针是否可见。

## **示例代码**

```
this.mapCtx = dd.createMapContext('map');
this.mapCtx.showsCompass({isShowsCompass:1});
```

## **入参**

Object 类型，属性如下：

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| isShowsCompass | Enum | 是 | 指南针是否可用。   - **1** ：表示可见 - **0**：表示不可见 |

## **兼容性**

使用 **dd.canIUse('createMapContext')**进行可用性判断。
