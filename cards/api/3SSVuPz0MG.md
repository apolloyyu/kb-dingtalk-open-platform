# 新增词条

doc_id: 3SSVuPz0MG
completeness: full
archived: false
method: POST
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
- wordName (String, required): 新增词条的名称。
- wordParaphrase (String, required): 词条释义，针对词条的描述内容。
- userId (String, required): 组织对应的员工userId。
- optional: wordAlias(Array of String), highLightWordAlias(Array of String), relatedDoc(Array), name(String), type(String), link(String), relatedLink(Array), picList(Array), mediaIdUrl(String), contactList(Array), nickName(String), avatarMediaId(String)

## Returns
- optional: uuid(Long), success(Boolean)

## Limits
- 词条的别名列表，多个名字的时候可以添加，每次调用最多传10个。
- 词条高亮别名列表，每次调用最多传10个。 从别名中选取，不在别名列表中不展示
- 词条相关的文档列表，每次调用最多传10个。 支持钉钉在线文档。
- 词条相关的链接列表，每次调用最多传10个。
- 词条相关的图片列表，每次调用最多传10个。
- 词条相关的联系人列表，每次调用最多传10个。

source_url: https://open.dingtalk.com/document/development/new-entry
updated_at: 2026-06-04 19:10:41
