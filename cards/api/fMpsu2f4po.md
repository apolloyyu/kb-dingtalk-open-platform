# 注册卡片回调地址

doc_id: fMpsu2f4po
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/card/callbacks/register
api_version: v2-new
app_types: 第三方企业应用
permissions: Card.Instance.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- callbackRouteKey (String, required): 回调地址的路由Key。 **[!NOTE]** 一个`callbackRouteKey` 仅可映射一个`callbackUrl`。
- callbackUrl (String, required): 接受动态卡片回调的 URL 地址。 **[!NOTE]** 必须是公网可访问的 URL。
- optional: apiSecret(String), forceUpdate(Boolean)

## Returns
- optional: success(Boolean), result(Object), callbackUrl(String), apiSecret(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/register-card-callback-address
updated_at: 2026-06-04 10:50:04
