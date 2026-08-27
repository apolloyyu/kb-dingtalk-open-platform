---
title: "根据unionid获取用户userid"
source_url: "https://open.dingtalk.com/document/development/you-can-call-this-operation-to-retrieve-the-userids-of"
namespace: "development"
slug: "you-can-call-this-operation-to-retrieve-the-userids-of"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 根据unionid获取用户userid"
doc_id: "OtGCDDB9AN"
updated_at: "2026-08-25 09:36:56"
---

> Source: https://open.dingtalk.com/document/development/you-can-call-this-operation-to-retrieve-the-userids-of
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 根据unionid获取用户userid
> Updated: 2026-08-25 09:36:56

# 根据unionid获取用户userid

调用本接口根据unionid获取用户的userid。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[根据unionid获取用户userid](0064-query-a-user-by-the-union-id.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/user/getUseridByUnionid`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |
| unionid | String | 是 | gliiW0piiii02zBUjUxxxx | 用户在当前钉钉开放平台账号范围内的唯一标识，同一个钉钉开放平台账号可以包含多个开放应用，同时也包含ISV的套件应用及企业应用。  可通过调用[查询用户详情](1459-queries-user-details.md)接口获取。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| contactType | Number | 1 | 联系人类型：   - **0**：表示企业内部员工 - **1**：表示企业外部联系人 |
| userid | String | 1 | 用户userid。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/user/getuseridbyunionid?access_token=ACCESS_TOKEN&unionid=gliiW0piiii02zBUjUxxxx
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/user/getUseridByUnionid");
OapiUserGetUseridByUnionidRequest req = new OapiUserGetUseridByUnionidRequest();
req.setUnionid("gliiW0piiii02zBUjUxxxx");
req.setHttpMethod("GET");
OapiUserGetUseridByUnionidResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "errmsg": "ok",
    "contactType": 1,
    "userid": "1"
}
```
