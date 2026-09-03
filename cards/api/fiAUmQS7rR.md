# 自定义模型数据同步

doc_id: fiAUmQS7rR
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/datas/customModels/import
api_version: v2-new
app_types: 第三方企业应用
permissions: Hrbrain.Import.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- corpId (String, required): 组织编码。
- modelCode (String, required): 自定义模型编码。

## Body
- none

## Returns
- optional: requestId(String), result(Boolean), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-hrbrainimportcustom
updated_at: 2026-06-02 19:34:58
