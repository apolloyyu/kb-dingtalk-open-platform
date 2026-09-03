# 数据集成入职信息同步

doc_id: qXklAtbg0q
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/datas/registerInfos/import
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
- registDate (String, required): 入职日期。
- empSource (String, required): 招聘类型。
- deptNo (String, required): 入职部门编码。
- deptName (String, required): 入职部门。
- optional: jobLevel(String), workLocAddr(String), superName(String), jobCodeName(String), postName(String), extendInfo(Map)

## Returns
- optional: result(Boolean), success(Boolean), requestId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-hrbrainimportregist
updated_at: 2026-06-04 19:10:10
