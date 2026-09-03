# 企业账号修改钉钉号

doc_id: 9VI0AepSKW
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/contact/orgAccounts/dingTalkIds/change
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_manage_addresslist

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userId (String, required): 员工userId，只支持归属于本企业的企业账号userId。
- dingTalkId (String, required): 新的钉钉号。全局唯一，不只是组织内唯一，所以不能和已经存在的冲突，发生冲突时需要更换备选值。格式要求： - 6<=长度<=20 - 字母开头 - 只包含字母、数字 - 不能包含违禁内容

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-changedingtalkid
updated_at: 2026-06-04 14:29:35
