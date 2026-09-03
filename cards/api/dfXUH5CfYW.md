# 获取限制查看通讯录设置列表

doc_id: dfXUH5CfYW
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/contact/restrictions/settings
api_version: v2-new
app_types: 企业内部应用
permissions: Contact.Visibility.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- optional: nextToken(Long), maxResults(Integer)

## Body
- none

## Returns
- optional: hasMore(Boolean), nextToken(Long), list(Array), id(Long), name(String), description(String), subjectUserIds(Array of String), subjectDeptIds(Array of Long), subjectTagIds(Array of Long), type(String), excludeUserIds(Array of String), excludeDeptIds(Array of Long), excludeTagIds(Array of Long), active(Boolean), restrictInUserProfile(Boolean), restrictInSearch(Boolean)

## Limits
- 最大返回结果数，最大值100。
- 限制类型。 - excludeNode: 只能看到白名单里的用户和部门。 - onlySelf: 只能看到自己。 - onlySelfDeptAndChild: 只能看到自己所在部门及子部门。

source_url: https://open.dingtalk.com/document/development/gets-a-list-of-address-book-limit-visibility-settings
updated_at: 2026-06-01 16:21:34
