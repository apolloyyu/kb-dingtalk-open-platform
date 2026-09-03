# 根据词条ID查询详情

doc_id: WADSAC7AsB
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/pedia/words/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Pedia.Words.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- uuid (Long, required): 查询主键编号，可调用分页获取企业词条信息接口获取。
- userId (String, required): 当前操作用户的userId。

## Body
- none

## Returns
- optional: data(Object), wordName(String), uuid(Long), gmtCreate(Long), gmtModify(Long), wordAlias(Array of String), highLightWordAlias(Array of String), relatedDoc(Array), name(String), type(String), link(String), relatedLink(Array), creatorName(String), updaterName(String), approveName(String), wordParaphrase(String), simpleWordParaphrase(String), contacts(Array of String), tagsList(Array of String), appLink(Array), appName(String), pcLink(String), phoneLink(String), iconLink(String), imHighLight(Boolean), simHighLight(Boolean), picList(Array), mediaIdUrl(String), contactList(Array), userId(String), nickName(String), avatarMediaId(String), parentUuid(Long), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-entry
updated_at: 2026-06-04 19:10:43
