---
title: "获取微应用免登授权码"
source_url: "https://open.dingtalk.com/document/development/obtain-the-micro-application-exemption-authorization-code"
namespace: "development"
slug: "obtain-the-micro-application-exemption-authorization-code"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 免登 > 获取微应用免登授权码"
doc_id: "AyQJgBY68Y"
updated_at: "2025-09-17 20:56:01"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-micro-application-exemption-authorization-code
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 免登 > 获取微应用免登授权码
> Updated: 2025-09-17 20:56:01

# 获取微应用免登授权码

调用**runtime.permission.requestAuthCode**获取微应用免登授权码。

> **[!IMPORTANT]**
>
> 为提升接口的使用安全性，我们对本接口进行了升级，具体说明如下：
>
> - 如果未使用本接口，我们建议您使用推荐的 [requestAuthCode](https://open.dingtalk.com/document/orgapp/jsapi-request-auth-code) 接口。
> - 如果已使用本接口，建议您根据自身的实际情况，评估是否切换至推荐的接口。
>
> 感谢您的理解与支持！

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=runtime.permission.requestAuthCode)在线调试该接口。

## 使用说明

调用本接口前，请先引入钉钉js，参考[准备工作](https://open.dingtalk.com/document/orgapp/read-before-development)。

| **客户端** | **是否需要鉴权** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- | --- |
| 支持说明 | 不需要 | 支持 | 支持 | 支持 |

```
dd.runtime.permission.requestAuthCode({
    corpId: "corpid",
    onSuccess: function(result) {
    /*{
        code: 'hYLK98jkf0m' //string authCode
    }*/
    },
    onFail : function(err) {}
 
})
```

## 参数说明

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| corpId | String | 是 | 企业的corpId。  **[!NOTE]**  第三方企业应用可以在微应用的首页URL中使用**$CORPID$**做为参数占位符，钉钉容器会将**$CORPID$**替换为当前访问用户的企业corpId。例如：https://www.dingtalk.com?corpId=$CORPID$。 |

## 返回结果

| **参数** | **说明** |
| --- | --- |
| code | 授权码，有效期5分钟，且只能使用一次，使用后会失效。 |

## **错误码**

| errorCode | **errorMessage** | **说明** |
| --- | --- | --- |
| 3 | 对应企业没有xxxx域名微应用 | 根据传入的corpId没有查到使用当前页面域名的微应用。 |
