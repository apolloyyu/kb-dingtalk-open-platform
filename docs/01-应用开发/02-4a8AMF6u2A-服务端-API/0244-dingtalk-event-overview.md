---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/dingtalk-event-overview"
namespace: "development"
slug: "dingtalk-event-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "日程 > 概述"
doc_id: "AhlZFjMuuX"
updated_at: "2026-07-02 10:36:17"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-event-overview
> Path: 应用开发 / 服务端 API / 日程 > 概述
> Updated: 2026-07-02 10:36:17

# 概述

本文介绍了日程产品，如何开通日程，日程开放了哪些接口能力，以及如何接入日程能力。

## 什么是日程

钉钉日程管理与即时沟通深度结合，同事间共享日程，便捷发起日程会议，重要事情一目了然，团队协作更高效，给员工良好的使用体验。更多介绍请参见[钉钉使用手册-日程](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Y7kmbOpyEdYLGLq2?dontjump=true%23%23)。

### 日程会议精确通知

一键轻松创建会议日程，邀约直接以聊天形式通知到每个与会人员，确保万无一失。

![日程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7779592871/p433288.png)

### 统一查看日程安排

打通阿里邮箱，在钉钉日历里统一查看和编辑，一处更新，处处同步，不错过任何会议或安排。![日程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7779592871/p433289.png)

## 如何开通日程

手机端操作方式：【协作】-【日历】或工具栏中【日历】。

![日程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7779592871/p433291.png)

电脑端操作方式：【日历】

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7779592871/p523339.png)

## 开放概览

### 开放接口列表

日程提供了丰富的接口开放能力，开发者通过API接口可以实现日程和企业业务系统打通。

> **[!NOTE]**
>
> - [创建日程](0250-create-schedule.md)、[修改日程](0252-modify-event.md)、[添加日程参与者](0256-add-schedule-participant.md)和[删除日程参与者](0257-delete-schedule-participant.md)接口，每次日程参与者操作最大支持500人，最大支持操作5000人的日程。
> - 日程参与者的添加和删除，建议使用[添加日程参与者](0256-add-schedule-participant.md)和[删除日程参与者](0257-delete-schedule-participant.md)接口。

#### **用户访问控制**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建访问控制](0247-create-schedule-access-control.md) | 给指定日历添加访问控制。 | 新版 |
| [删除访问控制](0248-delete-an-access-control-list.md) | 删除访问控制。 | 新版 |
| [获取访问控制列表](0249-obtain-the-access-control-list-of-the-calendar.md) | 获取日历访问控制列表。 | 新版 |

#### **日程**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建日程](0250-create-schedule.md) | 创建一个日程。 | 新版 |
| [删除日程](0251-delete-event.md) | 删除指定日程。 | 新版 |
| [修改日程](0252-modify-event.md) | 修改单个日程信息。 | 新版 |
| [查询单个日程详情](0253-query-details-about-an-event.md) | 查询单个日程详情。 | 新版 |
| [查询日程列表](0254-query-an-event-list.md) | 查询一个用户给定时间范围内的日程。 | 新版 |
| [查询日程视图](0255-query-schedule-view.md) | 查询用户的钉钉主日历在某时间范围内的日程视图。 | 新版 |

#### **日程参与者**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [添加日程参与者](0256-add-schedule-participant.md) | 添加日程参与者。 | 新版 |
| [删除日程参与者](0257-delete-schedule-participant.md) | 从日程参与者中删除指定的用户。 | 新版 |
| [获取日程参与者](0259-get-the-participants-of-a-schedule.md) | 获取日程参与者列表。 | 新版 |
| [设置日程响应邀请状态](0258-configure-response-status.md) | 设置日程响应邀请状态。 | 新版 |

#### **忙闲**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取用户忙闲信息](0260-free-schedule.md) | 查询指定用户列表在指定时间内的忙闲信息。 | 新版 |

#### **日历**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [查询日历](0261-query-a-calendar.md) | 调用本接口查询用户日历。 | 新版 |
| [订阅公共日历](0262-subscribe-to-a-public-calendar.md) | 调用本接口订阅公共日历。 | 新版 |
| [取消订阅公共日历](0263-unsubscribe-from-a-public-calendar.md) | 调用本接口，取消订阅公共日历。 | 新版 |
| [创建订阅日历](0264-create-subscription-calendar.md) | 调用本接口创建订阅日历。 | 新版 |
| [查询单个订阅日历详情](0265-query-a-single-subscription-calendar.md) | 调用本接口查询订阅日历的详情信息。 | 新版 |
| [更新订阅日历](0266-update-subscription-calendar.md) | 调用本接口更新单个订阅日历信息。 | 新版 |
| [删除订阅日历](0267-delete-subscription-calendar.md) | 调用本接口删除订阅日历。 | 新版 |

#### **签到**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [查看单个日程的签到详情](0268-view-the-check-in-details-of-a-single-schedule.md) | 调用本接口，查看单个日程的签到详情。 | 新版 |
| [针对单个日程进行签到](0270-sign-in-single-schedule-news.md) | 根据日程ID对指定日程进行签到。 | 新版 |
| [针对单个日程进行签退](0271-sign-off-for-a-single-schedule.md) | 根据日程ID对指定日程进行签退。 | 新版 |
| [查看单个日程的签退详情](0269-view-the-billing-details-of-a-single-schedule.md) | 根据日程ID查询单个日程签到与未签到人员列表。 | 新版 |
| [获取签到链接](0272-api-getsigninlink.md) | 通过日历 ID、用户 unionId和日程 eventId，查询签到链接。 | 新版 |
| [获取签退链接](0273-api-getsignoutlink.md) | 通过日历 ID、用户 unionId和日程 eventId，查询签退链接。 | 新版 |

