# 查看单个日程的签退详情

doc_id: qiC4k0QsjB
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/events/{eventId}/signOut
api_version: v2-new
app_types: 第三方个人应用
permissions: Calendar.Event.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。 - 第三方个人应用，调用获取用户token接口获取。

## Path params
- userId (String, required): 本次请求的资源所归属的用户unionId，该用户需要为请求日程的组织者和日程的参与者。 - 企业内部应用和第三方企业应用，调用查询用户详情接口获取unionid参数值。 - 第三方个人应用，调用获取用户通讯录个人信息接口获取unionId参数值。
- calendarId (String, required): 日程所属的日历ID，参数填写为primary，表示用户的主日历。
- eventId (String, required): 日程ID，可调用查询日程列表接口获取id参数值。

## Query params
- maxResults (Integer, required): 查询返回结果数，最大值500。
- type (String, required): 签退信息类型。 - **sign_out**：已签退 - **not_yet_sign_out**：未签退
- optional: nextToken(String)

## Body
- none

## Returns
- optional: nextToken(String), users(Array), userId(String), displayName(String), checkOutTime(Long)

## Limits
- 查询返回结果数，最大值500。

source_url: https://open.dingtalk.com/document/development/view-the-billing-details-of-a-single-schedule
updated_at: 2026-06-02 09:25:12
