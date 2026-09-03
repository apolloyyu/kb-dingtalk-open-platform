# 根据sns临时授权码获取用户信息

doc_id: VJWxtc35fw
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/sns/getuserinfo_bycode
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- accessKey (String, required): 应用的AppKey，在钉钉开发者后台应用详情页查看。
- timestamp (String, required): 当前时间戳，单位毫秒。 **[!NOTE]** 使用SDK调用时，这个值不需要填写，SDK内部已做处理。
- signature (String, required): 通过appSecret计算出来的签名值，计算方式请参考个人免登场景的签名计算方法。 **[!NOTE]** 使用SDK调用时，这个值不需要填写，SDK内部已做处理。

## Body
- optional: tmp_auth_code(String)

## Returns
- optional: user_info(UserInfo), nick(String), unionid(String), openid(String), main_org_auth_high_level(Boolean), errmsg(String), errcode(Number)

## Limits
- 用户授权的临时授权码，只能使用一次。获取方法请参考：实现网页方式登录应用（登录第三方网站）

source_url: https://open.dingtalk.com/document/development/obtain-the-user-information-based-on-the-sns-temporary-authorization
updated_at: 2026-08-25 09:36:36
