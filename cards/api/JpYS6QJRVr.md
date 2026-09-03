# 数据集成晋升记录同步

doc_id: JpYS6QJRVr
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/datas/promRecords/import
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
- period (String, required): 晋升计划名称。
- effectiveDate (String, required): 晋升生效日期。
- preJobLevel (String, required): 晋升前职级/岗位。
- newJobLevel (String, required): 晋升后职级/岗位。
- optional: periodStartDate(String), periodEndDate(String), comment(String), extendInfo(Map)

## Returns
- optional: result(Boolean), success(Boolean), requestId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-hrbrainimportpromeval
updated_at: 2026-06-04 19:10:13
