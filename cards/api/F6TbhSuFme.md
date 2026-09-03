# 获取单个数据表单实例详情

doc_id: F6TbhSuFme
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/dataForms/formInstances
api_version: v2-new
app_types: 企业内部应用
permissions: Premium.Workflow.ReadWrite.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- formInstanceId (String, required): 数据表单实例ID。
- formCode (String, required): 数据表单模板ID，通过OA审批概述-名词解释获取。
- optional: appUuid(String)

## Body
- none

## Returns
- optional: formInstanceId(String), formInstDataList(Array), componentType(String), bizAlias(String), extendValue(String), label(String), value(String), key(String), appUuid(String), formCode(String), title(String), creator(String), modifier(String), createTimestamp(Long), modifyTimestamp(Long), outInstanceId(String), outBizCode(String), attributes(Map)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-details-of-a-single-data-form-instance
updated_at: 2026-06-03 10:13:06
