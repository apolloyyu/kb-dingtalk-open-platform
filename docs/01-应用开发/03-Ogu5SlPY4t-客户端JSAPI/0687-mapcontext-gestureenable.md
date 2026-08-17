---
title: "设置所有手势是否可用(gestureEnable)"
source_url: "https://open.dingtalk.com/document/development/mapcontext-gestureenable"
namespace: "development"
slug: "mapcontext-gestureenable"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 地图 > MapContext > 设置所有手势是否可用(gestureEnable)"
doc_id: "AtfIUY4nAU"
updated_at: "2025-09-17 21:00:40"
---

> Source: https://open.dingtalk.com/document/development/mapcontext-gestureenable
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 地图 > MapContext > 设置所有手势是否可用(gestureEnable)
> Updated: 2025-09-17 21:00:40

# 设置所有手势是否可用(gestureEnable)

使用**MapContext.gestureEnable**设置所有手势是否可用。

## **示例代码**

```
this.mapCtx = dd.createMapContext('map');
this.mapCtx.gestureEnable({isGestureEnable:1});
```

## **入参说明**

Object 类型，属性如下：

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| isGestureEnable | Number | 是 | 指定手势是否可用。   - **1**：表示可用 - **0**：表述不可用 |

## **兼容性**

使用 **dd.canIUse('createMapContext')**进行可用性判断。
