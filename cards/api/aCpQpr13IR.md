# 新增可信设备信息

doc_id: aCpQpr13IR
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/exclusive/trustedDevices
api_version: v2-new
app_types: 企业内部应用
permissions: Custom.TrustedDevice.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userId (String, required): 员工userid，为0时表示这个设备为公共设备。
- platform (String, required): 平台类型，目前仅支持Mac和Win两种类型。
- optional: macAddress(String), did(String), status(Integer), title(String), serialNumber(String)

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/add-information-about-a-trusted-device
updated_at: 2026-06-02 19:10:59
