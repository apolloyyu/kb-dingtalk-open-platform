# 查询抄送我的任务列表（应用维度）

doc_id: XA7bOPOykV
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/yida/tasks/taskCopies
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Task.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- appType (String, required): 应用ID。
- systemToken (String, required): 应用秘钥，在应用数据中获取。
- userId (String, required): 用户userid。
- optional: pageSize(Integer), language(String), pageNumber(Integer), keyword(String), processCodes(String), createFromTimeGMT(Long), createToTimeGMT(Long)

## Body
- none

## Returns
- optional: pageNumber(Long), totalCount(Long), data(Array), actionExecutorId(Array of String), processInstanceId(String), formUuid(String), serialNumber(String), processInstanceStatus(String), originatorDisplayName(String), modifiedTimeGMT(String), carbonActivityId(String), dataType(String), actionExecutorName(Array of String), originatorAvatar(String), processInstanceStatusText(String), processApprovedResultText(String), formInstanceId(String), title(String), version(Long), instanceValue(String), createTimeGMT(String), processApprovedResult(String), processId(Long), processName(String), processCode(String), appType(String), dataMap(Map), currentActivityInstances(Array), activityName(String), activityNameInEnglish(String), activityId(String), id(Long), activityInstanceStatus(String), finishTimeGMT(String), originatorId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-copied-my-task-list-application-dimension
updated_at: 2026-06-02 11:25:32
