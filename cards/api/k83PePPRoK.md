# 数据集成离职信息同步

doc_id: k83PePPRoK
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/datas/dimissionInfos/import
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
- empType (String, required): 员工类型。
- dimissionDate (String, required): 离职日期。
- deptNo (String, required): 离职时部门编码。
- deptName (String, required): 离职时部门。
- superName (String, required): 离职时主管。
- dimissionReason (String, required): 离职原因分类。
- dimissionReaasonDesc (String, required): 离职原因说明。
- optional: jobLevel(String), workLocAddr(String), jobCodeName(String), postName(String), extendInfo(Map)

## Returns
- optional: result(Boolean), success(Boolean), requestId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-hrbrainimportdimission
updated_at: 2026-06-04 19:10:10
