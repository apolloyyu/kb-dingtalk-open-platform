# 数据集成奖励记录同步

doc_id: XwZjRLvH1C
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/datas/awardDetails/import
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
- awardName (String, required): 奖励名称。
- awardDate (String, required): 奖励颁发日期。
- optional: awardOrg(String), awardType(String), comment(String), extendInfo(Map)

## Returns
- optional: result(Boolean), success(Boolean), requestId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-hrbrainimportawarddetail
updated_at: 2026-06-04 19:10:14
