---
title: "获取jsapi_ticket"
source_url: "https://open.dingtalk.com/document/development/obtain-jsapi-ticket"
namespace: "development"
slug: "obtain-jsapi-ticket"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 获取访问凭证 > 获取jsapi_ticket"
doc_id: "Qh8agr9w1x"
updated_at: "2025-09-08 19:07:41"
---

> Source: https://open.dingtalk.com/document/development/obtain-jsapi-ticket
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 获取访问凭证 > 获取jsapi_ticket
> Updated: 2025-09-08 19:07:41

# 获取jsapi\_ticket

当开发H5微应用时，需要先通过本接口获取jsapi\_ticket，然后再生成鉴权签名，最后调用dd.config完成鉴权。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对**获取访问凭证**相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于2023年8月17日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用[获取jsapiTicket](https://open.dingtalk.com/document/orgapp/create-a-jsapi-ticket)新版规范接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

> **[!NOTE]**
>
> 企业内部应用是以应用维度获取jsapi\_ticket的，所以在使用的时候需要将jsapi\_ticket以appKey为维度进行缓存下来（设置缓存过期时间2小时），并不需要每次都通过接口拉取。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 默认开通，无需申请 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=dingtalk.oapi.get_jsapi_ticket) |
| 第三方企业应用 | 是 | 默认开通，无需申请 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=dingtalk.oapi.get_jsapi_ticket) |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/get_jsapi_ticket`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6adfxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 - 第三方企业应用，通过[获取第三方企业应用的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| expires\_in | Number | 7200 | ticket过期时间，单位秒。 |
| ticket | String | dWk81eLxxxx | 生成的临时jsapi\_ticket。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/get_jsapi_ticket?access_token=ACCESS_TOKEN
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/get_jsapi_ticket");
OapiGetJsapiTicketRequest req = new OapiGetJsapiTicketRequest();
req.setHttpMethod("GET");
OapiGetJsapiTicketResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "errcode":0,
        "ticket":"dWk8xxxx",
        "errmsg":"ok",
        "expires_in":7200
}
```

## 错误排查

当调用该接口返回`访问IP不在白名单`的错误，请按照以下方式排查：

```
{
  "errcode":60020,
  "errmsg":"请参考FAQ：https://open-doc.dingtalk.com/microapp/faquestions/cvbtph。错误原因：访问ip不在白名单之中,request ip=203.119.196.81 appKey(dingeqqpkv3artfbxxx)"
}
```

1. 对比接口调用使用的AppKey与报错信息中返回的AppKey值是否一致。

   - 如果不一致，可能是AppKey或者AppSecret使用的是其他应用的access\_token，导致在获取access\_token值时会提示错误。
   - 如果一致，将报错信息中的request IP添加到该应用的出口IP。

     ![p144065](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1063180261/p256874.png)
2. 如果错误信息中返回的是CorpId，创建应用时间较早，参考以下操作添加出口IP：

   1. 使用企业管理员账号登录[钉钉开发者后台](https://open-dev.dingtalk.com/#/testManage)，单击**基本信息**页签，然后单击**开发信息旧版**。找到该应用使用的CorpSecret。
   2. 点击设置修改IP。
