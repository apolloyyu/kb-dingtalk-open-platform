# 查询已经注册的设备信息

doc_id: UOg7aWsTlm
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/devicemng/customers/devices/activations/infos
api_version: v2-new
app_types: 第三方企业应用
permissions: Manufacture.DeviceData.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: deviceTypeId(String), pageNumber(Integer), groupId(String), pageSize(Integer), deviceCode(String), deviceCategory(Integer)

## Body
- none

## Returns
- optional: totalCount(Long), success(Boolean), result(Array), bizExt(String), deviceCallbackUrl(String), deviceCode(String), deviceDetailUrl(String), deviceName(String), groupUuid(String), icon(String), introduction(String), typeUuid(String), uuid(String), deviceCategory(Integer)

## Limits
- 每页大小，最大值50。

source_url: https://open.dingtalk.com/document/development/query-information-about-a-registered-device
updated_at: 2026-06-03 09:09:33
