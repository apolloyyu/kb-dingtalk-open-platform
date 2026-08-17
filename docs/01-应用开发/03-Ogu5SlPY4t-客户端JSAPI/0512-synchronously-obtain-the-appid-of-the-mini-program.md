---
title: "同步获取小程序AppId"
source_url: "https://open.dingtalk.com/document/development/synchronously-obtain-the-appid-of-the-mini-program"
namespace: "development"
slug: "synchronously-obtain-the-appid-of-the-mini-program"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础 API > 同步获取小程序AppId"
doc_id: "VldluOX1HD"
updated_at: "2025-09-17 20:58:43"
---

> Source: https://open.dingtalk.com/document/development/synchronously-obtain-the-appid-of-the-mini-program
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础 API > 同步获取小程序AppId
> Updated: 2025-09-17 20:58:43

# 同步获取小程序AppId

调用**dd.getAppIdSync**同步获取小程序的AppId，即MiniAppId。

## 扫码体验

![扫码体验](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2915715461/p406823.png)

> **[!NOTE]**
>
> 开发者可以通过**dd.canIUse**函数判断端上是否支持此能力。

## 示例代码

```
const appIdRes = dd.getAppIdSync();
console.log(appIdRes.appId);
```

## 返回值

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| appId | String | 当前小程序的AppId，即MiniAppId。 |
