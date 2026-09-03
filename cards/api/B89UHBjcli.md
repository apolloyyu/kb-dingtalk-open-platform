# 获取企业授权信息

doc_id: B89UHBjcli
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/service/get_auth_info
api_version: v1-oapi
app_types: 企业内部应用（委托产品方案商）, 第三方企业应用
permissions: isvapi_base

## Request headers
- none

## Path params
- none

## Query params
- accessKey (String, required): - 第三方企业应用的SuiteKey，可在钉钉开发者后台的应用详情页获取。 - 定制应用的CustomKey，可在钉钉开发者后台的应用详情页获取。
- timestamp (String, required): 当前时间戳，单位毫秒。
- suiteTicket (String, required): - 第三方企业应用，使用钉钉推送的suiteTicket。 - 定制应用，可指定任意值。
- signature (String, required): 签名。签名计算方式请参考第三方访问接口的签名计算方法。 **[!NOTE]** 计算出签名以后，需要进行urlencode，才能把签名参数拼接到url中。

## Body
- auth_corpid (String, required): 授权方的CorpId，可在钉钉开发者后台首页获取。
- optional: suite_key(String)

## Returns
- optional: auth_info(AuthInfo), agent(Agent[]), agentid(Number), logo_url(String), appid(Number), admin_list(String[]), agent_name(String), auth_user_info(AuthUserInfo), userId(String), auth_corp_info(AuthCorpInfo), corpid(String), invite_code(String), industry(String), corp_name(String), license_code(String), auth_channel(String), auth_channel_type(String), is_authenticated(Boolean), auth_level(Number), invite_url(String), corp_logo_url(String), errmsg(String), errcode(Number), channel_auth_info(ChannelAuthInfo), channelAgent(Channelagent[])

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-basic-information-of-an-enterprise
updated_at: 2026-04-29 22:27:44
