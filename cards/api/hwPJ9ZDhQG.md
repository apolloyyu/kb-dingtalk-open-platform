# 新增或修改限制查看通讯录设置

doc_id: hwPJ9ZDhQG
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/contact/restrictions/settings
api_version: v2-new
app_types: 企业内部应用
permissions: Contact.Visibility.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- type (String, required): 限制类型，有以下取值： - **onlySelf**：只能查看自己，不能看自己之外的其他部门和人。 - **onlySelfDeptAndChild**：只能看到自己所在的部门及子部门，不能看到其他部门和人。 - **excludeNode**：默认值，只能看到白名单列表中的部门和人。 当该参数值为excludeNode时，设置的白名单才生效。
- optional: id(Long), name(String), description(String), subjectUserIds(Array of String), subjectDeptIds(Array of Long), subjectTagIds(Array of Long), excludeUserIds(Array of String), excludeDeptIds(Array of Long), excludeTagIds(Array of Long), active(Boolean), restrictInUserProfile(Boolean), restrictInSearch(Boolean)

## Returns
- optional: result(Long)

## Limits
- 限制类型，有以下取值： - **onlySelf**：只能查看自己，不能看自己之外的其他部门和人。 - **onlySelfDeptAndChild**：只能看到自己所在的部门及子部门，不能看到其他部门和人。 - **excludeNode**：默认值，只能看到白名单列表中的部门和人。 当该参数值为excludeNode时，设置的白名单才生效。
- > 本接口的限制查看设置与OA后台的限制查看设置是相互独立存储，最终生效结果两边的设置是或的关系。比如：同一个部门，本接口或者OA后台有任意一方设置了仅能查看自己，最终这个部门就只能查看自己。

source_url: https://open.dingtalk.com/document/development/add-or-modify-visibility-settings-for-address-book-restrictions
updated_at: 2026-06-02 09:24:45
