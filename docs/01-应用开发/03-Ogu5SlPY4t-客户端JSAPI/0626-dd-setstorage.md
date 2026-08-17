---
title: "将数据存储在本地缓存"
source_url: "https://open.dingtalk.com/document/development/dd-setstorage"
namespace: "development"
slug: "dd-setstorage"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 缓存 > 将数据存储在本地缓存"
doc_id: "U4uW0vgxQN"
updated_at: "2025-09-17 20:59:59"
---

> Source: https://open.dingtalk.com/document/development/dd-setstorage
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 缓存 > 将数据存储在本地缓存
> Updated: 2025-09-17 20:59:59

# 将数据存储在本地缓存

调用dd.setStorage将数据存储在本地缓存中指定的 key 中，会覆盖掉原来该 key 对应的数据。

> **[!NOTE]**
>
> 单条数据转换成字符串后，字符串长度最大200\*1024。同一个钉钉用户，同一个小程序缓存总上限为10MB。

## **示例****代码**

```
dd.setStorage({
  key: 'currentCity',
  data: {
    cityName: '杭州',
    adCode: '330100',
    spell: ' hangzhou',
  },
  success: function() {
    dd.alert({content: '写入成功'});
  }
});
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| key | String | 是 | 缓存数据的key。 |
| data | Object/String | 是 | 要缓存的数据。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |
