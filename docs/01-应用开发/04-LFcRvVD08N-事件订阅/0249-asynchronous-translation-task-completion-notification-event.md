---
title: "异步转译通讯录id任务完成通知事件"
source_url: "https://open.dingtalk.com/document/development/asynchronous-translation-task-completion-notification-event"
namespace: "development"
slug: "asynchronous-translation-task-completion-notification-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 事件列表 > 异步转译通讯录id任务完成通知事件"
doc_id: "P9EWqqSzi0"
updated_at: "2025-12-08 14:44:45"
---

> Source: https://open.dingtalk.com/document/development/asynchronous-translation-task-completion-notification-event
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 事件列表 > 异步转译通讯录id任务完成通知事件
> Updated: 2025-12-08 14:44:45

# 异步转译通讯录id任务完成通知事件

本文介绍了异步转译通讯录id任务完成通知事件的相关说明。

如果注册回调事件时包含异步转译通讯录id任务完成通知事件“transfer\_contact\_id\_job\_result”，当异步转译通讯录id任务完成通知发生后，钉钉服务器会向回调url推送事件。

## 事件类型

| **事件类型** | **说明** |
| --- | --- |
| transfer\_contact\_id\_job\_result | 异步转译通讯录id任务完成通知事件 |

## 异步转译通讯录id任务完成通知

**示例：**

```
{
    "EventType": "transfer_contact_id_job_result",
    "EventTime": 1631700358973,
    "CorpId": "ding1d4b5fc9223daa8e35c2f4657xxxxxx",
    "BizId": "rLwFw5k5GZ0Z7Iv2eD6ggOuXHlNCtPBwQYhbcPMw0U0GZr7z15BW2xxxxxxxx",
    "jobId": "rLwFw5k5GZ0Z7Iv2eD6ggOuXHlNCtPBwQYhbcPMw0U0GZr7z15BW2xxxxxxxx",
    "status": 1
}
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| EventTime | 事件发生时间。 |
| CorpId | 企业CorpId。 |
| BizId | 无业务意义，幂等。 |
| jobId | 任务ID。 |
| status | 任务状态。 |
