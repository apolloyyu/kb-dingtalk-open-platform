# 删除访问控制

doc_id: XPlN3ca85W
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/acls/{aclId}
api_version: v2-new
app_types: 第三方个人应用
permissions: Calendar.Acl.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方个人应用，调用获取用户token接口获取。

## Path params
- userId (String, required): 日程组织者的unionId。 - 企业内部应用，调用查询用户详情接口获取unionid参数值。 - 第三方个人应用，通过获取用户通讯录个人信息接口获取unionId参数值。
- calendarId (String, required): 日程所属的日历ID，统一为**primary**，表示用户的主日历。
- aclId (String, required): 权限资源ID，可调用获取访问控制列表接口获取aclId参数值。

## Query params
- none

## Body
- none

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-an-access-control-list
updated_at: 2026-06-02 09:24:55
