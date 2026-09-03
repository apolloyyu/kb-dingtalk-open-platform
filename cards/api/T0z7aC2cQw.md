# 批量注册与激活设备

doc_id: T0z7aC2cQw
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/devicemng/customers/devices/registrationActivations/batch
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
- optional: registerAndActivateVOS(Array), deviceDetailUrl(String), deviceCallbackUrl(String), groupUuid(String), introduction(String), roleUuid(String), typeUuid(String), userIds(Array of String), deviceCategory(Integer)

## Returns
- optional: successItems(Array), errorCode(String), errorMsg(String), result(Object), deviceCallbackUrl(String), deviceCode(String), deviceDetailUrl(String), deviceName(String), groupUuid(String), icon(String), introduction(String), roleUuid(String), userIds(Array of String), status(Long), typeUuid(String), uuid(String), deviceCategory(Integer), success(Boolean), failItems(Array)

## Limits
- 批量注册的设备信息列表，最大值100。
- 设备详情链接，最大长度2048字符。
- 设备回调链接，最大长度2048字符。
- 设备管理员的userId列表，最大值50。

source_url: https://open.dingtalk.com/document/development/register-and-activate-devices-in-batches
updated_at: 2026-06-03 09:09:32
