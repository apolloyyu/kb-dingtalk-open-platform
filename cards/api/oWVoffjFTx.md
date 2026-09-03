# 查询企业下的所有考核计划

doc_id: oWVoffjFTx
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/agoal/org_perf/plans/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Agoal.OrgPerfPlan.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- pageNumber (Integer, required): 分页页码。
- optional: pageSize(Integer)

## Body
- none

## Returns
- optional: requestId(String), success(Boolean), content(Object), pageNumber(Integer), pageSize(Integer), totalCount(Long), result(Array), OpenOrgPerfPlanDTO(OpenOrgPerfPlanDTO)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-agoalorgperfplanquery
updated_at: 2026-06-02 11:54:49
