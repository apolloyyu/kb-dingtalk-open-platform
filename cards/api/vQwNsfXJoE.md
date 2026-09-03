# 查询设备详情

doc_id: vQwNsfXJoE
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/smartdevice/device/query
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_smart_device_base

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- pk (String, required): 产品的唯一标识。
- optional: device_query_vo(DeviceQueryVo), device_name(String), device_id(String)

## Returns
- optional: result(DeviceDetailVO), device_mac(String), corp_id(String), nick(String), device_id(String), device_name(String), pk(String), userid(String), ext(String), sn(String), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/intelligent-hardware-device-query
updated_at: 2026-06-03 09:53:25
