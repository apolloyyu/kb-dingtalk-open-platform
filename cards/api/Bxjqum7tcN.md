# 人员标签数据查询

doc_id: Bxjqum7tcN
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/datas/labelRecords/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Hrbrain.Data.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: dingCorpId(String), maxResult(Integer), nextToken(String)

## Body
- optional: userId(String), labels(Array), typeCode(String), code(String)

## Returns
- optional: requestId(String), success(Boolean), result(Boolean), content(Object), nextToken(String), maxResults(Long), totalCountt(Long), data(Array), labels(Array), code(String), guid(String), name(String), options(Array), label(String), tip(String), value(String), typeCode(String), typeName(String), userId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-stafflabelrecordsquery
updated_at: 2026-06-02 19:34:56
