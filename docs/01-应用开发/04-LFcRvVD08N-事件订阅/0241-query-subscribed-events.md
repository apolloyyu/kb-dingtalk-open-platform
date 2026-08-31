---
title: "查询订阅事件"
source_url: "https://open.dingtalk.com/document/development/query-subscribed-events"
namespace: "development"
slug: "query-subscribed-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 回调接口 > 查询订阅事件"
doc_id: "WZuvgJNBrK"
updated_at: "2025-10-16 14:31:39"
---

> Source: https://open.dingtalk.com/document/development/query-subscribed-events
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 回调接口 > 查询订阅事件
> Updated: 2025-10-16 14:31:39

# 查询订阅事件

调用本接口查询已经注册的回调事件，即订阅事件。

## 权限

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 无需申请 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=dingtalk.oapi.call_back.get_call_back) |
| 第三方企业应用 | 是 | 无需申请 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=dingtalk.oapi.call_back.get_call_back) |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/call_back/get_call_back`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 - 第三方企业应用可通过[获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| url | String | www.dingtalk.com | 接收事件回调的url。 |
| aes\_key | String | hvnzd2y8jkhx8yoo4483xxxx | 数据加密密钥。 |
| token | String | dingtalk | 加解密需要用到的token，可以随机填写，长度大于等于6个字符且少于64个字符。 |
| call\_back\_tag | String[] | ["user\_add\_org","user\_leave\_org"] | 需要监听的事件类型。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/call_back/get_call_back?access_token=ACCESS_TOKEN
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/call_back/get_call_back");
OapiCallBackGetCallBackRequest req = new OapiCallBackGetCallBackRequest();
req.setHttpMethod("GET");
OapiCallBackGetCallBackResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "errcode":0,
        "call_back_tag":["user_add_org","user_leave_org"],
        "aes_key":"hvnzd2y8jkhx8yoo4483xxxx",
        "errmsg":"ok",
        "url":"www.dingtalk.com",
        "token":"dingtalk"
}
```
