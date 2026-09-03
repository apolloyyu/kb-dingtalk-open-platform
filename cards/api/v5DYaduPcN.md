# 获取存储中异步任务信息

doc_id: v5DYaduPcN
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/storage/tasks/{taskId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.Task.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- taskId (String, required): 存储中的异步任务ID，可调用批量移动文件或文件夹接口获取taskId参数值。 例如，批量移动文件或文件夹的异步任务ID。

## Query params
- unionId (String, required): 操作人的unionId，可调用查询用户详情接口获取。

## Body
- none

## Returns
- optional: task(Object), id(String), status(String), totalCount(Long), successCount(Long), failCount(Long), failMessage(String), beginTime(String), endTime(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-the-asynchronous-task-information-in-storage
updated_at: 2026-06-04 19:09:47
