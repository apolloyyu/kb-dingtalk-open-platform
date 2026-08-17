---
title: "同步获取指定key的缓存数据"
source_url: "https://open.dingtalk.com/document/development/dd-getstoragesync"
namespace: "development"
slug: "dd-getstoragesync"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 缓存 > 同步获取指定key的缓存数据"
doc_id: "IlaL6Me5gg"
updated_at: "2025-09-17 21:00:01"
---

> Source: https://open.dingtalk.com/document/development/dd-getstoragesync
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 缓存 > 同步获取指定key的缓存数据
> Updated: 2025-09-17 21:00:01

# 同步获取指定key的缓存数据

调用**dd.getStorageSync**同步获取缓存数据。

> **[!IMPORTANT]**
>
> 同步数据IO操作可能会影响小程序流畅度，建议使用异步接口，或谨慎处理调用异常。

## **示例****代码**

```
 let res = dd.getStorageSync({ key: 'currentCity' });
 dd.alert({
    content: JSON.stringify(res.data),
 });
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| key | String | 是 | 缓存数据的key。 |

## **返回值**

| **名称** | **类型** | **说明** |
| --- | --- | --- |
| data | Object/String | key对应的内容，不存在时返回 null。 |
