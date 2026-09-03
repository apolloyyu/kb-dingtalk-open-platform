# 设置用户属性可见性

doc_id: uhDRwD28Uw
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/contact/staffAttributes/visibilitySettings
api_version: v2-new
app_types: 第三方企业应用
permissions: Contact.ReachableRule.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: id(Long), name(String), description(String), objectStaffIds(Array of String), objectDeptIds(Array of Long), objectTagIds(Array of Long), hideFields(Array of String), excludeStaffIds(Array of String), excludeDeptIds(Array of Long), excludeTagIds(Array of Long), active(Boolean)

## Returns
- optional: result(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/add-or-update-the-hidden-settings-of-the-employee-property
updated_at: 2026-06-02 09:18:11
