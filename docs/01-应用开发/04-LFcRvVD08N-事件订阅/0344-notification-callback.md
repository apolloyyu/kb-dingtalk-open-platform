---
title: "e签宝事件"
source_url: "https://open.dingtalk.com/document/development/notification-callback"
namespace: "development"
slug: "notification-callback"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > e签宝事件"
doc_id: "KRNGGRqg07"
updated_at: "2025-10-16 15:06:44"
---

> Source: https://open.dingtalk.com/document/development/notification-callback
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > e签宝事件
> Updated: 2025-10-16 15:06:44

# e签宝事件

由于文档签署涉及大量数字签名、文档操作等耗时操作，签署任务的执行采用异步方式进行，完成后通过回调的方式通知平台方签署结果。目前通知回调通过HTTP协议，POST 方法进行通知调用。

## 事件类型

| 事件类型 | 说明 |
| --- | --- |
| SIGN | 签署事件回调。 |
| CORP\_AUTH | 授权事件回调。 |

## 签署事件回调

**示例**：

```
{
    "action": "SIGN",
    "taskId": "",
    "bizData": {
        "status": "RUNNING",
        "finishTime": 123123123
    }
}
```

**参数说明**：

| 参数 | 说明 |
| --- | --- |
| action | 操作类型。 |
| taskId | 签署任务id。 |
| bizData | action对应的业务数据。 |
| status | 签署状态：   - **RUNNING**：签署中 - **FINISH**：签署完成 - **REVOKE**：撤销 - **REFUSE**：拒签 |
| finishTime | 签署完成时间。  **[!NOTE]**  当status状态为**FINISH**时，该参数才有值。 |

## 授权事件回调

**示例**：

```
{
    "action": "CORP_AUTH",
    "taskId": "",
    "bizData": {
        "status": "SUCCESS"

    }
}
```

**参数说明**：

| 参数 | 说明 |
| --- | --- |
| action | 操作类型。 |
| taskId | 签署任务id。 |
| bizData | action对应的业务数据。 |
| status | 授权结果：  **SUCCESS**：授权成功  **FALL**：授权失败 |

## 注意事项

- 调用超时时间5秒，首次调用失败后，3s后重试；再次失败后间隔6s再次重试，再次失败则不再通知。
- 对接方在接收到回调请求时，需返回HTTP状态码200，并保证返回的json数据不包含`空格\ /`等特殊字符。
- 为了保障异步通知的可靠性，建议业务方在回调请求处理中，尽可能减少业务操作，改用异步方式处理后续业务流程。
