---
title: "获取企业内部应用微应用的可使用范围"
source_url: "https://open.dingtalk.com/document/development/gets-the-microapplication-visible-range-set-by-the-enterprise"
namespace: "development"
slug: "gets-the-microapplication-visible-range-set-by-the-enterprise"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 应用管理 > 获取企业内部应用微应用的可使用范围"
doc_id: "2FknmSg368"
updated_at: "2026-08-25 09:39:04"
---

> Source: https://open.dingtalk.com/document/development/gets-the-microapplication-visible-range-set-by-the-enterprise
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 应用管理 > 获取企业内部应用微应用的可使用范围
> Updated: 2026-08-25 09:39:04

# 获取企业内部应用微应用的可使用范围

调用本接口获取应用的可见范围。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取企业内部应用的可使用范围](0872-obtains-the-application-visible-range.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/microapp/visible_scopes`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端接口的授权凭证，可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| agentId | Number | 是 | 123 | 应用ID。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| userVisibleScopes | String[] | ["user123","manager4220"] | 应用可见的用户列表。 |
| deptVisibleScopes | Number[] | [1,2] | 应用可见的部门列表。 |
| isHidden | Boolean | false | 是否仅限管理员可见，true代表仅限管理员可见。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/microapp/visible_scopes?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "agentId":852825694
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/microapp/visible_scopes");
OapiMicroappVisibleScopesRequest req = new OapiMicroappVisibleScopesRequest();
req.setAgentId(852825694L);
OapiMicroappVisibleScopesResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "userVisibleScopes": [
    "user123",
    "manager4220"
  ],
  "deptVisibleScopes": [
    1,
    2
  ],
  "isHidden": false
}
```
