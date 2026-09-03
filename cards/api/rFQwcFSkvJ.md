# 人才池在池人员列表

doc_id: rFQwcFSkvJ
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/datas/empPools/users/lists/query
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
- optional: nextToken(Integer), maxResults(Integer), poolCode(String), userId(String)

## Returns
- optional: requestId(String), success(Boolean), result(Boolean), content(Object), totalCount(Integer), maxResults(Integer), nextToken(Integer), empVos(Array), userId(String), name(String)

## Limits
- 分页条数，如果未填写，默认100条。

source_url: https://open.dingtalk.com/document/development/api-hrbrainemppooluser
updated_at: 2026-06-02 19:34:57
