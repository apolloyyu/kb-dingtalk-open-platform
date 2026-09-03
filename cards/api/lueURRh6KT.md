# 根据unionid获取用户userid

doc_id: lueURRh6KT
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/user/getbyunionid
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_get_member

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 **[!NOTE]** 如果是通过**免登方式**获取的unionid，则不能使用免登获取的 token 调用该接口，需要使用下方的接口重新获取。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- unionid (String, required): 员工在当前开发者企业账号范围内的唯一标识，系统生成，不会改变。可通过调用通过免登码获取用户信息获取unionid。

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(UserGetByUnionIdResponse), contact_type(Number), userid(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-a-user-by-the-union-id
updated_at: 2026-06-08 09:28:39
