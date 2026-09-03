# 人才池信息查询

doc_id: F6VA2yKJZv
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/datas/empPools/infos/query
api_version: v2-new
app_types: 企业内部应用
permissions: Hrbrain.Data.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: nextToken(Integer), maxResults(Integer), keyword(String), labels(Array of String), userId(String)

## Returns
- optional: requestId(String), success(Boolean), result(Boolean), content(Object), totalCount(Integer), maxResults(Integer), nextToken(Integer), poolInfos(Array), poolCode(String), poolName(String), poolDesc(String), poolTags(Array), label(String), value(String)

## Limits
- 分页条数，如果未填写，默认100条。

source_url: https://open.dingtalk.com/document/development/api-hrbrainemppoolquery
updated_at: 2026-06-02 19:34:57
