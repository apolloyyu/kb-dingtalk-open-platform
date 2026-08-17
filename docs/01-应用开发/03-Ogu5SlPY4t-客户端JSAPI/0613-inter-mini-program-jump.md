---
title: "跳转到另一个钉钉小程序"
source_url: "https://open.dingtalk.com/document/development/inter-mini-program-jump"
namespace: "development"
slug: "inter-mini-program-jump"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 小程序跳转 > 跳转到另一个钉钉小程序"
doc_id: "JXP8ten6BK"
updated_at: "2025-09-17 20:59:49"
---

> Source: https://open.dingtalk.com/document/development/inter-mini-program-jump
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 小程序跳转 > 跳转到另一个钉钉小程序
> Updated: 2025-09-17 20:59:49

# 跳转到另一个钉钉小程序

调用**dd.navigateToMiniProgram**跳转到其他钉钉小程序。

> **[!NOTE]**
>
> 跳转到另一个钉钉小程序的最新线上版。

## **扫码体验**

![qrcode](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5304444661/p497641.png)

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥5.1.39) | 支持(钉钉版本≥5.1.39) | 不支持 |

## **示例代码**

```
dd.navigateToMiniProgram({
  appId: 'xxxx',
  path: '/pages/index/index',
  extraData:{
    "data1":"test"
  },
  success: (res) => {
    console.log(JSON.stringify(res))
  },
  fail: (res) => {
    console.log(JSON.stringify(res))
  }
});
```

## **入参说明**

| **属性** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| appId | String | 是 | 要跳转的目标小程序miniAppId，请参考[基础概念-MiniAppId](https://open.dingtalk.com/document/orgapp/basic-concepts)。  **[!NOTE]**  如果该参数值错误，会跳转到加载失败页面。 |
| path | String | 否 | 打开目标小程序的页面路径。如果为空，则打开首页。 |
| extraData | Object | 否 | 需要传递给目标小程序的数据，为键值对的格式，数值的类型为字符串。  目标小程序可在 App.onLaunch()或 App.onShow()方法中获取到这份数据。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

## **返回结果**

> **[!NOTE]**
>
> - 本接口调用成功后，无返回参数。调用本接口跳转页面失败后，暂无失败回调信息。
> - 当跳转后出现加载失败时，该接口不会触发onFail回调，需要检查appId参数是否正确。
