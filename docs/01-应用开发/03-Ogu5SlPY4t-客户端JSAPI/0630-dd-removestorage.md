---
title: "删除缓存数据"
source_url: "https://open.dingtalk.com/document/development/dd-removestorage"
namespace: "development"
slug: "dd-removestorage"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 缓存 > 删除缓存数据"
doc_id: "MVLdAAHuDD"
updated_at: "2025-09-17 21:00:01"
---

> Source: https://open.dingtalk.com/document/development/dd-removestorage
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 缓存 > 删除缓存数据
> Updated: 2025-09-17 21:00:01

# 删除缓存数据

调用**dd.removeStorage**删除缓存数据。

## **示例****代码**

```
dd.removeStorage({
  key: 'currentCity',
  success: function(){
    dd.alert({content: '删除成功'});
  }
});
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| key | String | 是 | 缓存数据的key。 |
| success | Function | 否 | 调用成功的回调函数 |
| fail | Function | 否 | 调用失败的回调函数 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |
