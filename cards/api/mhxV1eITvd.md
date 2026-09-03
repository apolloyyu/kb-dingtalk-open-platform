# 注册设备到钉钉

doc_id: mhxV1eITvd
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/devicemng/customers/devices/registerAndActivate
api_version: v2-new
app_types: 第三方企业应用
permissions: Manufacture.DeviceData.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- deviceCode (String, required): 设备号。 **[!NOTE]** 用户自定义参数，要求企业内每一个设备的设备码必须唯一。
- deviceName (String, required): 设备名称。 **[!NOTE]** 用户自定义参数。
- optional: introduction(String), typeUuid(String), userIds(Array of String), roleUuid(String), deviceDetailUrl(String), deviceCallbackUrl(String), deviceCategory(Integer)

## Returns
- optional: success(Boolean), result(Object), deviceCode(String), deviceUuid(String), deviceName(String), introduction(String), typeUuid(String), roleUuid(String), deviceDetailUrl(String), userIds(Array of String), deviceCategory(Integer)

## Limits
- 设备详情链接，最大长度2048字符。
- 设备回调链接，最大长度2048字符。
- 设备管理员的userId列表，最大值50。

source_url: https://open.dingtalk.com/document/development/pin-registration-interface
updated_at: 2026-06-03 09:09:30
