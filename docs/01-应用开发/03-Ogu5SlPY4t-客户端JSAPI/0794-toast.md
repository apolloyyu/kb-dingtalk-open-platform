---
title: "toast"
source_url: "https://open.dingtalk.com/document/development/toast"
namespace: "development"
slug: "toast"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > toast"
doc_id: "uJXTLPDCK1"
updated_at: "2025-09-17 20:56:29"
---

> Source: https://open.dingtalk.com/document/development/toast
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > toast
> Updated: 2025-09-17 20:56:29

# toast

调用**device.notification.toast**实现toast弹窗。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.notification.toast)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 支持(参数不同，icon) |

```
dd.device.notification.toast({
    icon: '', //icon样式，不同客户端参数不同，请参考参数说明
    text: String, //提示信息
    duration: Number, //显示持续时间，单位秒，默认按系统规范[android只有两种(<=2s >2s)]
    delay: Number, //延迟显示，单位秒，默认0
    onSuccess : function(result) {
        /*{}*/
    },
    onFail : function(err) {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| icon | String | icon样式，不同客户端参数不同：   - Android和iOS样式：success和error，默认为空 - PC端样式：alert，success，error，warning，information，confirm，默认information |
| text | String | 必填，提示信息。 |
| duration | Number | 显示持续时间，单位秒，默认按系统规范。  Android只有两种(<=2s和>2s)。 |
| delay | Number | 延迟显示，单位秒，默认0。 |
