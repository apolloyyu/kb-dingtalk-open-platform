# 同意或拒绝宜搭审批任务

doc_id: WlO9Fl3DzP
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/yida/tasks/execute
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Process.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- outResult (String, required): 审批结果。 - **AGREE**：同意。 - **DISAGREE**：拒绝。
- appType (String, required): 应用编码，可在宜搭的应用设置中获取，如下图所示：
- systemToken (String, required): 应用密钥，可在宜搭的应用设置中获取，如下图所示：
- remark (String, required): 审批意见。
- processInstanceId (String, required): 实例ID，调用获取多个表单实例ID接口获取。
- userId (String, required): 用户的userid，可调用获取部门用户userid列表接口获取。
- taskId (Long, required): 任务ID，可通过获取实例ID列表接口获取返回值中的taskId。
- optional: noExecuteExpressions(String), formDataJson(String), language(String), digitalSignUrl(String)

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/execute-approval-tasks
updated_at: 2026-06-03 10:11:52
