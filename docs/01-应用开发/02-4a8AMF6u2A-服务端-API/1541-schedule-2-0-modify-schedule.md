---
title: "修改日程"
source_url: "https://open.dingtalk.com/document/development/schedule-2-0-modify-schedule"
namespace: "development"
slug: "schedule-2-0-modify-schedule"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 协同办公 > 日程 > 修改日程"
doc_id: "jlKI98IAns"
updated_at: "2026-08-25 09:38:05"
---

> Source: https://open.dingtalk.com/document/development/schedule-2-0-modify-schedule
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 协同办公 > 日程 > 修改日程
> Updated: 2026-08-25 09:38:05

# 修改日程

调用该接口修改日程。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[修改日程](0252-modify-event.md)接口，已接入用户不受影响。

> **[!NOTE]**
>
> 本接口使用说明：
>
> - 只能修改通过[创建日程](1540-schedule-2-0-creation-interface.md)接口创建的日程。
> - 确保已经申请了[修改日程参与者](1542-schedule-2-0-participant-modification.md)接口权限。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/calendar/v2/event/update`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| event | Event | 是 |  | 日程创建对象。 |
| attendees | Attendee[] | 否 |  | 日程参与者，参与人数最多100人，包括组织者。  如果通过该接口新增或删除参会人，则该字段必填。 |
| userid | String | 否 | manager8037 | 日程参与者userid。  必须与**attendee\_status**同时设置。 |
| attendee\_status | String | 否 | add | 添加或者删除状态：   - add: 添加参会者 - remove：删除参会者   必须与**userid**同时设置。 |
| calendar\_id | String | 是 | primary | 日历ID。  目前仅支持传**primary**表示修改当前用户“我的日程”下的日程。 |
| description | String | 是 | 请积极发言 | 日程描述。 |
| end | DateTime | 是 |  | 结束时间。 |
| date | String | 否 | 2019-09-15 | 日期，全天日程时使用，格式必须为'yyyy-mm-dd'，和timestamp字段互斥，该字段有值时，则忽略timestamp字段。 |
| timestamp | Number | 否 | 1570846303 | 时间戳，单位为秒。非全天日程使用，与date字段互斥。 |
| timezone | String | 否 | Asia/Shanghai | 时区信息，默认为"Asia/Shanghai"。date有值时，timezone为UTC。 |
| start | DateTime | 是 |  | 开始时间。 |
| date | String | 否 | 2019-09-15 | 日期，全天日程时使用，格式必须为'yyyy-mm-dd'，和timestamp字段互斥，该字段有值时，则忽略timestamp字段。 |
| timestamp | Number | 否 | 1570846303 | 时间戳，单位为秒。  非全天日程时使用，与date字段互斥。 |
| timezone | String | 否 | Asia/Shanghai | 时区信息，默认为"Asia/Shanghai"。date有值时，timezone 为UTC。 |
| summary | String | 是 | 晨会 | 日程主题。 |
| event\_id | String | 是 | 053E8Axxxx | 日程ID。 |
| reminder | OpenCalendarReminderVo | 否 |  | 会议开始前提醒。 |
| method | String | 否 | app | 提醒方式：   - .app表示应用内提醒。 |
| minutes | Number | 否 | 5 | 开始前提醒的分钟数，有效值为：0，5，15，30，60，1440。 |
| location | LocationVo | 否 |  | 地址信息。 |
| latitude | String | 否 | 30.285228 | 纬度。 |
| longitude | String | 否 | 120.017022 | 经度。 |
| place | String | 否 | 未来park | 地址详情。 |
| agentid | Number | 否 | 1212 | 应用对应的AgentId。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 是否成功。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | zbbs6uxpei1r | 请求ID。 |
| errmsg | String | ok | 返回码描述。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/calendar/v2/event/update?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "agentid": "923680251",
  "event": {
    "event_id": "5E6355BC9BA7D5576D602509E0B3A1FE",
    "summary": "夕会",
    "calendar_id": "primary",
    "description": "这是一个测试的日程呀",
    "attendees": [
      {
        "userid": "user123",
        "attendee_status": "remove"
      }
    ],
    "reminder": {
      "method": "app",
      "minutes": "5"
    },
    "organizer": {
      "userid": "user123"
    },
    "start": {
      "timezone": "Asia/Shanghai",
      "timestamp": 1605699000
    },
    "end": {
      "timezone": "Asia/Shanghai",
      "timestamp": 1605709800
    },
    "location": {
      "latitude": "30.285228",
      "place": "未来park",
      "longitude": "120.017022"
    }
  }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/calendar/v2/event/update");
OapiCalendarV2EventUpdateRequest req = new OapiCalendarV2EventUpdateRequest();
Event obj1 = new Event();
List<Attendee> list3 = new ArrayList<Attendee>();
Attendee obj4 = new Attendee();
list3.add(obj4);
obj4.setUserid("user123");
obj4.setAttendeeStatus("remove");
obj1.setAttendees(list3);
obj1.setCalendarId("primary");
obj1.setDescription("这是一个测试的日程呀");
DateTime obj5 = new DateTime();
// obj5.setDate("2019-09-15");
obj5.setTimestamp(1570846303L);
obj5.setTimezone("Asia/Shanghai");
obj1.setEnd(obj5);
Attendee obj6 = new Attendee();
obj6.setUserid("user123");
obj1.setOrganizer(obj6);
DateTime obj7 = new DateTime();
// obj7.setDate("2019-09-15");
obj7.setTimestamp(1570846303L);
obj7.setTimezone("Asia/Shanghai");
obj1.setStart(obj7);
obj1.setSummary("夕会");
obj1.setEventId("5E6355BC9BA7D5576D602509E0B3A1FE");
OpenCalendarReminderVo obj8 = new OpenCalendarReminderVo();
obj8.setMethod("app");
obj8.setMinutes(5L);
obj1.setReminder(obj8);
LocationVo obj9 = new LocationVo();
obj9.setLatitude("30.285228");
obj9.setLongitude("120.017022");
obj9.setPlace("未来park");
obj1.setLocation(obj9);
req.setEvent(obj1);
req.setAgentid(923680251L);
OapiCalendarV2EventUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "success": true,
  "request_id": "56pivzq01yj1"
}
```
