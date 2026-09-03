# 获取当前企业所有可管理的表单

doc_id: v7nE41k4cZ
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/workflow/processes/managements/templates
api_version: v2-new
app_types: 企业内部应用
permissions: Workflow.Form.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。。

## Path params
- none

## Query params
- userId (String, required): 用户的userId。 **[!NOTE]** userId对应的人员必须拥有该企业OA审批的权限。

## Body
- none

## Returns
- optional: result(Array), iconName(String), flowTitle(String), processCode(String), newProcess(Boolean), gmtModified(String), attendanceType(Integer), iconUrl(String), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-all-manageable-forms-for-the-current-enterprise
updated_at: 2026-06-03 10:12:24
