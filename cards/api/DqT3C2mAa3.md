# 批量获取设备详情

doc_id: DqT3C2mAa3
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/dvi/device/list
api_version: v2-new
app_types: 企业内部应用
permissions: Dvi.AudioDevice.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- deviceType (String, required): 设备类型： - 针对A1类型时，需要传递A1。 - 针对B1电子工牌类型时，需要传递B1。
- snList (Array of String, required): 设备SN。

## Returns
- optional: result(Array), sn(String), deviceName(String), userId(String), bindTimestamp(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-querydevicedetail
updated_at: 2026-08-06 15:50:49
