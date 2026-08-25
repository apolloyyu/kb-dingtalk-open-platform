---
title: "获取应用自定义空间使用详情"
source_url: "https://open.dingtalk.com/document/development/queries-the-usage-details-of-a-custom-application-space"
namespace: "development"
slug: "queries-the-usage-details-of-a-custom-application-space"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 钉盘 > 获取应用自定义空间使用详情"
doc_id: "pIA24GhTlB"
updated_at: "2026-08-25 09:38:17"
---

> Source: https://open.dingtalk.com/document/development/queries-the-usage-details-of-a-custom-application-space
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 文档/文件 > 钉盘 > 获取应用自定义空间使用详情
> Updated: 2026-08-25 09:38:17

# 获取应用自定义空间使用详情

调用本接口获取自定义空间已使用容量，单位为Bytes。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取空间信息](0653-get-space-information.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/cspace/used_info`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |
| domain | String | 是 | aaa | 企业调用时传入，需要为10个字节以内的字符串，仅可包含字母和数字，大小写不敏感。 |
| agent\_id | String | 是 | 86881016 | 应用的AgentId。   - 企业内部应用可以在[开发者后台](https://open-dev.dingtalk.com/)的应用详情页获取。 - 第三方企业应用可以调用[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| used\_size | String | 20053759 | 对应空间已使用大小，单位为Bytes。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/cspace/used_info?access_token=ACCESS_TOKEN&domain=aaa&agent_id=123
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/cspace/used_info");
OapiCspaceGetCustomSpaceRequest request = new OapiCspaceGetCustomSpaceRequest();
request.setAgentId("115xxx");
request.setDomain("userxxx");
request.setHttpMethod("GET");
OapiCspaceGetCustomSpaceResponse response = client.execute(request, access_token);
System.out.println(response.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "used_size": 20053759
}
```
