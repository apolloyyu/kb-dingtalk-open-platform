---
title: "考勤事件"
source_url: "https://open.dingtalk.com/document/development/attendance-events"
namespace: "development"
slug: "attendance-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 企业内部应用回调事件 > 考勤事件"
doc_id: "obmosRKJnc"
updated_at: "2025-10-16 14:31:56"
---

> Source: https://open.dingtalk.com/document/development/attendance-events
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 企业内部应用回调事件 > 考勤事件
> Updated: 2025-10-16 14:31:56

# 考勤事件

本文介绍了考勤事件的相关说明。

开发者注册回调事件时填写的事件类型“call\_back\_tag”包含考勤事件类型，当考勤数据发生变化时，如发生员工打卡、员工排班更改、员工加班等，钉钉服务器会向回调url推送事件。

## 事件类型

| **事件类型** | **类别** | **说明** |
| --- | --- | --- |
| attendance\_check\_record | 打卡 | 员工打卡事件。 |
| attendance\_schedule\_change | 排班 | 员工排班变更事件。 |
| attendance\_overtime\_duration | 加班 | 员工加班事件。 |
| attend\_group\_change | 考勤组 | 考勤组变更事件。 |
| attend\_shift\_change | 班次 | 班次变更事件。 |

## 员工打卡事件

**POST数据解密后示例：**

```
{
  "DataList": [
    {
      "address": "中国科学院工程热物理研究所(浙江海外高层次人才创新园7幢东)",
      "checkTime": 1570791880000,
      "corpId": "dingxxxx",
      "groupId": "4C63xxxx",
      "latitude": 30.285230848524307,
      "bizId": "FF62xxxx",
      "locationMethod": "MAP",
      "userId": "0126xxxx",
      "deviceSN": "160xxxxx6KN0294",
      "longitude": 120.01713514539931,
      "locationResult": "Normal",
      "checkByUser": true
    }
  ],
  "EventType": "attendance_check_record"
}
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| DataList | 数据列表。 |
| address | 打卡位置。 |
| checkTime | 打卡时间。 |
| corpId | 企业的corpid。 |
| groupId | 考勤组的groupId。 |
| latitude | 纬度信息。 |
| bizId | 关联的业务ID。 |
| locationMethod | 打卡方式。   - **MAP**：定位打卡 - **WIFI**：wifi打卡 - **ATM**：考勤机打卡或考勤机蓝牙打卡 |
| userId | 员工的userId。 |
| longitude | 经度信息。 |
| deviceSN | 考勤机SN。  当打卡方式为考勤机打卡时返回此字段。 |
| locationResult | 定位结果。   - **Normal**：内勤 - **Outside**：外勤 |
| checkByUser | 是否用户打卡：   - true：用户打卡触发 - false：重排班等引发的系统回放触发 |

## 员工排班变更事件

**POST数据解密后示例：**

```
{
    "DataList":[
        {
            "workDateEnd":1571328000000,
            "corpId":"dingxxxx",
            "userIds":[
                "0126xxxx"
            ],
            "type":"modify",
            "workDateBegin":1571328000000
        }
    ],
    "EventType":"attendance_schedule_change"
}
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| DataList | 数据列表。 |
| workDateEnd | 排班结束时间。 |
| corpId | 企业的corpId。 |
| userIds | 员工的userIds列表。 |
| type | 类型。   - **modify**：修改排班 - **delete**：删除排班 |
| workDateBegin | 排班开始时间。 |

## 员工加班事件

**POST数据解密后示例：**

```
{
    "DataList":[
        {        
                        "corpId":"dingxxxx",
                        "userid":"1234xxxx",
                        "overtimeDay":1.0,
                        "overtimeHour":8.0,
                        "workDate":1571033937000
        }
    ],
    "EventType":"attendance_overtime_duration"
}
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| DataList | 数据列表。 |
| workDate | 加班日期。 |
| corpId | 企业的corpId。 |
| userid | 员工的userid。 |
| overtimeDay | 加班时长，单位天。 |
| overtimeHour | 加班时长，单位小时。 |

## **考勤组变更事件**

**POST数据解密后示例：**

```
{
  "corpid": "dingxxxx",
  "name":"考勤组A",
  "action":"attend_group_delete",
  "id":11112222
  "EventType": "attend_group_change"
}
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| corpid | 企业的corpId。 |
| name | 考勤组名称。 |
| action | 考勤组动作简要信息：   - **attend\_group\_create**：企业增加考勤组之后的简要信息。 - **attend\_group\_update**：企业修改考勤组之后的简要信息。 - **attend\_group\_delete**：企业删除考勤组之后的简要信息。 |
| id | 考勤组id。 |

## 班次变更事件

**POST数据解密后示例：**

```
{
    "EventType": "attend_shift_change",
    "corpid": "dingxxxx",
    "name":"班次A",
    "action":"attend_shift_delete",
    "id":11112222
}
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| corpid | 企业的corpId。 |
| name | 考勤组名称。 |
| action | 班次动作简要信息：   - **attend\_shift\_create**：企业增加班次之后的简要信息。 - **attend\_shift\_update**：企业修改班次之后的简要信息。 - **attend\_shift\_delete**：企业删除班次之后的简要信息。 |
| id | 班次id。 |
