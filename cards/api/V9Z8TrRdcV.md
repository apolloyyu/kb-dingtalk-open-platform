# 删除空间

doc_id: V9Z8TrRdcV
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/drive/spaces/{spaceId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Drive.Space.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- spaceId (String, required): 钉盘空间ID，调用获取空间列表接口获取spaceId参数值。

## Query params
- unionId (String, required): 用户unionId，可调用查询用户详情接口获取。

## Body
- none

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-a-space
updated_at: 2026-06-04 19:09:26
