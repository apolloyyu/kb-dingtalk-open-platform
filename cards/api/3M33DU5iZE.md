# 确认执行设备固件升级

doc_id: 3M33DU5iZE
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/aiot/products/{productKey}/devices/{deviceName}/firmware/confirmUpgrade
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Device.AIoT.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- productKey (String, required): 产品Key。
- deviceName (String, required): 设备名称。

## Query params
- optional: moduleName(String)

## Body
- none

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-confirmfirmwareupgrade
updated_at: 2026-07-15 17:05:03
