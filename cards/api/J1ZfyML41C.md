# 更新流程中心任务状态

doc_id: J1ZfyML41C
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/workflow/processCentres/tasks
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_aflow

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- tasks (Array, required): OA审批任务列表，最多20个数。
- taskId (Long, required): OA审批任务ID，可调用查询通过流程中心集成的OA审批任务接口获取taskId参数值。
- status (String, required): 更新为目标任务状态： - **CANCELED**：撤销 - **COMPLETED**：完成
- optional: processInstanceId(String), result(String)

## Returns
- optional: success(Boolean)

## Limits
- OA审批任务列表，最多20个数。

source_url: https://open.dingtalk.com/document/development/update-process-center-task-status
updated_at: 2026-06-02 15:54:14
