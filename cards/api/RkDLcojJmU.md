# 设置日程响应邀请状态

doc_id: RkDLcojJmU
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/events/{eventId}/respond
api_version: v2-new
app_types: 第三方个人应用
permissions: Calendar.Event.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。 - 第三方个人应用，调用获取用户token接口获取。

## Path params
- userId (String, required): 日程参与者unionId。 - 企业内部应用和第三方企业应用，调用查询用户详情接口获取unionid参数值。 - 第三方个人应用，调用获取用户通讯录个人信息接口获取unionId参数值。
- calendarId (String, required): 日程所属的日历id，统一为primary，表示用户的主日历。
- eventId (String, required): 日程ID，可调用查询日程列表接口获取id参数值。

## Query params
- none

## Body
- responseStatus (String, required): 响应状态。 - **needsAction**（默认）：未操作 - **accepted**：已接受 - **declined**：已拒绝 - **tentative**：暂定接受

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/configure-response-status
updated_at: 2026-06-02 09:25:04
