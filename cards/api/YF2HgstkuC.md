# 删除可信设备

doc_id: YF2HgstkuC
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/exclusive/trustedDevices/remove
api_version: v2-new
app_types: 第三方企业应用
permissions: Custom.TrustedDevice.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userId (String, required): 设备所属的用户userId，请参考基础概念--UserId。
- kickOff (Boolean, required): 是否踢下线： - true：是 - false：否 该参数如果传true，该设备上登录的专属账号会全部下线，包括其他设备上登录的该账号，也会下线。
- optional: macAddress(String), id(Long)

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-trusted-devices
updated_at: 2026-06-04 19:09:54
