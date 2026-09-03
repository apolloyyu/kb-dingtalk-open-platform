# 获取可打标部门列表

doc_id: LvyxQfHsgI
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/exclusive/partnerDepartments
api_version: v2-new
app_types: 第三方企业应用
permissions: Partner.Department.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。 **[!NOTE]** 调用本接口，需要使用上下游组织的访问凭证，不能使用所属组织的访问凭证。

## Path params
- none

## Query params
- none

## Body
- none

## Returns
- optional: data(Array), deptId(String), superDeptId(String), deptName(String), memberCount(Long), partnerNum(String), partnerLabelVOLevel1(Object), labelId(Long), labelName(String), levelNum(Long), partnerLabelVOLevel2(Object), partnerLabelVOLevel3(Object), partnerLabelVOLevel4(Object), partnerLabelVOLevel5(Object)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-a-list-of-departments-that-can-be-marked
updated_at: 2026-06-02 19:14:50
