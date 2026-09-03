# 删除日程

doc_id: nFrliSK0U4
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/events/{eventId}
api_version: v2-new
app_types: 第三方个人应用
permissions: Calendar.Event.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。 - 第三方个人应用，调用获取用户token接口获取。
- optional: x-client-token(String)

## Path params
- userId (String, required): 期望删除的日程所属的用户uninoId。 - 企业内部应用和第三方企业应用，调用查询用户详情接口获取unionid参数值。 - 第三方个人应用，调用获取用户通讯录个人信息接口获取unionId参数值。
- calendarId (String, required): 日程所属的日历ID，统一为primary，表示用户的主日历。
- eventId (String, required): 日程ID，可调用创建日程接口或查询日程列表接口获取id参数值。

## Query params
- optional: pushNotification(Boolean)

## Body
- none

## Returns
- none

## Limits
- 幂等校验。 - 相同的`x-client-token`表示同一次请求。 - 过期失效，1天。

source_url: https://open.dingtalk.com/document/development/delete-event
updated_at: 2026-06-02 09:24:58
