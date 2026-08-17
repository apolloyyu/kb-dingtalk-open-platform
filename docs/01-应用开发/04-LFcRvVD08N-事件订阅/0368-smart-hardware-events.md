---
title: "智能硬件事件"
source_url: "https://open.dingtalk.com/document/development/smart-hardware-events"
namespace: "development"
slug: "smart-hardware-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 智能硬件事件"
doc_id: "4n7weefU1A"
updated_at: "2025-10-16 15:06:42"
---

> Source: https://open.dingtalk.com/document/development/smart-hardware-events
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 智能硬件事件
> Updated: 2025-10-16 15:06:42

# 智能硬件事件

本文介绍了智能硬件相关的RDS和SyncHTTP推送的数据格式。

## 配置事件回调

第三方企业应用配置事件订阅流程，请参见[第三方企业应用事件与回调流程](https://open.dingtalk.com/document/isvapp/third-party-enterprise-application-address-book-change-event-subscription-process)。

## 智能硬件数据表

| **主键（id）** | **订阅者ID（**subscribe\_id**）** | **企业ID（**corp\_id**）** | **业务ID（**biz\_id**）** | **业务类型（**biz\_type**）** | 说明 |
| --- | --- | --- | --- | --- | --- |
| 32 | xxxxx\_0 | corpxxxx | 绑定： active+设备id  解绑： delete+设备id | 32 | 智能硬件绑定类型 |

## biz\_type=32

当biz\_type=32时，数据为智能硬件设备管理。

该数据为企业发生硬件设备绑定变更时推送，插入表open\_sync\_biz\_data中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 第三方企业应用的suiteid加下划线0。 |
| corp\_id | 开通第三方企业应用的企业corpid。 |
| biz\_id | 绑定： active + 设备id  解绑： delete + 设备id |
| biz\_type | 32，为固定值，标识是智能硬件绑定类型消息。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下。

- 绑定事件

  ```
  {
    "actionType": "bind",
    "corpId": "yourcorpid",
    "syncAction": "device_bind_update",
    "sn": "设备sn",
    "pk": "产品编码",
    "nodeType": 0,
    "deviceId": 设备id
  }
  ```
- 解绑事件

  ```
  {
    "actionType": "unbind",
    "corpId": "yourcorpid",
    "syncAction": "device_bind_update",
    "sn": "设备sn",
    "pk": "产品编码",
    "nodeType": 0,
    "deviceId": 设备id
  }
  ```

**字段说明：**

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| actionType | String | - bind：绑定 - unbind：解绑 |
| corpId | String | 企业的corpid。 |
| syncAction | String | 数据类型。 |
| sn | String | 设备序列号。 |
| pk | String | productKey，产品类型编码。 |
| nodeType | Integer | 节点类型：   - 0： 节点 - 1：网关 |
| deviceId | Long | 设备ID。 |
| eventTimestamp | Long | 设备变化的时间戳。 |
| outBindStatus | String | 外部的绑定状态， ok 表示成功，其他表示失败 |
