# 查询企业下指定个人目标的所有进展

doc_id: TIilX3vb7k
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/agoal/objectives/progresses/lists
api_version: v2-new
app_types: 第三方企业应用
permissions: Agoal.ObjectiveProgress.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- objectiveId (String, required): 目标Id。
- pageNumber (Integer, required): 分页页码。
- optional: pageSize(Integer)

## Body
- none

## Returns
- optional: requestId(String), success(Boolean), content(Object), pageNumber(String), pageSize(String), totalCount(String), result(Array), OpenAgoalProgressDTO(OpenAgoalProgressDTO)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-agoalobjectiveprogresslist
updated_at: 2026-06-02 11:56:21
