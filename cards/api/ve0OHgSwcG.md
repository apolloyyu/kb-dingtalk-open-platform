# 数据集成人员信息同步

doc_id: ve0OHgSwcG
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/datas/empInfos/import
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
- gender (String, required): 性别。
- birthday (String, required): 出生日期。
- nation (String, required): 民族。
- nationCtry (String, required): 国籍。
- politicalStatus (String, required): 政治面貌。
- empType (String, required): 员工类型。
- empStatus (String, required): 雇佣状态。
- empSource (String, required): 招聘来源。
- jobCodeName (String, required): 职务。
- postName (String, required): 职位。
- deptNo (String, required): 部门编码。
- deptName (String, required): 部门名称。
- optional: marriage(String), workEmail(String), jobLevel(String), superEmpId(String), superName(String), workLocCity(String), workLocAddr(String), registDate(String), regularDate(String), isDimission(String), dimissionDate(String), highestEduName(String), highestDegree(String), lastSchoolName(String), extendInfo(Map)

## Returns
- optional: result(Boolean), success(Boolean), requestId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-hrbrainimportempinfo
updated_at: 2026-06-04 19:10:09
