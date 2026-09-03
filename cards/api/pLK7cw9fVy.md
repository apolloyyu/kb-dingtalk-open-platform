# 获取Agoal指定规则周期下负责人的目标列表

doc_id: pLK7cw9fVy
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/agoal/users/objectiveLists/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Agoal.Objective.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- objectiveRuleId (String, required): 目标规则id。
- periodIds (Array of String, required): 周期id。
- dingUserId (String, required): 目标负责人dingUserId。

## Returns
- optional: requestId(String), success(Boolean), content(Array), OpenAgoalObjectiveDTO(OpenAgoalObjectiveDTO)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-agoaluserobjectivelist
updated_at: 2026-06-04 14:22:58
