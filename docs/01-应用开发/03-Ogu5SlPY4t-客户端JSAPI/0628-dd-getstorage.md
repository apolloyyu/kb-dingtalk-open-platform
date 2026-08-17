---
title: "异步获取指定key的缓存数据"
source_url: "https://open.dingtalk.com/document/development/dd-getstorage"
namespace: "development"
slug: "dd-getstorage"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 缓存 > 异步获取指定key的缓存数据"
doc_id: "DLkwl7b5iY"
updated_at: "2025-09-17 21:00:00"
---

> Source: https://open.dingtalk.com/document/development/dd-getstorage
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 缓存 > 异步获取指定key的缓存数据
> Updated: 2025-09-17 21:00:00

# 异步获取指定key的缓存数据

调用**dd.getStorage**获取缓存数据，可以获取指定key的单条缓存数据。

## **示例代码**

```
dd.getStorage({
  key: 'currentCity',
  success: function(res) {
    dd.alert({content: '获取成功：' + res.data.cityName});
  },
  fail: function(res){
    dd.alert({content: res.errorMessage});
  }
});
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| key | String | 是 | 缓存数据的key。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success返回值**

| **名称** | **类型** | **说明** |
| --- | --- | --- |
| data | Object/String | key对应的内容，不存在时返回 null。 |
