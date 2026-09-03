# 数据集成工作经历同步

doc_id: diKaTfmh7S
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/datas/workExperiences/import
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
- companyName (String, required): 公司名称。
- startDate (String, required): 开始日期。
- endDate (String, required): 结束日期。
- optional: postName(String), jobDesc(String), extendInfo(Map)

## Returns
- optional: result(Boolean), success(Boolean), requestId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-hrbrainimportworkexp
updated_at: 2026-06-04 19:10:11
