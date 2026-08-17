---
title: "企业员工发送文件的检测事件"
source_url: "https://open.dingtalk.com/document/development/detection-event-of-enterprise-employee-sending-file"
namespace: "development"
slug: "detection-event-of-enterprise-employee-sending-file"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "专属开放 > 企业员工发送文件的检测事件"
doc_id: "tt1LAEZlfv"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/detection-event-of-enterprise-employee-sending-file
> Path: 应用开发 / 事件订阅 / 专属开放 > 企业员工发送文件的检测事件
> Updated: 2022-01-19 19:29:22

# 企业员工发送文件的检测事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业员工发送文件的检测事件 |
| 英文名称 | org\_file\_send\_check |

## 功能描述

专属钉钉大客户事件，企业员工发送文件的检测事件的推送数据。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "org_file_send_check",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "fileRecords": [
      {
        "openCid": "cidhoEzLAXnkhNZYlHg6PqcTzSlxxxdsfs",
        "fileName": "测试",
        "ossKey": "lA6h5dW5kaXNrMATOIQUokAXNB9IGAAxxx",
        "requestId": "dlpId4c5219a39xxx",
        "userId": "304235493xxxx"
      }
    ]
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "org_file_send_check",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "fileRecords": [
    {
      "openCid": "cidhoEzLAXnkhNZYlHg6PqcTzSlxxxdsfs",
      "fileName": "测试",
      "ossKey": "lA6h5dW5kaXNrMATOIQUokAXNB9IGAAxxx",
      "requestId": "dlpId4c5219a39xxx",
      "userId": "304235493xxxx"
    }
  ]
}
```
