# 查询已设置为条件的表单组件

doc_id: uB6xY2eYXw
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/workflow/processes/conditions/components
api_version: v2-new
app_types: 第三方企业应用
permissions: Workflow.Form.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- processCode (String, required): 审批流的唯一码，调用创建或更新审批表单模板接口或OA审批概述-名词解释获取。
- optional: agentId(Long)

## Body
- none

## Returns
- optional: result(Array), id(String), label(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-form-components-that-have-been-set-as-criteria-1
updated_at: 2026-06-03 10:12:24
