# 保存流程中心外部集成审批实例

doc_id: CPzgg9K5Sf
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/premium/processCentres/instances
api_version: v2-new
app_types: 第三方企业应用
permissions: Premium.Workflow.ReadWrite.All

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- processCode (String, required): 审批模板code，可通过调用获取模板code接口获取processCode参数值。
- originatorUserId (String, required): 审批实例发起人的userId。
- url (String, required): 第三方审批系统中审批单详情页地址。
- optional: formComponentValueList(Array), name(String), value(String), extValue(String), id(String), bizAlias(String), componentType(String), title(String), notifiers(Array), userid(String), position(String), featureConfig(Object), features(Array), pcUrl(String), mobileUrl(String), runType(String), callback(Object), appUuid(String), apiKey(String), version(String), config(String), bizData(String)

## Returns
- optional: result(Object), processInstanceId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-premiumexternalintegrationprocessinstance
updated_at: 2026-06-03 10:13:00
