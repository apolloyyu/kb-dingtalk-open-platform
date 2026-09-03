# 查询流程运行任务（VPC）

doc_id: VQAWR0zuGt
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/yida/processes/tasks/getRunningTasks
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Task.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: processInstanceId(String), appType(String), systemToken(String), language(String), userId(String)

## Body
- none

## Returns
- optional: result(Array), createTimeGMT(String), activityId(String), processInstanceId(String), taskType(String), titleInEnglish(String), activeTimeGMT(String), actualActionerId(String), originatorId(String), finishTimeGMT(String), title(String), taskId(String), status(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-process-running-tasks-vpc
updated_at: 2026-06-02 11:20:44
