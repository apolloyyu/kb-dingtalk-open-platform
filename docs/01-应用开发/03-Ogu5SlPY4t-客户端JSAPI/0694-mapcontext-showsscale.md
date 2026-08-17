---
title: "设置比例尺控件是否可见(showsScale)"
source_url: "https://open.dingtalk.com/document/development/mapcontext-showsscale"
namespace: "development"
slug: "mapcontext-showsscale"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 地图 > MapContext > 设置比例尺控件是否可见(showsScale)"
doc_id: "seN4WDlhAP"
updated_at: "2025-09-17 21:00:43"
---

> Source: https://open.dingtalk.com/document/development/mapcontext-showsscale
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 地图 > MapContext > 设置比例尺控件是否可见(showsScale)
> Updated: 2025-09-17 21:00:43

# 设置比例尺控件是否可见(showsScale)

使用**MapContext.showsScale**设置比例尺控件是否可见。

## 简介

## **示例代码**

```
this.mapCtx = dd.createMapContext('map');
this.mapCtx.showsScale({isShowsScale:1});
```

## **入参**

Object 类型，属性如下：

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| isShowsScale | Enum | 是 | 手势是否可用。   - **1**：表示可见 - **0**：表示不可见 |

## **兼容性**

使用 **dd.canIUse('createMapContext.return.showRoute')** 进行可用性判断。
