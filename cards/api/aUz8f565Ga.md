# 获取个人实名的地址

doc_id: aUz8f565Ga
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/esign/users/realnames
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Esign.Common.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。
- optional: serviceGroup(String)

## Path params
- none

## Query params
- none

## Body
- userId (String, required): 当前用户的userid。
- optional: redirectUrl(String)

## Returns
- optional: taskId(String), pcUrl(String), mobileUrl(String)

## Limits
- 实名认证成功后重定向地址。 **[!NOTE]** 地址有效期为2小时。

source_url: https://open.dingtalk.com/document/development/obtain-the-address-that-is-redirected-to-the-user-s-real
updated_at: 2026-06-04 19:11:09
