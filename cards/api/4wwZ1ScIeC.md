# 通知完成指定的新手任务

doc_id: 4wwZ1ScIeC
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/ats/beginnerTasks/{taskCode}/finish
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_recruitment_plugin

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- taskCode (String, required): 任务编码。 该参数需线下提供，请通过技术支持咨询。

## Query params
- userId (String, required): 员工userId。
- optional: scope(String)

## Body
- none

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/notify-the-completion-of-the-specified-novice-task
updated_at: 2026-06-04 19:10:34
