---
title: "获取授权企业的永久授权码"
source_url: "https://open.dingtalk.com/document/development/obtain-a-permanent-authorization-code"
namespace: "development"
slug: "obtain-a-permanent-authorization-code"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 回调接口 > 获取授权企业的永久授权码"
doc_id: "XfnKVn0J3W"
updated_at: "2025-10-16 14:31:41"
---

> Source: https://open.dingtalk.com/document/development/obtain-a-permanent-authorization-code
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 回调接口 > 获取授权企业的永久授权码
> Updated: 2025-10-16 14:31:41

# 获取授权企业的永久授权码

调用本接口获取企业的永久授权码。

> **[!IMPORTANT]**
>
> 本接口适用于第三方企业应用配置HTTP回调方式时，当授权企业开通该应用，调用本接口获取授权企业的永久授权码。由于第三方企业应用的HTTP回调方式已不再支持，推荐使用[RDS推送](https://open.dingtalk.com/document/isvapp/configure-rds-push-table)和[SyncHTTP推送](https://open.dingtalk.com/document/isvapp/configure-synchttp-push)，本接口文档移动到历史文档中。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保对应用已经添加了接口权限。

| 应用类型 | 是否可调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 否 | — | — |
| 第三方企业应用 | 是 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/service/get_permanent_code`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| suite\_access\_token | String | 是 | 6ed1bxxxx | 第三方企业应用的access\_token，可调用[获取第三方企业应用的suite\_access\_token](https://open.dingtalk.com/document/isvapp/obtain-application-suite-ticket)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| tmp\_auth\_code | String | 是 | xxxx | 回调接口（tmp\_auth\_code）获取的临时授权码。  **[!NOTE]**  临时授权码只能使用一次。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| auth\_corp\_info | AuthCorpInfo |  | 授权方企业信息。 |
| corpid | String | ding1234 | 授权方企业CorpId。 |
| corp\_name | String | 钉钉 | 授权方企业名称。 |
| permanent\_code | String | xxxx | 永久授权码。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/service/get_permanent_code?suite_access_token=SUITE_ACCESS_TOKEN
```

请求正文

```
{
        "tmp_auth_code":"xxxx"
}
```

**请求示例（JAVA SDK）**

```
   DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/service/get_permanent_code?suite_access_token=SUITE_ACCESS_TOKEN");
   OapiServiceGetPermanentCodeRequest req = new OapiServiceGetPermanentCodeRequest();
   req.setTmpAuthCode("xxxx");
   OapiServiceGetPermanentCodeResponse rsp = client.execute(req);
   System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "errcode":0,
        "auth_corp_info":{
                "corpid":"xxxxx",
                "corp_name":"name"
        },
        "errmsg":"ok",
        "permanent_code":"xxxx"
}
```
