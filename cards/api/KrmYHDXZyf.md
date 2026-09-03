# 根据手机号查询企业账号用户

doc_id: KrmYHDXZyf
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/v2/user/getbymobile
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_get_member_by_mobile

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- mobile (String, required): 用户的手机号。
- support_exclusive_account_search (Boolean, required): 是否支持通过手机号搜索企业账号。 - **true**：支持。 - **fasle**：不支持。 **[!NOTE]** - 仅适用于企业账号。 - 仅支持搜索当前企业创建的企业账号。

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(Object), userid(String), exclusive_account_userid_list(String[])

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-userid-of-your-mobile-phone-number
updated_at: 2026-05-27 13:09:09
