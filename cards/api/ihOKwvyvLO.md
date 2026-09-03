# Agoal业务数据查询

doc_id: ihOKwvyvLO
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/agoal/bizData/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Agoal.Indicator.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: nextToken(String), maxResults(Long), bizCode(String)

## Body
- none

## Returns
- optional: success(Boolean), result(Boolean), requestId(String), content(Object), nextToken(String), maxResults(Long), bizInfos(Array of Object)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/agoal-business-biz-data-query
updated_at: 2026-06-02 11:57:10
