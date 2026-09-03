# 查询可信设备详细信息

doc_id: b5ViWzhSvi
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/exclusive/trustedDevices/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Custom.TrustedDevice.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: userIds(Array of String), gmtCreateStart(Long), gmtCreateEnd(Long), gmtModifiedStart(Long), gmtModifiedEnd(Long), pageSize(Long), pageNumber(Long), platform(String), macAddress(String), status(Integer), serialNumber(String), deviceUuid(String)

## Returns
- optional: data(Array), userId(String), platform(String), macAddress(String), status(Integer), createTime(Long), title(String), model(String), modifiedTime(Long), id(Long), serialNumber(String), deviceUuid(String), total(Long), pageSize(Long), currentPage(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-trusted-device-details
updated_at: 2026-06-04 19:09:55
