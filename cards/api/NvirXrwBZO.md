# 获取流程任务详情

doc_id: NvirXrwBZO
completeness: full
archived: true
method: GET
endpoint: https://api.dingtalk.com/v1.0/esign/flows/detail
api_version: v2-new
app_types: 第三方企业应用
permissions: not_stated

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: taskId(String)

## Body
- none

## Returns
- optional: data(Object), businessSense(String), flowStatus(Integer), initiatorAuthorizedName(String), initiatorName(String), logs(Array), operatorAccountName(String), logType(String), operateDescription(String), operateTime(Long), code(Integer), message(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-task-details-of-the-corresponding-process
updated_at: 2026-08-25 09:37:37
