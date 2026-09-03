# 查询设备属性

doc_id: oYLH6Ou7Rg
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/dvi/device/status
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
- snList (Array of String, required): 设备SN：可以在设备背面铭牌区域查看到。

## Returns
- optional: result(Array), sn(String), status(Object), timestamp(Long), value(String), battery(Object), firmware(Object), recordingStartTime(Object)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-querydevicestatus
updated_at: 2026-08-06 15:50:43
