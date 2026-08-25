---
title: "激活应用"
source_url: "https://open.dingtalk.com/document/development/activate-suite"
namespace: "development"
slug: "activate-suite"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 回调接口 > 激活应用"
doc_id: "cFUFmjZjB5"
updated_at: "2025-10-16 14:31:40"
---

> Source: https://open.dingtalk.com/document/development/activate-suite
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 回调接口 > 激活应用
> Updated: 2025-10-16 14:31:40

# 激活应用

在收到HTTP回调推送的企业授权开通应用事件后，调用本接口激活企业授权的应用。

> **[!IMPORTANT]**
>
> 本接口适用于第三方企业应用配置HTTP回调方式时，当授权企业开通该应用，调用本接口激活授权企业应用。由于第三方企业应用的HTTP回调方式已不再支持，推荐使用[RDS推送](https://open.dingtalk.com/document/isvapp/configure-rds-push-table)和[SyncHTTP推送](https://open.dingtalk.com/document/isvapp/configure-synchttp-push)，本接口文档移动到历史文档中。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保对应用已经添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 否 | — | — |
| 第三方企业应用 | 是 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/service/activate_suite`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| suite\_access\_token | String | 是 | 68fbxxxx | 第三方应用的suite\_access\_token，可调用[服务商获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| suite\_key | String | 是 | suitexxxx | 第三方应用的SuiteKey。  可在[钉钉开发者后台](https://open-dev.dingtalk.com/#/index)的第三方应用详情页面获取。 |
| auth\_corpid | String | 是 | ding1234 | 授权企业的CorpId。  HTTP回调事件中推送的CorpId。 |
| permanent\_code | Sting | 是 | xxxx | 授权企业的永久授权码。  通过[获取授权企业的永久授权码](https://open.dingtalk.com/document/isvapp/obtain-a-permanent-authorization-code)接口获取。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/service/activate_suite?suite_access_token=SUITE_ACCESS_TOKEN
```

请求正文

```
{
        "auth_corpid":"ding1234",
        "suite_key":"suitexxxx",
        "permanent_code":"xxxx"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client= new DefaultDingTalkClient("https://oapi.dingtalk.com/service/activate_suite?suite_access_token=SUITE_ACCESS_TOKEN");
OapiServiceActivateSuiteRequest req= new OapiServiceActivateSuiteRequest();
req.setSuiteKey("suitexxxx");
req.setAuthCorpid("ding1234");
req.setPermanentCode("xxxx");
OapiServiceActivateSuiteResponse rsp= client.execute(req);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "errcode":0,
        "errmsg":"ok"
}
```
