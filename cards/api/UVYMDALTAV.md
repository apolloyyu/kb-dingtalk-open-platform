# 查询指定设备的详情

doc_id: UVYMDALTAV
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/aiot/products/deviceDetail
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Device.AIoT.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- productKey (String, required): 产品Key。
- deviceName (String, required): 设备名字。

## Body
- none

## Returns
- optional: status(String), connectivity(String), activatedAt(String), lastOnlineTime(String), lastOfflineTime(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getdevicedetail
updated_at: 2026-07-15 17:05:00
