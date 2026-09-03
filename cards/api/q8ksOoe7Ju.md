# 人才档案基础数据查询

doc_id: q8ksOoe7Ju
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/profiles/basicData/query
api_version: v2-new
app_types: 企业内部应用
permissions: Hrbrain.Data.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- optional: dingCorpId(String)

## Body
- none

## Returns
- optional: requestId(String), success(Boolean), result(Boolean), content(Object), profileBaseInfoList(Array), workNo(String), name(String), age(String), deptName(String), jobcode(String), position(String), jobLevel(String), superName(String), workPlace(String), gender(String), birthday(String), seniorityYears(String), superWorkNo(String), deptNo(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-hrbraintalentprofilebasicquery
updated_at: 2026-06-02 19:34:56
