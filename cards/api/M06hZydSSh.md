# 设置部门可见性优先级

doc_id: M06hZydSSh
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/contact/depts/settings/priorities
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
- enable (Boolean, required): 是否开启子部门设置优先，取值： - **true**: 子部门设置优先于父部门 - **false(默认值)**: 父部门设置优先于子部门

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/set-address-book-visibility-sub-department-settings-to-take-precedence
updated_at: 2026-06-01 16:21:33
