# 数据集成专业技能同步

doc_id: JjQ3h0OOkR
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/datas/profSkills/import
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
- name (String, required): 姓名。
- workNo (String, required): 钉钉用户 UserId。
- level1 (String, required): 专业技能一级。
- level2 (String, required): 专业技能二级。
- level3 (String, required): 专业技能三级。
- optional: extendInfo(Map)

## Returns
- optional: result(Boolean), success(Boolean), requestId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-hrbrainimportlabelprofskill
updated_at: 2026-06-04 19:10:17
