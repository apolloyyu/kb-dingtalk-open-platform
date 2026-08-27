---
title: "获取微应用后台免登的access_token"
source_url: "https://open.dingtalk.com/document/development/obtain-the-ssotoken-for-micro-application-background-logon-free"
namespace: "development"
slug: "obtain-the-ssotoken-for-micro-application-background-logon-free"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 获取访问凭证 > 获取微应用后台免登的access_token"
doc_id: "Sjl74e7iGA"
updated_at: "2026-08-25 09:36:33"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-ssotoken-for-micro-application-background-logon-free
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 获取访问凭证 > 获取微应用后台免登的access_token
> Updated: 2026-08-25 09:36:33

# 获取微应用后台免登的access\_token

调用本接口获取微应用后台免登的access\_token。获取的access\_token即ssotoken只在应用管理后台免登场景中使用。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版 [获取微应用后台免登的accessToken](0025-obtain-the-access-token-of-the-micro-application-background-without-log-on.md)接口，已接入用户不受影响。

> **[!NOTE]**
>
> ISV开发的应用后台免登用的access\_token，需使用ISV自己的corpId和SSOsecret来换取，不是管理员所在的企业的。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保对应用已经添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 默认开通，无需申请 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=dingtalk.oapi.sso.gettoken) |
| 第三方企业应用 | 支持 | 默认开通，无需申请 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=dingtalk.oapi.sso.gettoken) |
| 第三方个人应用 | 暂不支持 | — | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/sso/gettoken`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| corpid | String | 是 | ding1234 | 企业的corpid。 |
| corpsecret | String | 是 | 2pyNWs4LV8Ge2Mxxxx | 可以在[钉钉开发者后台](https://open-dev.dingtalk.com/fe/old#/corpAuthInfo)的**基本信息 > 开发信息（旧版**）页面获取**微应用管理后台SSOSecret**。  如下图所示：SSO获取途径 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| access\_token | String | 674xxxx6356 | 获取到的凭证。 |
| errmsg | String | ok | 错误信息。 |
| errcode | Number | 0 | 错误码。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/sso/gettoken?corpid=ding1234&corpsecret=12345
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/sso/gettoken");
OapiSsoGettokenRequest req = new OapiSsoGettokenRequest();
req.setCorpid("ding1234");
req.setCorpsecret("2pyNWs4LV8Ge2Mxxxx");
req.setHttpMethod("GET");
OapiSsoGettokenResponse rsp = client.execute(req);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "access_token":"67477fed82e63563a320xxxx",
        "errcode":0,
        "errmsg":"ok"
}
```

## 相关文档

- [应用管理后台免登](0022-log-on-site-application-management-backend.md)
