# 通过指标编码批量查询指标列表

doc_id: yzaqdR9GOw
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/agoal/indicator/batch/query
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Agoal.Indicator.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: codeList(Array of String)

## Body
- none

## Returns
- optional: success(Boolean), result(Array), id(String), code(String), title(String), description(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-agoalindicatorbatchquery
updated_at: 2026-06-15 10:39:07
