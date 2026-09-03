# 查询词条详情

doc_id: fcgi7gsVm9
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/wiki/words/details
api_version: v2-new
app_types: 第三方企业应用
permissions: Wiki.Words.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- wordName (String, required): 词条名称，最大长度50个字符。

## Body
- none

## Returns
- optional: data(Array), wordName(String), uuid(Long), gmtCreate(Long), gmtModify(Long), orgName(String), wordAlias(Array of String), highLightWordAlias(Array of String), wordFullName(String), relatedDoc(Array), name(String), type(String), link(String), relatedLink(Array), creatorName(String), updaterName(String), approveName(String), wordParaphrase(String), simpleWordParaphrase(String), contacts(Array of String), tagsList(Array of String), appLink(Array), appName(String), appId(Long), pcLink(String), phoneLink(String), iconLink(String), imHighLight(Boolean), simHighLight(Boolean), errMsg(String), success(Boolean)

## Limits
- 词条名称，最大长度50个字符。

source_url: https://open.dingtalk.com/document/development/enterprise-encyclopedia-query-entry-details-by-entry-name
updated_at: 2026-06-04 19:10:42
