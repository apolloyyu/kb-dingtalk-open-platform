---
title: "更新企业内部应用微应用的可使用范围"
source_url: "https://open.dingtalk.com/document/development/set-the-visible-range-of-the-microapplication"
namespace: "development"
slug: "set-the-visible-range-of-the-microapplication"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 应用管理 > 更新企业内部应用微应用的可使用范围"
doc_id: "ogJAcVM1ru"
updated_at: "2026-08-25 09:39:03"
---

> Source: https://open.dingtalk.com/document/development/set-the-visible-range-of-the-microapplication
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 应用管理 > 更新企业内部应用微应用的可使用范围
> Updated: 2026-08-25 09:39:03

# 更新企业内部应用微应用的可使用范围

调用本接口设置指定应用的可见范围。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[更新企业内部应用的可使用范围](0871-update-the-visible-range-of-micro-applications.md)接口，已接入用户不受影响。

> **[!NOTE]**
>
> - 企业内部应用-H5微应用
>
>   - 当前H5微应用是开发版本，调用本接口可指定H5微应用开发版本的可见范围。
>   - 当前H5微应用是线上版本，调用本接口可指定H5微应用线上版本的可见范围。
> - 企业内部应用-小程序应用
>
>   - 仅在小程序线上版本适用。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/microapp/set_visible_scopes`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端接口的授权凭证，可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userVisibleScopes | String[] | 否 | ["userId1","userId2"] | 设置可见的员工userid列表，格式为JSON数组。 |
| deptVisibleScopes | Number[] | 否 | [1,2] | 设置可见的部门ID列表，格式为JSON数组。 |
| isHidden | Boolean | 否 | false | 是否仅限管理员可见：   - **true** - **false** |
| agentId | Number | 是 | 16691682 | 应用AgentID。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码。 |
| errcode | Number | 0 | 返回码描述。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/microapp/set_visible_scopes?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "agentId": 852825694,
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

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/microapp/set_visible_scopes");
OapiMicroappSetVisibleScopesRequest req = new OapiMicroappSetVisibleScopesRequest();
req.setUserVisibleScopes(Arrays.asList("user123","manager4220"));
req.setDeptVisibleScopes(Arrays.asList(1L,2L));
req.setIsHidden(false);
req.setAgentId(852825694L);
OapiMicroappSetVisibleScopesResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode":0,
  "errmsg":"ok"
}
```
