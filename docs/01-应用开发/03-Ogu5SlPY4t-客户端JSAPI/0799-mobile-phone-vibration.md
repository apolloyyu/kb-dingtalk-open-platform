---
title: "手机震动"
source_url: "https://open.dingtalk.com/document/development/mobile-phone-vibration"
namespace: "development"
slug: "mobile-phone-vibration"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > 手机震动"
doc_id: "M6jJWRNOre"
updated_at: "2025-09-17 20:56:32"
---

> Source: https://open.dingtalk.com/document/development/mobile-phone-vibration
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > 手机震动
> Updated: 2025-09-17 20:56:32

# 手机震动

调用**device.notification.vibrate**实现手机震动。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.notification.vibrate)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
    dd.device.notification.vibrate({
    duration: 300, //震动时间，android可配置 iOS忽略
    onSuccess : function(result) {
        /*
        {}
        */
    },
    onFail : function(err) {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| duration | Number | 震动时间，仅支持Android端配置。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| buttonIndex | 被点击按钮的索引值，Number类型，从0开始。 |
| value | 输入的值。 |
