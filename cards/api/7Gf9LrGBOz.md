# 获取数据表单实例列表

doc_id: 7Gf9LrGBOz
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/dataForms/formInstances/pages
api_version: v2-new
app_types: 企业内部应用
permissions: Premium.Workflow.ReadWrite.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- maxResults (Integer, required): 分页大小，最大值100。
- formCode (String, required): 数据表单模板ID。 - 通过OA审批概述-名词解释获取。
- optional: nextToken(String), appUuid(String)

## Body
- none

## Returns
- optional: result(Object), nextToken(String), hasMore(Boolean), maxResults(Long), values(Array), formInstanceId(String), appUuid(String), formCode(String), title(String), creator(String), modifier(String), createTimestamp(Long), modifyTimestamp(Long), outInstanceId(String), outBizCode(String), attributes(Map), formInstDataList(Array), componentType(String), bizAlias(String), extendValue(String), label(String), value(String), key(String)

## Limits
- 分页大小，最大值100。

source_url: https://open.dingtalk.com/document/development/api-premiumgetforminstances
updated_at: 2026-06-03 10:13:06