#### **会议室**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取会议室忙闲信息](0274-queries-free-and-busy-meeting-room-information.md) | 获取会议室忙闲信息。 | 新版 |
| [预定会议室](0275-add-a-meeting-room.md) | 预定会议室。 | 新版 |
| [取消预定会议室](0276-remove-a-meeting-room.md) | 取消预定会议室。 | 新版 |

### 回调事件列表

日程支持用户发生[日程变更](../04-LFcRvVD08N-事件订阅/0018-event-calendar-event-change.md)的回调事件。

## 使用教程

钉钉提供了创建及删除日程、日程参与者等常用场景的使用流程示例：

- [创建、修改、查询及删除日程](0245-create-and-delete-an-event.md)
- [添加、获取及删除日程参与者](0246-calendar-participant-process.md)

## 名词解释

| 权限值 | 说明 |
| --- | --- |
| **free\_busy\_reader** | 查看忙闲 |
| **title\_reader** | 查看标题 |
| **reader** | 查看详情 |
| **writer** | 创建和编辑 |

## **资源定义**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| id | String | 日程的全局唯一ID。 |
| summary | String | 日程标题。 |
| description | String | 日程描述。 |
| start | Object | 日程开始时间。 |
| start.date | String | 日程开始日期，格式：yyyy-MM-dd。如果是全天日程必须有值，非全天日程必须留空。 |
| start.dateTime | String | 日程开始时间，格式为ISO-8601的date-time格式。非全天日程必须有值，全天日程必须留空。 |
| start.timeZone | String | 日程开始时间所属时区。非全天日程必须有值，全天日程必须留空。 |
| end | Object | 日程结束时间。 |
| end.date | String | 日程结束日期，格式：yyyy-MM-dd。如果是全天日程必须有值，非全天日程必须留空。 |
| end.dateTime | String | 日程结束时间，格式为ISO-8601的date-time格式。非全天日程必须有值，全天日程必须留空。 |
| end.timeZone | String | 日程结束时间所属时区，必须和开始时间所属时区相同，TZ database name格式。非全天日程必须有值，全天日程必须留空。 |
| isAllDay | Boolean | 是否为全天日程。 |
| recurrence | Object | 日程循环规则。 |
| recurrence.pattern | Object | 循环规则。 |
| recurrence.pattern.type | String | 循环规则类型：   - **daily**：每`interval`天重复 - **weekly**：每`interval`周的第`daysOfWeek`天重复 - **absoluteMonthly**：每`interval`月的第`dayOfMonth`天重复 - **relativeMonthly**：每`interval`月的第`index`周的第`daysOfWeek`天重复 - **absoluteYearly**：每`interval`年重复 |
| recurrence.pattern.dayOfMonth | Integer | 当`type=absoluteMonthly`时，用于指定是每个月的第几天。 |
| recurrence.pattern.daysOfWeek | String | 英文小写单词指定星期几，如果有多个值逗号分割。 |
| recurrence.pattern.index | String | 当`type=relativeMonthly`时，用于指定每月第几周：   - **first** - **second** - **third** - **fourth** - **last**   其中`last`表示当月的最后一周。 |
| recurrence.pattern.interval | Integer | 循环间隔，根据type不同单位不同。例如当`type=daily`时表示间隔N天，`type=absoluteYearly`则表示间隔N年。 |
| recurrence.range | Object | 循环范围。 |
| recurrence.range.type | String | 循环范围类型：   - **noEnd**：永不结束 - **endDate**：循环至指定日期结束 - **numbered**：循环指定次数后结束 |
| recurrence.range.endDate | String | 循环结束时间。 |
| recurrence.range.numberOfOccurrences | Integer | 循环次数。 |
| attendees | Array | 日程参与人列表。 |
| attendees.id | String | 用户的unionId。 |
| attendees.displayName | String | 用户姓名。 |
| attendees.responseStatus | String | 参会人状态：   - **needsAction**：未操作（默认状态） - **accepted**：已接受 - **declined**：已拒绝 - **tentative**：暂定接受 |
| attendees.self | Boolean | 是否当前操作用户。 |
| organizer | Object | 日程组织者。 |
| organizer.id | String | 组织者unionId。 |
| organizer.displayName | String | 组织者用户名。 |
| organizer.responseStatus | String | 组织者的回复状态。 |
| organizer.self | Boolean | 是否当前用户。 |
| location | Object | 日程地点。 |
| location.displayName | String | 地点名称。 |
| reminders | Array | 日程提醒。 |
| reminders.method | String | 提醒方式：   - **dingtalk**：应用内提醒 - **sms**：短信提醒 - **phone**：电话提醒 |
| reminders.minutes | String | 提前多久提醒，单位分钟。 |
| onlineMeetingInfo | Object | 创建日程同时创建线上会议。 |
| onlineMeetingInfo.type | String | 线上会议类型：   - **dingtalk**: 钉钉视屏会议 |
| onlineMeetingInfo.conferenceId | String | 会议id。 |
| onlineMeetingInfo.url | String | 参会url。 |
| onlineMeetingInfo.extraInfo | Map | 其他扩展信息。 |
| seriesMasterId | String | 重复日程的主日程id，非重复日程为空。 |
| createTime | String | 创建时间。 |
| updateTime | String | 更新时间。 |
| status | String | 日程状态：   - **confirmed**：正常 - **cancelled**：已取消 |
