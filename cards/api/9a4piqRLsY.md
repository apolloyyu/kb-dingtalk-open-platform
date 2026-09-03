# 查询企业下单个目标规则详情

doc_id: 9a4piqRLsY
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/agoal/objectiveRules/details
api_version: v2-new
app_types: 第三方企业应用
permissions: Agoal.ObjectiveRule.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- objectiveRuleId (String, required): 目标规则Id。

## Body
- none

## Returns
- optional: requestId(String), success(Boolean), content(OpenObjectiveRuleDTO)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getobjectiveruledetail
updated_at: 2026-06-02 11:52:53
