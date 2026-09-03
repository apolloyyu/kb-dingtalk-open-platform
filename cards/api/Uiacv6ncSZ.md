# 绑定设备

doc_id: Uiacv6ncSZ
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/smartdevice/external/bind
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_smart_device_bind_write

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- device_bind_req_vo (DeviceBindReqVo, required): 设备请求信息对象，包含设备绑定所需的所有参数。
- sn (String, required): 设备序列号（SN），唯一标识一台物理设备。
- dn (String, required): 设备名称。
- pk (String, required): 产品的唯一标识。该参数需线下提供，请发送邮件至`yuze.yl@alibaba-inc.com`，并说明调用智能硬件接口的场景描述。
- optional: nick(String), mac(String), outid(String), ext(String)

## Returns
- optional: result(DeviceBindRespVo), device_id(String), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/establishing-a-binding-relationship-between-intelligent-hardware-and-cloud
updated_at: 2026-06-03 09:53:18
