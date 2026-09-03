# 查询日历

doc_id: G6AvqKZXRK
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars
api_version: v2-new
app_types: 第三方个人应用
permissions: Calendar.Event.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。 - 第三方个人应用，调用获取用户token接口获取。

## Path params
- userId (String, required): 查询目标用户的unionId。 - 企业内部应用和第三方企业应用，调用查询用户详情接口获取unionid参数值。 - 第三方个人应用，调用获取用户通讯录个人信息接口获取unionId参数值。

## Query params
- none

## Body
- none

## Returns
- optional: response(Object), calendars(Array), id(String), summary(String), description(String), timeZone(String), eTag(String), type(String), privilege(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-a-calendar
updated_at: 2026-06-02 09:25:08
