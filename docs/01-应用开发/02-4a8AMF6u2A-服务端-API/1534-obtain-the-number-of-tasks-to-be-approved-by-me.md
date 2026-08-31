---
title: "获取用户待审批数量"
source_url: "https://open.dingtalk.com/document/development/obtain-the-number-of-tasks-to-be-approved-by-me"
namespace: "development"
slug: "obtain-the-number-of-tasks-to-be-approved-by-me"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > OA审批 > 获取用户待审批数量"
doc_id: "hy9R3UELUe"
updated_at: "2026-08-25 09:37:45"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-number-of-tasks-to-be-approved-by-me
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > OA审批 > 获取用户待审批数量
> Updated: 2026-08-25 09:37:45

# 获取用户待审批数量

调用本接口根据用户的userid获取该用户待处理的审批数量。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取用户待审批数量](0508-queries-the-number-of-requests-to-be-approved-by-users.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/gettodonum`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证，可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | manager123 | 要查询的用户userid。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| count | Number | 13 | 待处理的审批数量。  **[!NOTE]**  开发者可以通过以下链接，使用[打开目标页面](../03-Ogu5SlPY4t-客户端-JSAPI/0866-open-link-on-new-window.md)跳转到钉钉审批移动端微应用（暂不支持PC端）的待我审批页面：  https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?showmenu=false&dd\_share=false&corpid=$CORPID#/upcoming?swfrom=work\_homepage |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回描述。 |
| request\_id | String | 3x1lrffff9xk | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/gettodonum?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "userid":"manager4220"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/gettodonum");
OapiProcessGettodonumRequest req = new OapiProcessGettodonumRequest();
req.setUserid("manager4220");
OapiProcessGettodonumResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "count": 1,
  "errcode": 0,
  "errmsg":"ok",
  "request_id": "3x1lrffff9xk"
}
```
