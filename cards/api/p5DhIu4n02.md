# 订阅公共日历

doc_id: p5DhIu4n02
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/subscribe
api_version: v2-new
app_types: 第三方个人应用
permissions: Calendar.Calendar.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。 - 第三方个人应用，调用获取用户token接口获取。

## Path params
- userId (String, required): 订阅者的unionId。 - 企业内部应用和第三方企业应用，调用查询用户详情接口获取unionid参数值。 - 第三方个人应用，调用获取用户通讯录个人信息接口获取unionId参数值。
- calendarId (String, required): 日历ID，目前订阅操作仅支持日历类型为**subscribed**的日历。 订阅日历的创建者或已订阅日历的人员可通过查询日历接口获取。

## Query params
- none

## Body
- none

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/subscribe-to-a-public-calendar
updated_at: 2026-06-02 09:25:08
