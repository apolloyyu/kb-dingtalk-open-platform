---
title: "智能硬件绑定"
source_url: "https://open.dingtalk.com/document/development/smart-hardware-binding-stream"
namespace: "development"
slug: "smart-hardware-binding-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 智能硬件事件 > 智能硬件绑定"
doc_id: "vjX6bJXbX2"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/smart-hardware-binding-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 智能硬件事件 > 智能硬件绑定
> Updated: 2022-01-19 19:29:22

# 智能硬件绑定

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 智能硬件绑定 |
| 英文名称 | device\_bind\_update |

## 功能描述

eventType为device\_bind\_update，表示企业发生硬件设备绑定变更时推送的智能硬件绑定事件数据。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 不支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### data部分(事件业务信息)

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "device_bind_update",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "actionType": "bind",
    "corpId": "dinga39fdxxxx",
    "outBindStatus": "ok",
    "dn": "设备dn",
    "pk": "产品编码",
    "sn": "设备sn",
    "nodeType": 0,
    "serviceId": 12246,
    "userId": "123455",
    "deviceId": 13344,
    "eventTimestamp": 16848000097
  }
}
```
