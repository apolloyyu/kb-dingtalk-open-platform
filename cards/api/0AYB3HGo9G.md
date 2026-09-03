# 批量取消流程中心待处理任务

doc_id: 0AYB3HGo9G
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/processCentres/tasks/cancel
api_version: v2-new
app_types: 第三方企业应用
permissions: Workflow.Instance.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- processInstanceId (String, required): OA审批流程实例ID，调用创建实例接口获取processInstanceId参数值。
- activityId (String, required): 待办组ID，调用创建流程中心待处理任务接口获取，最大长度512字符。 **[!NOTE]** 需要在调用创建流程中心待处理任务接口时，主动设置该值。
- optional: activityIds(Array of String)

## Returns
- optional: success(Boolean)

## Limits
- 待办组ID，调用创建流程中心待处理任务接口获取，最大长度512字符。 **[!NOTE]** 需要在调用创建流程中心待处理任务接口时，主动设置该值。

source_url: https://open.dingtalk.com/document/development/cancel-multiple-oa-approval-tasks
updated_at: 2026-06-02 15:54:15
