# 获取单个审批实例详情

doc_id: DuRiZXutk0
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/workflow/processInstances
api_version: v2-new
app_types: 第三方企业应用
permissions: Workflow.Instance.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- processInstanceId (String, required): 审批实例ID。 - 调用发起审批实例接口获取`InstanceId`参数值： - 调用获取审批实例ID列表接口获取`list`参数值。

## Body
- none

## Returns
- optional: result(Object), title(String), finishTime(String), originatorUserId(String), originatorDeptId(String), originatorDeptName(String), status(String), approverUserIds(Array of String), ccUserIds(Array of String), businessId(String), operationRecords(Array), userId(String), date(String), type(String), remark(String), attachments(Array), fileName(String), fileSize(String), fileId(String), fileType(String), spaceId(String), activityId(String), showName(String), images(Array of String), tasks(Array), taskId(Long), createTime(String), mobileUrl(String), pcUrl(String), processInstanceId(String), taskGroupName(String), bizAction(String), bizData(String), attachedProcessInstanceIds(Array of String), mainProcessInstanceId(String), formComponentValues(Array), id(String), name(String), value(String), extValue(String), componentType(String), bizAlias(String), success(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-details-of-a-single-approval-instance-pop
updated_at: 2026-08-19 09:09:34
