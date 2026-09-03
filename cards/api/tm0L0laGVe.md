# 新增或更新通讯录隐藏设置

doc_id: tm0L0laGVe
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/contact/contactHideSettings
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
- optional: name(String), description(String), objectStaffIds(Array of String), objectDeptIds(Array of Long), objectTagIds(Array of Long), excludeStaffIds(Array of String), excludeDeptIds(Array of Long), excludeTagIds(Array of Long), active(Boolean), id(Long), hideInUserProfile(Boolean), hideInSearch(Boolean)

## Returns
- optional: result(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/update-address-book-hide-settings
updated_at: 2026-06-02 09:24:43
