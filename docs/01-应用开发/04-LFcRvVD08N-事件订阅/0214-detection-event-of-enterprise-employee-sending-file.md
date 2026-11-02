---
title: "企业员工发送文件的检测事件"
source_url: "https://open.dingtalk.com/document/development/detection-event-of-enterprise-employee-sending-file"
namespace: "development"
slug: "detection-event-of-enterprise-employee-sending-file"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "专属开放 > 企业员工发送文件的检测事件"
doc_id: "tt1LAEZlfv"
updated_at: "2025-08-28 19:47:31"
---

> Source: https://open.dingtalk.com/document/development/detection-event-of-enterprise-employee-sending-file
> Path: 应用开发 / 事件订阅 / 专属开放 > 企业员工发送文件的检测事件
> Updated: 2025-08-28 19:47:31

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.fileRecords`（array）：发送文件记录。
- `data.fileRecords[].openCid`（string）：发送文件时的会话id。
- `data.fileRecords[].fileName`（string）：文件名。
- `data.fileRecords[].ossKey`（string）：文件在专属存储上的ossKey。
- `data.fileRecords[].requestId`（string）：发送该文件的请求id。
- `data.fileRecords[].userId`（string）：发送文件的企业员工userId。

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

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `fileRecords`（array）：发送文件记录。
- `fileRecords[].openCid`（string）：发送文件时的会话id。
- `fileRecords[].fileName`（string）：文件名。
- `fileRecords[].ossKey`（string）：文件在专属存储上的ossKey。
- `fileRecords[].requestId`（string）：发送该文件的请求id。
- `fileRecords[].userId`（string）：发送文件的企业员工userId。

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
