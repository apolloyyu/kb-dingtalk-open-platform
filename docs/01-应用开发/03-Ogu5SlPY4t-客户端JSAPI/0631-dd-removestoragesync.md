---
title: "同步删除指定key的缓存数据"
source_url: "https://open.dingtalk.com/document/development/dd-removestoragesync"
namespace: "development"
slug: "dd-removestoragesync"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 缓存 > 同步删除指定key的缓存数据"
doc_id: "0ApmmgD7fh"
updated_at: "2025-09-17 21:00:02"
---

> Source: https://open.dingtalk.com/document/development/dd-removestoragesync
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 缓存 > 同步删除指定key的缓存数据
> Updated: 2025-09-17 21:00:02

# 同步删除指定key的缓存数据

调用**dd.removeStorageSync**同步删除缓存数据。

> **[!IMPORTANT]**
>
> 同步数据IO操作可能会影响小程序流畅度，建议使用异步接口，或谨慎处理调用异常。

## **示例代码**

```
dd.removeStorageSync({
  key: 'currentCity',
});
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| key | String | 是 | 缓存数据的key。 |
