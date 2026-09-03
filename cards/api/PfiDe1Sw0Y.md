# 批量新增可信设备

doc_id: PfiDe1Sw0Y
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/exclusive/trusts/devices
api_version: v2-new
app_types: 第三方企业应用
permissions: Custom.TrustedDevice.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： 企业内部应用，调用获取企业内部应用的accessToken接口获取。 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userId (String, required): 员工userid，为0时表示这个设备为公共设备
- platform (String, required): 操作端。 - Mac端 - Win端
- optional: macAddressList(Array of String), detailList(Array), title(String), macAddress(String), serialNumber(String)

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-multiple-trusted-devices
updated_at: 2026-06-04 19:09:53
