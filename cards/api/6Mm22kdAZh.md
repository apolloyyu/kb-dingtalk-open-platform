# 删除词条

doc_id: 6Mm22kdAZh
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/pedia/words
api_version: v2-new
app_types: 第三方企业应用
permissions: Pedia.Words.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- uuid (Long, required): 当前需要删除的词条主键编号，可调用分页获取企业词条信息接口获取。
- userId (String, required): 当前操作用户的userId。

## Body
- none

## Returns
- optional: uuid(Long), success(Boolean)

## Limits
- 调用本接口，删除词条，删除词条后，会有3秒缓存。

source_url: https://open.dingtalk.com/document/development/delete-entry
updated_at: 2026-06-02 19:45:00
