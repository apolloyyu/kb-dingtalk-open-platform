---
title: "获取日志统计数据"
source_url: "https://open.dingtalk.com/document/development/query-log-statistics"
namespace: "development"
slug: "query-log-statistics"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 协同办公 > 日志 > 获取日志统计数据"
doc_id: "oG0dIG1XWk"
updated_at: "2026-08-25 09:38:08"
---

> Source: https://open.dingtalk.com/document/development/query-log-statistics
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 协同办公 > 日志 > 获取日志统计数据
> Updated: 2026-08-25 09:38:08

# 获取日志统计数据

调用本接口，获取日志的已读人数、评论条数、评论人数、点赞人数。

> **[!IMPORTANT]**
>
> 为统一数据资产管理体验，钉钉数据资产平台已整合原分散的数据服务。本接口及另外 60 个[数据资产类OpenAPI](https://open.dingtalk.com/document/dataservice/data-asset-interface-adjustment-description) 已停止新权限申请，本文档同步迁入「历史文档」目录。
>
> 本接口仅保持现有功能，不再新增支持其他能力，说明如下：
>
> - **未接入用户**：请直接使用[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)获取数据服务。
> - **已接入用户**：请评估业务情况，逐步切换至钉钉数据资产平台。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/report/statistics`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| report\_id | String | 是 | 174xxxx | 日志ID。调用[获取用户发送日志的概要信息](0298-view-log-summary-data.md)或[获取用户发出的日志列表](0297-query-logs-sent-by-an-employee.md)接口获取report\_id参数值。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ReportStatisticsVo |  | 返回结果。 |
| read\_num | Number | 1 | 已读人数。 |
| comment\_num | Number | 1 | 评论个数。 |
| comment\_user\_num | Number | 1 | 去重后的评论人数。 |
| like\_num | Number | 1 | 点赞人数。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | 43knzyjc6f2b | 请求ID。 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/report/statistics?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "report_id":"174xxxx"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/statistics");
OapiReportStatisticsRequest req = new OapiReportStatisticsRequest();
req.setReportId("174xxxx");
OapiReportStatisticsResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "result": {
    "comment_num": 1,
    "comment_user_num": 1,
    "like_num": 1,
    "read_num": 0
  },
  "success": true,
  "request_id": "43knzyjc6f2b"
}
```
