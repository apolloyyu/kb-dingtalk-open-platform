---
title: "同步将数据存储"
source_url: "https://open.dingtalk.com/document/development/dd-setstoragesync"
namespace: "development"
slug: "dd-setstoragesync"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 缓存 > 同步将数据存储"
doc_id: "lPXgiNPG16"
updated_at: "2025-09-17 21:00:00"
---

> Source: https://open.dingtalk.com/document/development/dd-setstoragesync
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 缓存 > 同步将数据存储
> Updated: 2025-09-17 21:00:00

# 同步将数据存储

调用dd.setStorageSync同步将数据存储在本地缓存中指定的 key 中。

> **[!IMPORTANT]**
>
> 同步数据IO操作可能会影响小程序流畅度，建议使用异步接口，或谨慎处理调用异常。

## **示例****代码**

```
dd.setStorageSync({
  key: 'currentCity',
  data: {
    cityName: '杭州',
    adCode: '330100',
    spell: ' hangzhou',
  }
});
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| key | String | 是 | 缓存数据的key。 |
| data | Object/String | 是 | 要缓存的数据。 |
