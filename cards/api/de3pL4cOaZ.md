# 修改设备昵称

doc_id: de3pL4cOaZ
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/smartdevice/device/updatenick
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
- pk (String, required): 产品的唯一标识。该参数需要线下提供，请发送邮件至`yuze.yl@alibaba-inc.com`，并说明调用智能硬件接口的场景描述。
- nick (String, required): 新的设备昵称。
- optional: device_nick_modify_vo(DeviceNickModifyVo), device_name(String), device_id(String)

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/intelligent-hardware-device-nickname-modification
updated_at: 2026-06-03 09:53:22
