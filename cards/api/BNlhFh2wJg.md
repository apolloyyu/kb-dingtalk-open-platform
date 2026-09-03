# 分页获取企业词条信息

doc_id: BNlhFh2wJg
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/pedia/words/search
api_version: v2-new
app_types: 第三方企业应用
permissions: Pedia.Words.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userId (String, required): 操作人的userId。
- pageSize (Integer, required): 当前每页需要展示的数量，最大20。
- pageNumber (Integer, required): 当前查询的页数，从1开始。
- status (String, required): 当前搜索列表的状态： - 0：审核通过 - 1：创建待审核 - 2：更新待审核 默认是0，代表获取所有审核完成的词条。
- optional: wordName(String)

## Returns
- optional: data(Array), wordName(String), uuid(Long), gmtCreate(Long), gmtModify(Long), wordAlias(Array of String), highLightWordAlias(Array of String), relatedLink(Array), name(String), type(String), link(String), relatedDoc(Array), creatorName(String), updaterName(String), approveName(String), wordParaphrase(String), simpleWordParaphrase(String), contacts(Array of String), tagsList(Array of String), appLink(Array), appName(String), pcLink(String), phoneLink(String), iconLink(String), imHighLight(Boolean), simHighLight(Boolean), picList(Array), mediaIdUrl(String), contactList(Array), userId(String), nickName(String), avatarMediaId(String), parentUuid(Long), success(Boolean)

## Limits
- 当前每页需要展示的数量，最大20。

source_url: https://open.dingtalk.com/document/development/entry-search
updated_at: 2026-06-04 19:10:44
