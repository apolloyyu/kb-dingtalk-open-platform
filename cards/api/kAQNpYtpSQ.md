# 获取通讯录隐藏设置

doc_id: kAQNpYtpSQ
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/contact/contactHideSettings
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
- optional: hasMore(Boolean), nextToken(Long), list(Array), name(String), description(String), objectStaffIds(Array of String), objectDeptIds(Array of Long), objectTagIds(Array of Long), excludeStaffIds(Array of String), excludeDeptIds(Array of Long), excludeTagIds(Array of Long), active(Boolean), id(Long)

## Limits
- 分页大小，最大值100。

source_url: https://open.dingtalk.com/document/development/obtains-the-hide-settings-of-the-address-book
updated_at: 2026-06-01 16:21:32
