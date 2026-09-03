# 获取Agoal目标或关键结果关联的关键行动

doc_id: KNtD4EBdMw
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/agoal/objectives/keyActionLists
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Agoal.Objective.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- objectiveId (String, required): 查询的目标id。
- dingUserId (String, required): 查询的指定用户钉钉userId。
- optional: keyResultId(String)

## Body
- none

## Returns
- optional: requestId(String), success(Boolean), content(Array), OpenAgoalKeyActionDTO(OpenAgoalKeyActionDTO)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-agoalobjectivekeyactionlist
updated_at: 2026-06-15 10:38:59
