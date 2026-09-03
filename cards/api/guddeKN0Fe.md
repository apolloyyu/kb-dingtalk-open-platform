# 数据集成异动记录同步

doc_id: guddeKN0Fe
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/datas/changeRecords/import
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
- workNo (String, required): 钉钉 UserId。
- transferType (String, required): 异动类型。
- transferReason (String, required): 异动原因。
- transferDate (String, required): 异动时间。
- preInfo (Map, required): 异动前岗位/部门信息。
- currInfo (Map, required): 异动后岗位/部门信息。
- optional: extendInfo(Map)

## Returns
- optional: result(Boolean), success(Boolean), requestId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-hrbrainimporttransfereval
updated_at: 2026-06-04 19:10:21
