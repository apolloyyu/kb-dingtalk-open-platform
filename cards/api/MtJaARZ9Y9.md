# 根据设备ID查询设备

doc_id: MtJaARZ9Y9
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/smartdevice/device/querybyid
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
- device_query_vo (DeviceQueryVo, required): 设备查询对象，包含查询条件。
- device_id (String, required): 设备主键ID，唯一标识一个设备，可通过查询设备列表接口获取。

## Returns
- optional: result(DeviceDetailVO), device_mac(String), corp_id(String), nick(String), device_id(String), device_name(String), pk(String), userid(String), ext(String), sn(String), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/the-smart-hardware-can-query-details-based-on-the-device
updated_at: 2026-06-03 09:53:27
