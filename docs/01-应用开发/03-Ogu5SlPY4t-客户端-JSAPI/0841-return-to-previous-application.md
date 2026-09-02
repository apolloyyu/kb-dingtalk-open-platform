---
title: "返回上一个应用"
source_url: "https://open.dingtalk.com/document/development/return-to-previous-application"
namespace: "development"
slug: "return-to-previous-application"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 打开应用 > 返回上一个应用"
doc_id: "3qUXDt5CzE"
updated_at: "2026-09-02 18:14:20"
---

> Source: https://open.dingtalk.com/document/development/return-to-previous-application
> Path: 应用开发 / 客户端 JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 打开应用 > 返回上一个应用
> Updated: 2026-09-02 18:14:20

# 返回上一个应用

调用**biz.navigation.navigateBackPage**，返回上一个应用。

> **[!NOTE]**
>
> 在调用[跳转H5微应用](0840-jump-to-h5-micro-application.md)接口后，可以从目标H5微应用内调用本接口返回。

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** | 是否需要鉴权 |
| --- | --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥6.5.45) | 支持(钉钉版本≥6.5.45) | 不支持 | 不需要 |

```
dd.biz.navigation.navigateBackPage({
  extraData:{
    "a":"b"
  },
  onSucess:(res) => {
    console.log(JSON.stringify(res))
  },
  onFail:(err) =>{
    console.log(JSON.stringify(err))
  }
})
```

## **参数说明**

| 参数 | 类型 | 是否必传 | 说明 |
| --- | --- | --- | --- |
| extraData | Object | 否 | 返回上一个应用携带的参数，返回的目标H5微应用可在[页面resume事件的回调监听](../01-XOnnmGCTbn-开发指南/0042-webapp-page-event-monitoring.md#section-8jy-gd1-cug)中获取携带的参数。 |
| onSuccess | Function | 否 | 调用成功的回调函数。 |
| onFail | Function | 否 | 调用失败的回调函数。 |

## **返回结果**

> **[!NOTE]**
>
> 本接口调用后，无返回参数。
