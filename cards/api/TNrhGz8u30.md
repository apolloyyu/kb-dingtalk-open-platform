# 数据集成组织架构同步

doc_id: TNrhGz8u30
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/datas/deptInfos/import
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
- deptNo (String, required): 部门 ID。
- deptName (String, required): 部门名称。
- superDeptNo (String, required): 上级部门 ID。
- optional: superDeptName(String), superEmpId(String), superName(String), createDate(String), effectiveDate(String), isEffective(String), extendInfo(Map)

## Returns
- optional: result(Boolean), success(Boolean), requestId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-hrbrainimportdeptinfo
updated_at: 2026-06-04 19:10:20
