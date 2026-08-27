---
title: "删除H5微应用"
source_url: "https://open.dingtalk.com/document/development/delete-an-h5-microapplication"
namespace: "development"
slug: "delete-an-h5-microapplication"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 应用管理 > 删除H5微应用"
doc_id: "04ZuBzGhPg"
updated_at: "2026-08-25 09:39:05"
---

> Source: https://open.dingtalk.com/document/development/delete-an-h5-microapplication
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 应用管理 > 删除H5微应用
> Updated: 2026-08-25 09:39:05

# 删除H5微应用

调用本接口删除H5微应用。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[删除企业内部应用](0863-delete-an-internal-h5-application.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/microapp/delete`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端接口的授权凭证，可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| agentId | Number | 是 | 1144651083 | H5微应用的agentid。企业只能删除自建H5微应用。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/microapp/delete?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "agentId":1144651083
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/microapp/delete");
OapiMicroappDeleteRequest req = new OapiMicroappDeleteRequest();
req.setAgentId(1144651083L);
OapiMicroappDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "agentId": 1144651083
}
```
