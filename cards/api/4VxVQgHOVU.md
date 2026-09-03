# 获取审批单流程中的节点信息

doc_id: 4VxVQgHOVU
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/processes/forecast
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
- processCode (String, required): 审批流的唯一码，调用创建或更新审批表单模板接口或OA审批概述-名词解释获取。
- deptId (Integer, required): 即将发起审批单的员工所在部门ID，可通过获取部门列表接口获取。
- userId (String, required): 即将发起审批单的员工userId，可通过获取部门用户userid列表接口获取。
- formComponentValues (Array, required): 表单控件数据列表，最多长度150。
- name (String, required): 控件名称。
- value (String, required): 控件值。
- optional: id(String), bizAlias(String), extValue(String), componentType(String), details(Array)

## Returns
- optional: result(Object), isForecastSuccess(Boolean), processCode(String), userId(String), processId(Long), isStaticWorkflow(Boolean), workflowActivityRules(Array), activityId(String), prevActivityId(String), activityName(String), activityType(String), isTargetSelect(Boolean), workflowActor(Object), actorKey(String), actorType(String), actorSelectionType(String), actorSelectionRange(Object), approvals(Array), workNo(String), userName(String), labels(Array), labelNames(String), allowedMulti(Boolean), approvalType(String), approvalMethod(String), actorActivateType(String), required(Boolean), activityActioners(Array), name(String), avatar(String), workflowForecastNodes(Array), outId(String)

## Limits
- 表单控件数据列表，最多长度150。
- 子控件列表，最大列表长度150。

source_url: https://open.dingtalk.com/document/development/approval-process-prediction
updated_at: 2026-06-03 10:12:22
