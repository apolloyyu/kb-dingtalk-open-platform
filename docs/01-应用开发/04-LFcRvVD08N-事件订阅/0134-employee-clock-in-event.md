---
title: "员工打卡事件"
source_url: "https://open.dingtalk.com/document/development/employee-clock-in-event"
namespace: "development"
slug: "employee-clock-in-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 考勤 > 员工打卡事件"
doc_id: "TrTp3BgsuN"
updated_at: "2025-08-28 19:46:52"
---

> Source: https://open.dingtalk.com/document/development/employee-clock-in-event
> Path: 应用开发 / 事件订阅 / 智能人事 > 考勤 > 员工打卡事件
> Updated: 2025-08-28 19:46:52

# 员工打卡事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 员工打卡事件 |
| 英文名称 | attendance\_check\_record |

## 功能描述

当考勤数据发生员工打卡时，钉钉推送的员工打卡事件数据。

> 同一个人一分钟打卡多次只算一次，即同一个人一分钟只能推送一次员工打卡事件。

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
- `data.dataList`（array）：数据列表。
- `data.dataList[].address`（string）：打卡位置。
- `data.dataList[].checkTime`（long）：打卡时间。
- `data.dataList[].corpId`（string）：企业的corpid。
- `data.dataList[].locationResult`（string）：定位结果：  
  - Normal：内勤。  
  - Outside：外勤。
- `data.dataList[].groupId`（string）：考勤组的groupId。
- `data.dataList[].latitude`（double）：纬度信息。
- `data.dataList[].bizId`（string）：关联的业务ID。
- `data.dataList[].locationMethod`（string）：打卡方式：  
  - MAP：定位打卡。  
  - WIFI：wifi打卡。  
  - ATM：考勤机打卡或考勤机蓝牙打卡。
- `data.dataList[].userId`（string）：员工的userId。
- `data.dataList[].deviceSN`（string）：考勤机SN。  
    
  当打卡方式为考勤机打卡时返回此字段。
- `data.dataList[].checkByUser`（boolean）：是否用户打卡：  
  - true：用户打卡触发。  
  - false：重排班等引发的系统回放触发。
- `data.dataList[].longitude`（double）：经度信息。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "attendance_check_record",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "dataList": [
      {
        "address": "中国科学院xxx物理研究所(浙江海外高层次人才创新xxx东)",
        "corpId": "dingxxxx",
        "checkTime": 1570791880000,
        "locationResult": "Normal",
        "groupId": "4C63xxxx",
        "latitude": 30.285230848524307,
        "bizId": "FF62xxxx",
        "locationMethod": "MAP",
        "userId": "0126xxxx",
        "deviceSN": "160xxxxx6KN0294",
        "checkByUser": true,
        "longitude": 120.01713514539931
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
- `dataList`（array）：数据列表。
- `dataList[].address`（string）：打卡位置。
- `dataList[].checkTime`（long）：打卡时间。
- `dataList[].corpId`（string）：企业的corpid。
- `dataList[].locationResult`（string）：定位结果：  
  - Normal：内勤。  
  - Outside：外勤。
- `dataList[].groupId`（string）：考勤组的groupId。
- `dataList[].latitude`（double）：纬度信息。
- `dataList[].bizId`（string）：关联的业务ID。
- `dataList[].locationMethod`（string）：打卡方式：  
  - MAP：定位打卡。  
  - WIFI：wifi打卡。  
  - ATM：考勤机打卡或考勤机蓝牙打卡。
- `dataList[].userId`（string）：员工的userId。
- `dataList[].deviceSN`（string）：考勤机SN。  
    
  当打卡方式为考勤机打卡时返回此字段。
- `dataList[].checkByUser`（boolean）：是否用户打卡：  
  - true：用户打卡触发。  
  - false：重排班等引发的系统回放触发。
- `dataList[].longitude`（double）：经度信息。

### **事件体示例**

```
{
  "EventType": "attendance_check_record",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "dataList": [
    {
      "address": "中国科学院xxx物理研究所(浙江海外高层次人才创新xxx东)",
      "corpId": "dingxxxx",
      "checkTime": 1570791880000,
      "locationResult": "Normal",
      "groupId": "4C63xxxx",
      "latitude": 30.285230848524307,
      "bizId": "FF62xxxx",
      "locationMethod": "MAP",
      "userId": "0126xxxx",
      "deviceSN": "160xxxxx6KN0294",
      "checkByUser": true,
      "longitude": 120.01713514539931
    }
  ]
}
```
