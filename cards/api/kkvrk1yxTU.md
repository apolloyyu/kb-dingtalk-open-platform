# 数据集成教育经历同步

doc_id: kkvrk1yxTU
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/datas/eduExperiences/import
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
- schoolName (String, required): 学校。
- startDate (String, required): 开始日期。
- endDate (String, required): 结束日期。
- eduName (String, required): 学历。
- optional: major(String), extendInfo(Map)

## Returns
- optional: result(Boolean), success(Boolean), requestId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-hrbrainimporteduexp
updated_at: 2026-06-04 19:10:12
