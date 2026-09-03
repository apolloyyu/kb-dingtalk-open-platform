# 获取用户属性可见性设置

doc_id: UeUsWt9n3q
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/contact/staffAttributes/visibilitySettings
api_version: v2-new
app_types: 第三方企业应用
permissions: Contact.ReachableRule.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: nextToken(Long), maxResults(Integer)

## Body
- none

## Returns
- optional: hasMore(Boolean), nextCursor(Long), list(Array), id(Long), gmtCreate(String), gmtModified(String), name(String), description(String), objectStaffIds(Array of String), objectDeptIds(Array of Long), objectTagIds(Array of Long), hideFields(Array of String), excludeStaffIds(Array of String), excludeDeptIds(Array of Long), excludeTagIds(Array of Long), active(Boolean)

## Limits
- 分页大小，最大支持100。

source_url: https://open.dingtalk.com/document/development/pull-hidden-property-field-for-enterprise-employees
updated_at: 2026-06-02 09:18:12
