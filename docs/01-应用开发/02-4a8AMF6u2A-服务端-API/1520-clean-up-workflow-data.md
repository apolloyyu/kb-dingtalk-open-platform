---
title: "清理审批数据"
source_url: "https://open.dingtalk.com/document/development/clean-up-workflow-data"
namespace: "development"
slug: "clean-up-workflow-data"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > OA审批 > 清理审批数据"
doc_id: "7n4BtAF9yn"
updated_at: "2026-08-25 09:37:40"
---

> Source: https://open.dingtalk.com/document/development/clean-up-workflow-data
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > OA审批 > 清理审批数据
> Updated: 2026-08-25 09:37:40

# 清理审批数据

企业在某种情况下不再使用ISV的应用，比如服务到期或主动解除授权（非停用），ISV可以调用此接口，删除企业的审批模板、实例、任务等数据。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[发起审批实例](0497-create-an-approval-instance.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 否 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/clean`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| suite\_access\_token | String | 是 | 6d1bxxxx | 调用服务端API授权凭证，可通过[获取第三方企业应用的suite\_access\_token](1447-obtain-application-suite-ticket.md)接口获取。 |

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
