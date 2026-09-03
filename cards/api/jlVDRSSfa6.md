# 数据集成绩效记录同步

doc_id: jlVDRSSfa6
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/datas/perfRecords/import
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
- perfPlanName (String, required): 绩效计划名称。
- period (String, required): 绩效周期。
- periodStartDate (String, required): 计划开始日期。
- periodEndDate (String, required): 计划结束日期。
- score (String, required): 绩效结果。
- optional: perfCate(String), perfScore(String), comment(String), extendInfo(Map)

## Returns
- optional: result(Boolean), success(Boolean), requestId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-hrbrainimportperfeval
updated_at: 2026-06-04 19:10:13
