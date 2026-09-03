# 调用指定设备的物模型服务

doc_id: OxlzpHA0GH
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/aiot/products/{productKey}/devices/{deviceName}/services/{serviceIdentifier}/invoke
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Device.AIoT.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- productKey (String, required): 产品key。
- deviceName (String, required): 设备名称。
- serviceIdentifier (String, required): 物模型服务 identifier，必须与产品物模型保持一致。

## Query params
- none

## Body
- optional: timeoutSeconds(Long), args(Map)

## Returns
- optional: status(String), invocationId(String), errorCode(String), errorMsg(String), outputData(Map)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-invokedeviceservice
updated_at: 2026-07-15 17:05:06
