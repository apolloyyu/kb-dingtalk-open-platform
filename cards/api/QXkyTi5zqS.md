# 获取第三方应用授权企业的accessToken

doc_id: QXkyTi5zqS
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/oauth2/corpAccessToken
api_version: v2-new
app_types: 企业内部应用（委托产品服务商）``, 第三方企业应用`
permissions: isvapi_base

## Request headers
- none

## Path params
- none

## Query params
- none

## Body
- suiteKey (String, required): 已创建的第三方企业应用的 Cilent ID（原第三方企业应用SuiteKey）。
- suiteSecret (String, required): 已创建的第三方企业应用的 Cilent Secret（原第三方企业应用SuiteSecret）。
- authCorpId (String, required): 授权企业的CorpId。 - 网页应用（H5）： 你可以在应用首页地址/PC端首页地址添加参数`corpid=$CORPID$`，例如：https://example.com?corpid=$CORPID$，当从工作台访问该应用时，会将 $CORPID$ 自动解析为当前访问用户所在的组织 ID。 image.png - 小程序： 使用客户端corpId接口获取。
- suiteTicket (String, required): 钉钉推送的suiteTicket，获取步骤： 1. 接入第三方企业应用的事件订阅，请参考配置 Stream 推送（推荐）。 2. 事件订阅配置成功时，钉钉会定期推送授权事件套件票据内的 suiteTicket 值。 **[!NOTE]** suiteTicket是有有效期的，调用接口要确保从推送源中读取最新推送的suiteTicket值，一般五个小时推送一次。

## Returns
- optional: accessToken(String), expireIn(Long)

## Limits
- 钉钉推送的suiteTicket，获取步骤： 1. 接入第三方企业应用的事件订阅，请参考配置 Stream 推送（推荐）。 2. 事件订阅配置成功时，钉钉会定期推送授权事件套件票据内的 suiteTicket 值。 **[!NOTE]** suiteTicket是有有效期的，调用接口要确保从推送源中读取最新推送的suiteTicket值，一般五个小时推送一次。
- 定制应用的accessToken超时时间，单位秒。 **[!NOTE]** accessToken的有效期为7200秒（2小时），有效期内重复获取会返回新的accessToken。

source_url: https://open.dingtalk.com/document/development/obtain-the-access-token-of-the-authorized-enterprise-1
updated_at: 2026-06-08 12:02:03
