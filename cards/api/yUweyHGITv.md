# 查询团队列表

doc_id: yUweyHGITv
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/dvi/teams
api_version: v2-new
app_types: 企业内部应用
permissions: Dvi.Sale.Meta.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- optional: nextToken(String), maxResults(Integer)

## Body
- none

## Returns
- optional: result(Array), code(String), name(String), tagList(Array), valueList(Array), totalCount(Integer), nextToken(String)

## Limits
- 每页数据数量,最大50，默认10。
- 下一页的查询token，5分钟内有效。

source_url: https://open.dingtalk.com/document/development/api-listteam
updated_at: 2026-07-08 14:13:52
