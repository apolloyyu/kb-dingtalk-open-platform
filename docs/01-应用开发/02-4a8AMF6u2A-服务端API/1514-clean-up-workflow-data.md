---
title: "清理审批数据"
source_url: "https://open.dingtalk.com/document/development/clean-up-workflow-data"
namespace: "development"
slug: "clean-up-workflow-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 清理审批数据"
doc_id: "7n4BtAF9yn"
updated_at: "2026-08-20 16:40:54"
---

> Source: https://open.dingtalk.com/document/development/clean-up-workflow-data
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 清理审批数据
> Updated: 2026-08-20 16:40:54

# 清理审批数据

调用本接口清理审批相关数据。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对OA审批相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/isvapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于2022年10月8日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用新版规范[清理OA审批数据](https://open.dingtalk.com/document/isvapp/clear-oa-approval-data)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

企业在某种情况下不再使用ISV的应用，比如服务到期或主动解除授权（非停用），ISV可以调用此接口，删除企业的审批模板、实例、任务等数据。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 否 | — | — |
| 第三方企业应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/clean`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| suite\_access\_token | String | 是 | 6d1bxxxx | 调用服务端API授权凭证，可通过[获取第三方企业应用的suiteAccessToken](https://open.dingtalk.com/document/isvapp/obtains-the-suite_acess_token-of-third-party-enterprise-applications)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| process\_code | String | 是 | PROC-EF6YJL35 | 模板唯一码。 |
| corpid | String | 是 | ding1234 | 企业的corpid。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回码描述。 |
| request\_id | String | 7jtw2fl4kmlm | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/clean?suite_access_token=SUITE_ACCESS_TOKEN
```

请求正文

```
{
        "corpid":"ding1234",
        "process_code":"PROC-EF6YJL35"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/clean");
OapiProcessCleanRequest req = new OapiProcessCleanRequest();
req.setProcessCode("PROC-EF6YJL35");
req.setCorpid("ding1234");
OapiProcessCleanResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "errcode":0,
        "request_id": "146262d9p0xmi"
}
```
