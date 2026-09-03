# 批量执行宜搭审批任务

doc_id: WPDQntD2PZ
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/yida/tasks/batches/execute
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Task.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- outResult (String, required): 审批动作，目前支持的审批动作如下： - agree: 同意。 - disagree: 拒绝。
- appType (String, required): 宜搭应用编码。 该参数从宜搭应用中获取。
- systemToken (String, required): 宜搭应用密钥。 该参数从宜搭应用中获取。
- userId (String, required): 操作人userId。
- taskInformationList (String, required): 批量执行的审批任务列表，数组对象格式，每个元素值包含taskId和formInstId两个子属性。 - taskId，表示待执行的审批任务Id，调用查询流程运行任务（VPC）接口获取。 - formInstId，表示当前taskId所属的宜搭表单实例Id，调用获取实例ID列表接口或者获取多个表单实例ID接口获取。 该参数示例值如下： ``` "[{\"taskId\":\"2291xxx\",\"formInstId\":\"d84a79xxx\"}, {\"taskId\":\"2291xxx\",\"formI
- optional: remark(String)

## Returns
- optional: failNumber(Integer), successNumber(Integer), total(Integer)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/batch-execution-should-take-the-lead-of-approval-tasks
updated_at: 2026-06-03 10:11:56
