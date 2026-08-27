---
title: "获取管理员列表"
source_url: "https://open.dingtalk.com/document/development/obtains-a-list-of-administrators"
namespace: "development"
slug: "obtains-a-list-of-administrators"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 获取管理员列表"
doc_id: "d4B7upM7dE"
updated_at: "2026-08-25 09:36:57"
---

> Source: https://open.dingtalk.com/document/development/obtains-a-list-of-administrators
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 获取管理员列表
> Updated: 2026-08-25 09:36:57

# 获取管理员列表

调用本接口获取管理员列表。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取管理员列表](0068-query-the-administrator-list.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/user/get_admin`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码。 |
| errcode | Number | 0 | 返回码描述。 |
| adminList | AdminList[] |  | 管理员列表。 |
| sys\_level | Number | 1 | 管理员角色：   - **1**：表示主管理员 - **2**：表示子管理员 |
| userid | String | manger123 | 用户userid。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/user/get_admin?access_token=ACCESS_TOKEN
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/user/get_admin");
OapiUserGetAdminRequest req = new OapiUserGetAdminRequest();
req.setHttpMethod("GET");
OapiUserGetAdminResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode":0,
  "errmsg":"ok",
  "adminList":[
    {
      "sys_level":1,
      "userid":"manger123"
    }
  ]
}
```
