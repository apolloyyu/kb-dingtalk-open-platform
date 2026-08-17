---
title: "考勤事件"
source_url: "https://open.dingtalk.com/document/development/subscribe-to-attendance-events"
namespace: "development"
slug: "subscribe-to-attendance-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 考勤事件 > 考勤事件"
doc_id: "WUjGZEl0LS"
updated_at: "2025-12-08 15:45:08"
---

> Source: https://open.dingtalk.com/document/development/subscribe-to-attendance-events
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 考勤事件 > 考勤事件
> Updated: 2025-12-08 15:45:08

# 考勤事件

本文介绍了考勤相关的RDS和SyncHTTP推送的数据格式。

## 配置事件回调

第三方企业应用配置事件订阅流程，请参见[第三方企业应用事件与回调流程](https://open.dingtalk.com/document/isvapp/third-party-enterprise-application-address-book-change-event-subscription-process)。

## 考勤数据表

| **主键（id）** | **订阅者ID（**subscribe\_id**）** | **企业ID（**corp\_id**）** | **业务ID（**biz\_id**）** | **业务类型（**biz\_type**）** | 说明 |
| --- | --- | --- | --- | --- | --- |
| 67 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=67的数据格式解释 | 67 | 钉钉假期相关回调事件 |
| 152 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=152的数据格式解释 | 152 | 考勤组数据变更事件 |
| 153 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=153的数据格式解释 | 153 | 班次数据变更事件 |

## biz\_type=67

当biz\_type=67时，数据为钉钉假期相关数据

该数据为企业发生假期相关的数据变更时推送，插入表open\_sync\_biz\_data中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 第三方企业应用的suiteid加下划线0。 |
| corp\_id | 开通第三方企业应用的企业corpId。 |
| biz\_id | 加班转调休事件：`${无业务含义的id}:${userId}:${workDate}`，workDate的格式为yyyyMMdd，如20210312。 |
| biz\_type | 67，为固定值，标识该消息为钉钉假期相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data各数据格式如下。

- 加班转调休假事件（新增、更新时会触发同步）

  ```
  {
      "syncAction": "overtime_to_vacation_data",
      "corpId": "ding33f33xxxx",
      "userId": "33506665005555",
      "workDate": "20210311",
      "overtimeDayType": "restDay",
      "overtimeDay": 0.262,
      "overtimeHour": 2.1,
      "workHoursPerDay": 8,
      "vacationRate": 2,
      "leaveCode": "c1f772d2-xxxx-407e-816a-55be5c245569",
      "startTime": 1615392000000,
      "endTime": 1640966399000,
      "delayEndTime": 1640966399000
  }
  ```

> **[!NOTE]**
>
> 数据业务唯一性约束为 ${corpId}+${userId}+${workDate}，同一个员工一天内可能会触发多次数据同步，但是应以当天最后一次同步的数据为准（例如：重排班、修改加班申请、加班转调休规则修改等，均会触发重算逻辑，导致之前同一天已同步的数据失效）。
>
> **即**：一个员工一天只会有一条有效的加班转调休记录，不会存在2条。

字段说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | overtime\_to\_vacation\_data：加班转调休事件 |
| corpId | String | 企业的corpid。 |
| userId | String | 对应的员工id。 |
| workDate | String | 对应的工作日，格式yyyyMMdd，如：20210312。 |
| overtimeDayType | String | 加班类型：   - **workDay**：工作日加班转调休 - **restDay**：休息日加班转调休 - **holiday**：节假日加班转调休 |
| overtimeDay | Number | 加班转调休时长（以天为单位），例如：0.262。 |
| overtimeHour | Number | 加班转调休时长（以小时为单位），例如：2.1。  与overtimeDay的换算关系：overtimeDay=overtimeHour/workHoursPerDay |
| workHoursPerDay | Number | 一天的工作时长（单位：小时）。 |
| vacationRate | Number | 加班转调休的比例，即实际工作时长\*vacationRate=调休时长。 |
| leaveCode | String | 转成的调休假，对应的假期code。 |
| startTime | Long | 该假期的开始生效时间（unix时间戳）。 |
| endTime | Long | 该假期的失效时间（unix时间戳）。 |
| delayEndTime | Long | 假期的延迟失效时间（unix时间戳）。  startTime < endTime <= delayEndTime |

## biz\_type=152

当biz\_type=152时，数据为考勤组数据变更的相关数据

该数据为考勤组数据变更时推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 考勤组id。 |
| biz\_type | 固定值152，表示考勤组数据变更的相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
    "syncAction": "attend_group_change",
    "corpid": "dingxxxx",
    "name":"考勤组A",
    "action":"attend_group_delete",
    "id":11112222
}
```

字段说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | 事件类型。 |
| corpid | String | 企业corpId。 |
| name | String | 考勤组名称。 |
| action | String | 考勤组动作简要信息：   - **attend\_group\_create**：企业增加考勤组之后的简要信息。 - **attend\_group\_update**：企业修改考勤组之后的简要信息。 - **attend\_group\_delete**：企业删除考勤组之后的简要信息。 |
| id | Long | 考勤组id。 |

## biz\_type=153

当biz\_type=153时，数据为班次变更的相关数据

该数据为班次变更时推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 班次的id。 |
| biz\_type | 固定值153，表示考勤组数据变更的相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
    "syncAction": "attend_shift_change",
    "corpid": "dingxxxx",
    "name":"班次A",
    "action":"attend_shift_delete",
    "id":11112222
}
```

字段说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | 事件类型。 |
| corpid | String | 企业corpId。 |
| name | String | 班次名称。 |
| action | String | 班次动作简要信息：   - **attend\_shift\_create**：企业增加班次之后的简要信息。 - **attend\_shift\_update**：企业修改班次之后的简要信息。 - **attend\_shift\_delete**：企业删除班次之后的简要信息。 |
| id | Long | 班次id。 |
