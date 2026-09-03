# 删除用户属性可见性设置

doc_id: aVeU6xGcMh
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/contact/staffAttributes/visibilitySettings/{settingId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Contact.ReachableRule.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- settingId (Long, required): 设置的ID，可通过设置用户属性可见性接口获取id参数值。

## Query params
- none

## Body
- none

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-enterprise-employee-attribute-field-visibility-settings
updated_at: 2026-06-02 09:18:10
