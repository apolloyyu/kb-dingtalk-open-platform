# 查询表单数据

doc_id: nmoz6mUK1C
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v2.0/yida/forms/instances/{id}
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Yida.Form.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- optional: id(String)

## Query params
- optional: appType(String), systemToken(String), userId(String), language(String), useAlias(Boolean), formUuid(String)

## Body
- none

## Returns
- optional: originator(Object), userId(String), name(Object), nameInChinese(String), nameInEnglish(String), type(String), departmentName(String), email(String), modifiedTimeGMT(String), formInstId(String), formData(Map)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getformdatabyid-v2
updated_at: 2026-06-15 10:44:08
