# 获取授权应用的基本信息

doc_id: QpAVnHmVl3
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/service/get_agent
api_version: v1-oapi
app_types: 第三方企业应用
permissions: isvapi_base

## Request headers
- none

## Path params
- none

## Query params
- suite_access_token (String, required): 第三方企业应用的suite_access_token，可通过获取第三方企业应用的suite_access_token接口获取。
- timestamp (String, required): 当前时间戳, 单位毫秒。 **[!NOTE]** 使用SDK调用时，不需要传递此参数。
- suiteTicket (String, required): 钉钉开放平台向应用的回调URL推送的suite_ticket，详细内容请参考数据格式biz_type=2。
- signature (String, required): 签名。签名计算方式请参考第三方访问接口的签名计算方法。 **[!IMPORTANT]** 计算出签名以后，需要进行urlencode，才能把签名参数拼接到url中。

## Body
- agentid (String, required): 授权企业方应用ID，有以下两种获取方式： - 调用获取企业授权信息接口获取。 - 从企业授权开通应用事件中获取。
- auth_corpid (String, required): 授权企业的CorpId，从企业授权开通应用事件中获取。
- suite_key (String, required): 第三方应用的Suitekey。 可在钉钉开发者后台的第三方应用详情页面获取。

## Returns
- optional: agentid(Number), name(String), logo_url(String), description(String), close(Number), errmsg(String), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-application-information-of-an-enterprise
updated_at: 2026-04-29 22:27:45
