---
title: "返回上一个钉钉小程序"
source_url: "https://open.dingtalk.com/document/development/return-to-the-previous-dingtalk-mini-program"
namespace: "development"
slug: "return-to-the-previous-dingtalk-mini-program"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 小程序跳转 > 返回上一个钉钉小程序"
doc_id: "n2ey1CGRy2"
updated_at: "2025-09-17 20:59:50"
---

> Source: https://open.dingtalk.com/document/development/return-to-the-previous-dingtalk-mini-program
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 小程序跳转 > 返回上一个钉钉小程序
> Updated: 2025-09-17 20:59:50

# 返回上一个钉钉小程序

调用**dd.navigateBackMiniProgram**返回到上一个钉钉小程序。

> **[!NOTE]**
>
> 只有使用[跳转到另一个钉钉小程序](https://open.dingtalk.com/document/orgapp/inter-mini-program-jump)方法跳转的目标小程序，才可以调用本接口返回上一个小程序。

## **扫码体验**

![qrcode](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7404444661/p497642.png)

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥5.1.39) | 支持(钉钉版本≥5.1.39) | 不支持 |

## **示例代码**

```
dd.navigateBackMiniProgram({
	extraData:{
    "data1":"test"
  },
	success: (res) => {
  },
  fail: (res) => {
  }
});
```

## **入参说明**

| **属性** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| extraData | Object | 否 | 需要传递给目标小程序的数据，目标小程序可在App.onLaunch()或App.onShow()方法中获取到这份数据。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

## **返回结果**

> **[!IMPORTANT]**
>
> 本接口无返回值。
