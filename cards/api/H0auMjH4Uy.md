# 数据集成基础标签同步

doc_id: H0auMjH4Uy
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/datas/baseLabels/import
api_version: v2-new
app_types: 企业内部应用
permissions: Hrbrain.Import.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 接口调用凭证，调用获取用户token接口获取。

## Path params
- none

## Query params
- corpId (String, required): 组织编码。

## Body
- workNo (String, required): 钉钉 UserId。
- name (String, required): 姓名。
- extendInfo (Map, required): 标签字段，KV结构。

## Returns
- optional: result(Boolean), success(Boolean), requestId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-hrbrainimportlabelbase
updated_at: 2026-06-04 19:10:16
