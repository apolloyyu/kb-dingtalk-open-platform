---
title: "获取小程序的运行版本"
source_url: "https://open.dingtalk.com/document/development/obtain-the-running-version-of-the-mini-program"
namespace: "development"
slug: "obtain-the-running-version-of-the-mini-program"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础 API > 获取小程序的运行版本"
doc_id: "M914rQoVDg"
updated_at: "2025-09-17 20:58:44"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-running-version-of-the-mini-program
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础 API > 获取小程序的运行版本
> Updated: 2025-09-17 20:58:44

# 获取小程序的运行版本

使用dd.getRunScene获取当前小程序的运行版本，小程序版本说明请查看[版本管理与发布](https://open.dingtalk.com/document/orgapp/publish-orgapp)。

## 扫码体验

![getRunScene](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0156276461/p412407.png)

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

> **[!NOTE]**
>
> - 开发者可以通过[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)函数判断端上是否支持此能力。
> - IDE真机调试时暂不支持触发该API，请使用IDE的预览调试。

## 示例代码

```
dd.getRunScene({
  success(result) {
     dd.alert({
      title: '小程序版本',
      content:`${result.envVersion}`
    });
  },
})
```

## 入参说明

| 属性 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

### success返回值

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| envVersion | String | 小程序当前运行的版本，小程序版本说明请查看[版本管理与发布](https://open.dingtalk.com/document/orgapp/publish-orgapp)。   - **debug**：开发版。 - **trial**：体验版。 - **release**：线上版。 |

### fail返回值

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| error | String | 错误码。 |
| errorMessage | String | 错误信息。 |

## 错误码

| 错误码 | 描述 |
| --- | --- |
| 3 | 发生未知错误。 |
