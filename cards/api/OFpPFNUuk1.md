# 更新词条

doc_id: OFpPFNUuk1
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/pedia/words
api_version: v2-new
app_types: 第三方企业应用
permissions: Pedia.Words.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- uuid (Long, required): 需要更新的词条编号，可调用分页获取企业词条信息接口获取。
- wordName (String, required): 词条名称。
- wordParaphrase (String, required): 词条释义。
- optional: wordAlias(Array of String), highLightWordAlias(Array of String), relatedDoc(Array), name(String), type(String), link(String), relatedLink(Array), appLink(Array), appName(String), pcLink(String), phoneLink(String), iconLink(String), userId(String), picList(Array), mediaIdUrl(String), contactList(Array), nickName(String), avatarMediaId(String)

## Returns
- optional: uuid(Long), success(Boolean)

## Limits
- 词条别名列表，最大值10。
- 可高亮的别名列表，最大值10。 高亮别名必须来自别名，否则不生效。
- 词条相关文档列表，最大值10。 支持钉钉在线文档。
- 词条相关链接列表，最大值10。
- 词条相关应用，最大值10。
- 词条的相关图片列表，最大值10。
- 词条的相关联系人列表，最大值10。

source_url: https://open.dingtalk.com/document/development/update-entry
updated_at: 2026-06-04 19:10:43
