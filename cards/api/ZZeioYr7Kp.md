# 获取 Agoal 组织目标列表

doc_id: ZZeioYr7Kp
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/agoal/orgObjectives/list
api_version: v2-new
app_types: 第三方企业应用
permissions: Agoal.OrgObjective.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- pageNumber (Integer, required): 分页页码
- optional: dingTeamId(String), periodId(String), pageSize(Integer)

## Body
- none

## Returns
- optional: requestId(String), success(Boolean), content(OpenAgoalOrgObjectiveListDTO)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-agoalorgobjectivelist
updated_at: 2026-07-08 14:13:50
