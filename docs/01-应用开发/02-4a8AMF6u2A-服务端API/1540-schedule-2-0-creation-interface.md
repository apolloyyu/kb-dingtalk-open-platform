---
title: "创建日程"
source_url: "https://open.dingtalk.com/document/development/schedule-2-0-creation-interface"
namespace: "development"
slug: "schedule-2-0-creation-interface"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 协同办公 > 日程 > 创建日程"
doc_id: "djQH516y78"
updated_at: "2026-08-25 09:38:04"
---

> Source: https://open.dingtalk.com/document/development/schedule-2-0-creation-interface
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 协同办公 > 日程 > 创建日程
> Updated: 2026-08-25 09:38:04

# 创建日程

调用创建日程接口可以将企业员工的待办事项写入到钉钉日历并在钉钉日历中展示。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[创建日程](0250-create-schedule.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/calendar/v2/event/create`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| event | Event | 是 |  | 日程创建对象。 |
| attendees | Attendee[] | 是 |  | 日程参与者，参与者最大人数为100，包括组织者。 |
| userid | String | 是 | manager8037 | 参与日程的员工userid。 |
| calendar\_id | String | 是 | primary | 目前只能传primary，表示创建的日程在“我的日程”下。 |
| description | String | 否 | 请积极发言 | 日程描述。 |
| end | DateTime | 是 |  | 结束时间。 |
| date | String | 否 | 2019-09-15 | 日期，全天日程时使用，格式必须为'yyyy-mm-dd'，和timestamp字段互斥，该字段有值时，则忽略timestamp字段。 |
| timestamp | Number | 否 | 1570781196 | 时间戳，**单位为秒**。  非全天日程时使用，与date字段互斥。 |
| timezone | String | 否 | Asia/Shanghai | 时区信息，默认为"Asia/Shanghai"。date有值时，timezone为UTC。 |
| organizer | Attendee | 是 |  | 日程组织者信息。 |
| userid | String | 否 | manager8037 | 组织者userid。 |
| start | DateTime | 是 |  | 开始时间。 |
| date | String | 否 | 2019-09-15 | 日期，全天日程时使用，格式必须为'yyyy-mm-dd'，和timestamp字段互斥，该字段有值时，则忽略timestamp字段。 |
| timestamp | Number | 否 | 1570781196 | 时间戳，**单位为秒**。  非全天日程时使用，与date字段互斥。 |
| timezone | String | 否 | Asia/Shanghai | 时区信息，默认为"Asia/Shanghai"。date有值时，timezone 为 UTC。 |
| summary | String | 是 | 晨会 | 日程主题。 |
| reminder | OpenCalendarReminderVo | 否 |  | 会议开始前提醒。 |
| method | String | 否 | app | 提醒方式：   - app表示应用内提醒 |
| minutes | Number | 否 | 0 | 开始前提醒的分钟数，有效值为：0，5，15，30，60，1440。 |
| location | LocationVo | 否 |  | 地址信息。 |
| latitude | String | 否 | 30.285228 | 纬度。 |
| longitude | String | 否 | 120.017022 | 经度。 |
| place | String | 否 | 未来park | 地址详情。 |
| notification\_type | String | 否 | NONE | 受限字段，仅支持传NONE或者APP。 |
| agentid | Number | 是 | 1212 | 应用对应的AgentId。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Event |  | 日程对象。 |
| attendees | Attendee[] |  | 日程参与者。 |
| userid | String | manager8037 | 参与者员工userid。 |
| calendar\_id | String | primary | primary表示创建的日程在“我的日程”下。 |
| description | String | 请积极发言 | 日程描述。 |
| end | DateTime |  | 结束时间。 |
| date | String | 2020-09-09 | 日程结束日期。 |
| timestamp | Number | 1599613200 | 时间戳，**单位为秒**。非全天日程使用，与date字段互斥。 |
| timezone | String | Asia/Shanghai | 时区信息，默认为"Asia/Shanghai"。date有值时，timezone 为UTC。 |
| event\_id | String | 053E8ACBA1D0C7706D602509E0B3A1FE | 日程ID。 |
| organizer | Attendee |  | 日程组织者信息。 |
| userid | String | manager8037 | 组织者userid。 |
| start | DateTime |  | 开始时间。 |
| date | String | 2019-09-15 | 开始日期。  全天日程时和timestamp字段互斥，该字段有值时，则忽略timestamp字段。 |
| timestamp | Number | 1570781196 | 时间戳，单位为秒。非全天日程使用，与date字段互斥。 |
| timezone | String | Asia/Shanghai | 时区信息，默认为"Asia/Shanghai"。date有值时，timezone为 UTC。 |
| summary | String | 晨会 | 日程主题。 |
| reminder | OpenCalendarReminderVo |  | 会议开始前提醒。 |
| method | String | app | 提醒方式：   - .app表示应用内提醒 |
| minutes | Number | 5 | 会议开始前多少分钟提醒。 |
| location | LocationVo |  | 地址。 |
| latitude | String | 30.285228 | 纬度。 |
| longitude | String | 120.285228 | 经度。 |
| place | String | 未来park | 地址。 |
| notification\_type | String | NONE | 提醒方式。 |
| success | Boolean | true | 是否成功。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | zbbs6uxpei1r | 请求ID。 |
| errmsg | String | ok | 返回的错误信息。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/calendar/v2/event/create?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "agentid": "923680251",
  "event": {
    "summary": "夕会",
    "notification_type": "NONE",
    "calendar_id": "primary",
    "description": "这是一个测试的日程啊",
    "reminder": {
      "method": "app",
      "minutes": "5"
    },
    "attendees": [
      {
        "userid": "user123"
      },
      {
        "userid": "user456"
      }
    ],
    "organizer": {
      "userid": "user456"
    },
    "start": {
      "timezone": "Asia/Shanghai",
      "timestamp": "1605696900"
    },
    "end": {
      "timezone": "Asia/Shanghai",
      "timestamp": "1605709800"
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
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/calendar/v2/event/create");
OapiCalendarV2EventCreateRequest req = new OapiCalendarV2EventCreateRequest();
Event obj1 = new Event();
List<Attendee> list3 = new ArrayList<Attendee>();
Attendee obj4 = new Attendee();
list3.add(obj4);
obj4.setUserid("user456");
obj1.setAttendees(list3);
obj1.setCalendarId("primary");
obj1.setDescription("这是一个测试的日程啊");
DateTime obj5 = new DateTime();
// obj5.setDate("2019-09-15");
obj5.setTimestamp(1570781196L);
obj5.setTimezone("Asia/Shanghai");
obj1.setEnd(obj5);
Attendee obj6 = new Attendee();
obj6.setUserid("user123");
obj1.setOrganizer(obj6);
DateTime obj7 = new DateTime();
// obj7.setDate("2019-09-15");
obj7.setTimestamp(1570781196L);
obj7.setTimezone("Asia/Shanghai");
obj1.setStart(obj7);
obj1.setSummary("夕会");
OpenCalendarReminderVo obj8 = new OpenCalendarReminderVo();
obj8.setMethod("app");
obj8.setMinutes(5L);
obj1.setReminder(obj8);
LocationVo obj9 = new LocationVo();
obj9.setLatitude("30.285228");
obj9.setLongitude("120.017022");
obj9.setPlace("未来park");
obj1.setLocation(obj9);
obj1.setNotificationType("NONE");
req.setEvent(obj1);
req.setAgentid(923680251L);
OapiCalendarV2EventCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": {
    "attendees": [
      {
        "userid": "user123"
      },
      {
        "userid": "user456"
      }
    ],
    "calendar_id": "primary",
    "description": "这是一个测试的日程啊",
    "end": {
      "timestamp": 1605709800,
      "timezone": "Asia/Shanghai"
    },
    "event_id": "387FB2xxxxxxD085",
    "location": {
      "latitude": "30.285228",
      "longitude": "120.017022",
      "place": "未来park"
    },
    "notification_type": "NONE",
    "organizer": {
      "userid": "user456"
    },
    "reminder": {
      "method": "app",
      "minutes": 5
    },
    "start": {
      "timestamp": 1605696900,
      "timezone": "Asia/Shanghai"
    },
    "summary": "夕会"
  },
  "success": true,
  "request_id": "5c4kit4r67me"
}
```

## 错误码

| 错误码 | 说明 | 解决方案 |
| --- | --- | --- |
| 856010 | 必填项错误 | 请仔细检查遗漏参数。 |
| 856011 | 格式化全天日程失败 | 全天日程格式必须为“yyyy-mm-dd”。 |
| 856012 | 开始结束日期不匹配。例如：开始日期是全天格式，但是结束日期不是全天格式 | 请检查开始时间和结束时间是否匹配，请求参数**date**和**timestamp**互斥。 |
| 856013 | 开始日期大于结束日期 | 请检查设置的开始时间和结束时间。 |
| 856014 | 开始时间等于结束时间 | 请检查设置的开始时间和结束时间。 |
| 856015 | 非法的event\_id | 请检查event\_id是否正确。 |
| 856016 | 非法的app\_id | 请检查app\_id是否正确。 |
| 856017 | 非法的userid | 请检查userid是否正确。 |
| 856018 | 非法的agentId | 检查agentid字段是否为空，是否真实存在。 |
| 856019 | 获取open senderId异常 | 请使用应用的Appkey和AppSecret获取access\_token，再次发送请求。 |
