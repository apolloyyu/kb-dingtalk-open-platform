# 匹配文本中的词条

doc_id: B8gsHoBhzB
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/wiki/words/parse
api_version: v2-new
app_types: 第三方企业应用
permissions: Wiki.Words.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- content (String, required): 待匹配词条的文本，最大长度4096个字符。

## Returns
- optional: success(Boolean), errMsg(String), data(Array), startIndex(Long), endIndex(Long), wordName(String)

## Limits
- 待匹配词条的文本，最大长度4096个字符。

source_url: https://open.dingtalk.com/document/development/enterprise-encyclopedia-match-entries-in-a-text
updated_at: 2026-06-04 19:10:45
