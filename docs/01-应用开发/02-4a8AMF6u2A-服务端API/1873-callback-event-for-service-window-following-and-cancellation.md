---
title: "服务窗关注与取消回调"
source_url: "https://open.dingtalk.com/document/development/callback-event-for-service-window-following-and-cancellation"
namespace: "development"
slug: "callback-event-for-service-window-following-and-cancellation"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 客户管理（官方CRM） > 服务窗 > 服务窗关注与取消回调"
doc_id: "2qn7GNbv6f"
updated_at: "2025-10-17 13:00:09"
---

> Source: https://open.dingtalk.com/document/development/callback-event-for-service-window-following-and-cancellation
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 客户管理（官方CRM） > 服务窗 > 服务窗关注与取消回调
> Updated: 2025-10-17 13:00:09

# 服务窗关注与取消回调

本文介绍了服务窗的回调事件类型、数据推送，以及POST数据进行解密后，对POST参数的详细说明。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，客户管理的服务窗接口已升级。客户管理-服务窗关注与取消回调事件文档已于2022年11月30日移动至历史文档（不推荐）目录。新用户请关注[服务窗事件](https://open.dingtalk.com/document/orgapp/service-window-event-callback)。

## 事件类型

服务窗包含如下事件类型：

| 事件类型 | 说明 |
| --- | --- |
| ding\_crm\_service\_subscribe | 服务窗关注事件。 |
| ding\_crm\_service\_unsubscribe | 服务窗取消关注事件。 |

## 数据推送

**POST数据解密后示例**：

```
{
    "instanceIdList": [
        "946b6da5-47a6-xxxx852a655200f9",
        "946b6da5-47a6-xxxx852a612312f9"
    ],
    "instances": [
        {
            "instanceId": "ca99de48-aba7-xxxx4d82b789921a",
            "unionId": "zDLvntTqxxxxoiE",
            "userId": "onu6lbcqisxxxxolttp75u",
            "objectType": "crm_contact"
        }
    ],
    "TimeStamp": "14023842343204",
    "EventType": "ding_crm_service_unsubscribe"
}
```

**参数说明**：

| 参数 | 说明 |
| --- | --- |
| instanceIdList | 联系人实例ID列表，可通过[按照ID列表批量获取联系人数据](https://open.dingtalk.com/document/orgapp/retrieves-contact-data-in-batches-based-on-the-id-list)接口获取。 |
| instances | 联系人实例ID列表所对应的实例数据，包括instanceId和userId。 |
| EventType | 事件类型：   - **ding\_crm\_service\_unsubscribe**：取消关注 - **ding\_crm\_service\_subscribe**：关注 |
| TimeStamp | 时间戳。 |

## 相关文档

- [配置事件订阅](https://open.dingtalk.com/document/orgapp/configure-event-subcription)
