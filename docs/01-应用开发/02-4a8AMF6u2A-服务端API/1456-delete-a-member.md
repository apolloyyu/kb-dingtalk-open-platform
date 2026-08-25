---
title: "删除用户"
source_url: "https://open.dingtalk.com/document/development/delete-a-member"
namespace: "development"
slug: "delete-a-member"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 删除用户"
doc_id: "1f7yrRpDfE"
updated_at: "2026-08-25 09:36:50"
---

> Source: https://open.dingtalk.com/document/development/delete-a-member
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 删除用户
> Updated: 2026-08-25 09:36:50

# 删除用户

调用本接口删除指定用户。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版 [删除用户](0058-delete-a-user.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/user/delete`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6ed1bxxx | 调用服务端API授权凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |
| userid | String | 是 | user123 | 员工唯一标识userid，可通过[根据手机号查询用户](1463-retrieve-userid-from-mobile-phone-number.md)接口获取userid。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/user/delete?access_token=ACCESS_TOKEN&userid=user123
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/user/delete");
OapiUserDeleteRequest req = new OapiUserDeleteRequest();
req.setUserid("user123");
req.setHttpMethod("GET");
OapiUserDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "errcode":0,
        "errmsg":"ok"
}
```
