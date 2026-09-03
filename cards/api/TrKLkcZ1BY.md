# 创建访问控制

doc_id: TrKLkcZ1BY
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/calendars/{calendarId}/acls
api_version: v2-new
app_types: 第三方个人应用
permissions: Calendar.Acl.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方个人应用，调用获取用户token接口获取。

## Path params
- userId (String, required): 日程组织者的unionId。 - 企业内部应用，调用查询用户详情接口获取unionid参数值。 - 第三方个人应用，通过获取用户通讯录个人信息接口获取unionId参数值。
- calendarId (String, required): 日程所属的日历ID，统一为primary，表示用户的主日历。

## Query params
- none

## Body
- privilege (String, required): 权限信息，取值： - **free_busy_reader**：查看忙闲 - **title_reader**：查看标题 - **reader**：查看详情 - **writer**：创建和编辑
- sendMsg (Boolean, required): 是否向授权人发消息。 - **true**：发 - **false**：不发
- scope (Object, required): 权限范围。
- scopeType (String, required): 权限类型，目前只支持**user**表示用户。
- userId (String, required): 用户ID。当**scopeType**取值为**user**时，传入用户的**unionId**。 **[!NOTE]** 单人最多添加500个共享人 。

## Returns
- optional: privilege(String), aclId(String), scope(Object), scopeType(String), userId(String)

## Limits
- 用户ID。当**scopeType**取值为**user**时，传入用户的**unionId**。 **[!NOTE]** 单人最多添加500个共享人 。

source_url: https://open.dingtalk.com/document/development/create-schedule-access-control
updated_at: 2026-06-02 09:24:54
