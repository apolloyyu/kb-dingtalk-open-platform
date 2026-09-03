# 创建订阅日历

doc_id: P9NKhxPeYy
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/subscribedCalendars
api_version: v2-new
app_types: 第三方个人应用
permissions: Calendar.Calendar.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。 - 第三方个人应用，调用获取用户token接口获取。

## Path params
- userId (String, required): 日历创建者的unionId。 - 企业内部应用和第三方企业应用，调用查询用户详情接口获取unionid参数值。 - 第三方个人应用，调用获取用户通讯录个人信息接口获取unionId参数值。

## Query params
- none

## Body
- name (String, required): 订阅日历的名称。
- subscribeScope (Object, required): 可订阅该日历的对象。
- optional: description(String), managers(Array of String), unionIds(Array of String), openConversationIds(Array of String), corpIds(Array of String)

## Returns
- optional: calendarId(String)

## Limits
- 订阅日历的描述，最大长度1024字符。

source_url: https://open.dingtalk.com/document/development/create-subscription-calendar
updated_at: 2026-06-01 18:08:34
