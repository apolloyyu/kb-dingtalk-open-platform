# 修改日程

doc_id: jlKI98IAns
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/calendar/v2/event/update
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- event (Event, required): 日程创建对象。
- calendar_id (String, required): 日历ID。 目前仅支持传**primary**表示修改当前用户“我的日程”下的日程。
- description (String, required): 日程描述。
- end (DateTime, required): 结束时间。
- start (DateTime, required): 开始时间。
- summary (String, required): 日程主题。
- event_id (String, required): 日程ID。
- optional: attendees(Attendee[]), userid(String), attendee_status(String), date(String), timestamp(Number), timezone(String), reminder(OpenCalendarReminderVo), method(String), minutes(Number), location(LocationVo), latitude(String), longitude(String), place(String), agentid(Number)

## Returns
- optional: success(Boolean), errcode(Number), request_id(String), errmsg(String)

## Limits
- 日程参与者，参与人数最多100人，包括组织者。 如果通过该接口新增或删除参会人，则该字段必填。
- > - 只能修改通过创建日程接口创建的日程。

source_url: https://open.dingtalk.com/document/development/schedule-2-0-modify-schedule
updated_at: 2026-08-25 09:38:05
