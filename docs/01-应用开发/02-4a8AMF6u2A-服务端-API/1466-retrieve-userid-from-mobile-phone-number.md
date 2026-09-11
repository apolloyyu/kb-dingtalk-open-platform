---
title: "根据手机号查询用户"
source_url: "https://open.dingtalk.com/document/development/retrieve-userid-from-mobile-phone-number"
namespace: "development"
slug: "retrieve-userid-from-mobile-phone-number"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 根据手机号查询用户"
doc_id: "JrHCzSHRjF"
updated_at: "2026-08-25 09:36:56"
---

> Source: https://open.dingtalk.com/document/development/retrieve-userid-from-mobile-phone-number
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 根据手机号查询用户
> Updated: 2026-08-25 09:36:56

# 根据手机号查询用户

调用本接口根据手机号获取用户的userid。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[根据手机号查询用户](0063-query-users-by-phone-number.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/user/get_by_mobile`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 |
| mobile | String | 是 | 150xxxx2547 | 要获取的用户手机号。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| userid | String | manager123 | 员工在当前企业内的唯一标识。  **[!NOTE]**  员工离职后，无法再通过手机号获取userid。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/user/get_by_mobile?access_token=ACCESS_TOKEN&mobile=150xxxx2547
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/user/get_by_mobile");
OapiUserGetByMobileRequest req = new OapiUserGetByMobileRequest();
req.setMobile("150xxxx2547");
req.setHttpMethod("GET");
OapiUserGetByMobileResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "errcode":0,
        "errmsg":"ok",
        "userid":"manager123"
}
```
