# 转交任务

doc_id: b0wUeb2Aic
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/yida/tasks/redirect
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
- processInstanceId (String, required): 流程实例ID。
- appType (String, required): 应用ID。
- systemToken (String, required): 应用秘钥，在应用数据中获取。
- remark (String, required): 审批意见。
- nowActionExecutorId (String, required): 新的任务处理人工号。
- userId (String, required): 处理人的userid。
- taskId (Long, required): 任务ID。
- optional: byManager(String), language(String)

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/transfer-tasks
updated_at: 2026-06-02 11:19:41
