# 删除限制查看通讯录设置

doc_id: rEsbmgUTBh
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/contact/restrictions/settings/{settingId}
api_version: v2-new
app_types: 企业内部应用
permissions: Contact.Visibility.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- settingId (Long, required): 限制规则ID，通过获取限制查看通讯录设置列表接口获取。

## Query params
- none

## Body
- none

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-visible-restrictions
updated_at: 2026-06-01 16:21:35
