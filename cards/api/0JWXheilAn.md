# 获取任务状态

doc_id: 0JWXheilAn
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v2.0/doc/task/info/{taskId}
api_version: v2-new
app_types: 企业内部应用
permissions: SNS.Document.WorkspaceDocument.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- taskId (String, required): 任务id，可通过复制文档接口获取。

## Query params
- none

## Body
- none

## Returns
- optional: taskId(String), status(Integer), totalCount(Integer), succCount(Integer), failCount(Integer)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-gettaskinfo
updated_at: 2026-06-02 17:37:14
