---
title: "注册回调事件"
source_url: "https://open.dingtalk.com/document/development/register-callback-events"
namespace: "development"
slug: "register-callback-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 回调接口 > 注册回调事件"
doc_id: "ncsdxZAsVb"
updated_at: "2025-10-16 14:31:36"
---

> Source: https://open.dingtalk.com/document/development/register-callback-events
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 回调接口 > 注册回调事件
> Updated: 2025-10-16 14:31:36

# 注册回调事件

调用本接口注册回调事件。

如下图所示，钉钉服务器会向URL发起“**测试回调URL**”事件，来验证填写URL的合法性，URL服务器需要在接收到回调之后返回带有success的加密字符串，才能完成订阅。

> **[!IMPORTANT]**
>
> 一个应用只能注册一个接收回调的URL地址。

单击[这里](https://github.com/open-dingtalk/dingtalk-callback-Crypto)获取回调加解密类库和对应demo。

![事件订阅 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4167497061/p200499.png)

## 权限

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 无需申请 | 暂不支持 |
| 第三方企业应用 | 是 | 无需申请 | 暂不支持 |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/call_back/register_call_back`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6ed1bxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 - 第三方企业应用可通过[获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| call\_back\_tag | String[] | 是 | ["user\_add\_org", "user\_modify\_org", "user\_leave\_org"] | 注册的事件类型。 |
| token | String | 是 | dingtalk | 加解密需要用到的token，可以随机填写，长度大于等于6个字符且少于64个字符。 |
| aes\_key | String | 是 | hvnzd2y8jkhx8yoo4483xxxx | 数据加密密钥。用于回调数据的加密，长度固定为43个字符，从a-z，A-Z，0-9共62个字符中选取，您可以随机生成，ISV(服务提供商)推荐使用注册套件时填写的EncodingAESKey。 |
| url | String | 是 | www.dingtalk.com | 接收事件回调的url，必须是公网可以访问的url地址。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/call_back/register_call_back?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "call_back_tag":["user_add_org", "user_modify_org", "user_leave_org"],
        "aes_key":"hvnzd2y8jkhx8yoo4483xxxx",
        "url":"www.dingtalk.com",
        "token":"dingtalk"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/call_back/register_call_back");
OapiCallBackRegisterCallBackRequest request = new OapiCallBackRegisterCallBackRequest();
request.setUrl("http://test001.vaiwan.com/eventreceive");
request.setAesKey("hvnzd2y8jkhx8yoo4483xxxx");
request.setToken("dingtalk");
 request.setCallBackTag(Arrays.asList("user_add_org", "user_modify_org", "user_leave_org"));
OapiCallBackRegisterCallBackResponse response = client.execute(request,accessToken);
```

**返回示例**

```
{
        "errcode":0,
        "errmsg":"ok"
}
```
