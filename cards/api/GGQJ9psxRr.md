# 获取用户通讯录个人信息

doc_id: GGQJ9psxRr
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/contact/users/{unionId}
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用, 第三方个人应用
permissions: Contact.User.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用服务端接口的授权凭证。使用个人用户的accessToken，请参考获取登录用户的访问凭证。

## Path params
- unionId (String, required): 用户的unionId。 **[!NOTE]** 如需获取当前授权人的信息，unionId参数可以传me。

## Query params
- none

## Body
- none

## Returns
- optional: nick(String), avatarUrl(String), mobile(String), openId(String), unionId(String), email(String), stateCode(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/dingtalk-retrieve-user-information
updated_at: 2026-07-30 10:02:44
