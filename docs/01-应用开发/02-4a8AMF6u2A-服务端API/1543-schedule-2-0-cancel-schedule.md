---
title: "取消日程"
source_url: "https://open.dingtalk.com/document/development/schedule-2-0-cancel-schedule"
namespace: "development"
slug: "schedule-2-0-cancel-schedule"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 协同办公 > 日程 > 取消日程"
doc_id: "I92rWRpY8n"
updated_at: "2026-08-25 09:38:07"
---

> Source: https://open.dingtalk.com/document/development/schedule-2-0-cancel-schedule
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 协同办公 > 日程 > 取消日程
> Updated: 2026-08-25 09:38:07

# 取消日程

调用该接口取消日程，只能取消通过**创建日程**接口创建的日程。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[删除日程](0251-delete-event.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/calendar/v2/event/cancel`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| calendar\_id | String | 是 | primary | 日历ID。  目前仅支持传**primary**表示修改当前用户“我的日程”下的日程。 |
| event\_id | String | 是 | 053E8xxxx | 加密后的日程ID。 |
| agentid | Number | 否 | 1212 | 应用对应的AgentId。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | zbbs6uxpei1r | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/calendar/v2/event/cancel?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "agentid": 923680251,
  "event_id": "053ExxxxA1FE",
  "calendar_id": "primary"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/calendar/v2/event/cancel");
OapiCalendarV2EventCancelRequest req = new OapiCalendarV2EventCancelRequest();
req.setCalendarId("primary");
req.setEventId("053ExxxxA1FE");
req.setAgentid(923680251L);
OapiCalendarV2EventCancelResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "success": true,
  "request_id": "3wiymoeilfb6"
}
```
