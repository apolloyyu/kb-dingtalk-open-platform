# 通过流程code获取流程定义

doc_id: zDzQ4ALGml
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/yida/processes/designStructures
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Form.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- systemToken (String, required): 应用密钥。在应用数据中获取。
- userId (String, required): 钉钉userId。
- appType (String, required): 应用编码。
- processCode (String, required): 流程编码。
- optional: processId(Long)

## Body
- none

## Returns
- optional: formulaRules(Array), nodeType(String), ruleType(String), triggerMode(String), block(String), message(String), activityId(Array of String), activityAction(Array of String), rule(Object), content(String), displayRule(String), source(String), name(Object), zh_CN(String), en_US(String), nodes(Array), nextId(Array of String), childNodes(Array of Object), description(String), prevId(String), type(String), nodeId(String), props(Map), approvalSummary(Array), title(Object), flowConfig(Object), sid_instDetail(Array), fieldId(String), fieldBehavior(String), processMobileDetailUrl(String), bindingForm(String), processInitUrl(String), noRecordRecall(Boolean), allowCollaboration(Boolean), allowTemporaryStorage(Boolean), processCode(String), stopAssociationRulesIfFailed(Boolean), allowWithdraw(Boolean), processDetailUrl(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-definition-through-process-code
updated_at: 2026-06-02 09:50:23
