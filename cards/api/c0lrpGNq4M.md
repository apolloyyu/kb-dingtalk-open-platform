# 获取访问控制列表

doc_id: c0lrpGNq4M
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/acls
api_version: v2-new
app_types: 第三方个人应用
permissions: Calendar.Acl.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方个人应用，调用获取用户token接口获取。

## Path params
- userId (String, required): 日程组织者的unionId。 - 企业内部应用，调用查询用户详情接口获取unionid参数值。 - 第三方个人应用，通过获取用户通讯录个人信息接口获取unionId参数值。
- calendarId (String, required): 日程所属的日历ID，统一为primary，表示用户的主日历。

## Query params
- none

## Body
- none

## Returns
- optional: acls(Array), privilege(String), aclId(String), scope(Object), userId(String), scopeType(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-access-control-list-of-the-calendar
updated_at: 2026-06-02 09:24:56
