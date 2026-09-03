# 查询公共设备

doc_id: PFrPfVam5O
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/exclusive/trusts/publicDevices
api_version: v2-new
app_types: 企业内部应用
permissions: Custom.TrustedDevice.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- optional: platform(String), startTime(Long), endTime(Long), pageSize(Integer), pageNumber(Integer), title(String), macAddress(String), serialNumber(String), deviceUuid(String), serialNumberList(Array of String), encryptDeviceIdList(Array of String), didList(Array of String)

## Body
- none

## Returns
- optional: totalCnt(Long), dataCnt(Integer), data(Array), gmtCreate(Long), gmtModified(Long), title(String), macAddress(String), platform(String), deviceScopeType(Integer), deviceStaffs(Array), userId(String), name(String), deviceDepts(Array), id(Long), deviceRoles(Array), tagCode(String), serialNumber(String), deviceUuid(String), retryPermission(String), status(Integer), did(String), encryptDeviceId(String)

## Limits
- 单页返回的数据条数。 **[!NOTE]** - 最小值10。 - 最大值200。

source_url: https://open.dingtalk.com/document/development/query-public-equipment
updated_at: 2026-08-12 09:21:14
