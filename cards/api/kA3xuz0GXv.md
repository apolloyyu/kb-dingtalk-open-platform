# 获取员工组件的值

doc_id: kA3xuz0GXv
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/yida/forms/employeeFields
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Form.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: targetFieldJson(String), formUuid(String), appType(String), modifiedToTimeGMT(String), systemToken(String), modifiedFromTimeGMT(String), language(String), searchFieldJson(String), originatorId(String), userId(String), createToTimeGMT(String), createFromTimeGMT(String)

## Returns
- optional: result(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/gets-the-value-of-the-employee-component
updated_at: 2026-06-02 10:10:47
