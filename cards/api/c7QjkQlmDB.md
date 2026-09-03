# 获取流程设计结构

doc_id: c7QjkQlmDB
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/yida/processes/{processId}definitions/designs
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Yida.Form.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- processId (Long, required): 流程版本id，从流程设计页面url中获取。

## Query params
- systemToken (String, required): 应用密钥，在应用数据中获取。
- userId (String, required): 用户的userid。
- appType (String, required): 应用ID。

## Body
- none

## Returns
- optional: formulaRules(Array), nodeType(String), ruleType(String), triggerMode(String), block(String), message(String), activityId(Array of String), activityAction(Array of String), rule(Object), content(String), displayRule(String), source(String), name(Object), zh_CN(String), en_US(String), nodes(Array), nextId(Array of String), childNodes(Array of Object), description(String), prevId(String), type(String), nodeId(String), props(Map), approvalSummary(Array), title(Object), flowConfig(Object), sid_instDetail(Array), fieldId(String), fieldBehavior(String), processMobileDetailUrl(String), bindingForm(String), processInitUrl(String), noRecordRecall(Boolean), allowCollaboration(Boolean), allowTemporaryStorage(Boolean), processCode(String), stopAssociationRulesIfFailed(Boolean), allowWithdraw(Boolean), processDetailUrl(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getprocessdesign
updated_at: 2026-06-02 18:09:08
