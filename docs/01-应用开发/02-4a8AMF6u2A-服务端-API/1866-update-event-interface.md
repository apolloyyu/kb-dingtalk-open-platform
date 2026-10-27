---
title: "更新事件接口"
source_url: "https://open.dingtalk.com/document/development/update-event-interface"
namespace: "development"
slug: "update-event-interface"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 回调接口 > 更新事件接口"
doc_id: "n90VN6HXSf"
updated_at: "2026-09-02 18:13:40"
---

> Source: https://open.dingtalk.com/document/development/update-event-interface
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 回调接口 > 更新事件接口
> Updated: 2026-09-02 18:13:40

# 更新事件接口

调用本接口更新已经注册的回调事件，即更新订阅事件。

> **[!IMPORTANT]**
>
> 本接口后续将维持现有功能且不再新增能力，已接入用户不受影响。

## 权限

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/call_back/update_call_back`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| call\_back\_tag | String[] | 是 | ["user\_add\_org", "user\_leave\_org"] | 需要监听的事件类型，可通过[查询订阅事件](1867-query-subscribed-events.md)接口获取。 |
| token | String | 是 | dingtalk | 加解密需要用到的token，可以随机填写，长度大于等于6个字符且少于64个字符。 |
| aes\_key | String | 是 | hvnzd2y8jkhx8yoo4483xxxx | 数据加密密钥。用于回调数据的加密，长度固定为43个字符，从a-z, A-Z, 0-9共62个字符中选取,您可以随机生成，ISV(服务提供商)推荐使用注册套件时填写的EncodingAESKey。 |
| url | String | 是 | www.dingtalk.com | 接收事件回调的url，必须是公网可以访问的url地址。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/call_back/update_call_back?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "aes_key": "hvnzd2y8jkhx8yoo4483xxxx", 
  "call_back_tag": [
    "user_add_org", 
    "user_modify_org", 
    "user_leave_org"
  ], 
  "url": "www.dingtalk.com", 
  "token": "dingtalk"
}
```

**请求示例（JAVA SDK）**

```
 DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/call_back/update_call_back");
 OapiCallBackUpdateCallBackRequest req = new OapiCallBackUpdateCallBackRequest();
 req.setCallBackTag(Arrays.asList("user_add_org","user_modify_org","user_leave_org"));
 req.setAesKey("123");
 req.setToken("123");
 req.setUrl("www.dingtalk.com");
 OapiCallBackUpdateCallBackResponse rsp = client.execute(req, access_token);
 System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode":0,
  "errmsg":"ok"
}
```
