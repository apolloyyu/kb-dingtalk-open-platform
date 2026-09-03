# 批量获取员工离职信息

doc_id: ILaPL4GaKQ
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/hrm/employees/dimissionInfos
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_hrm_read_user

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- userIdList (Array of String, required): 员工userId列表，最大长度50。

## Body
- none

## Returns
- optional: result(Array), userId(String), lastWorkDay(Long), deptList(Array), dept_path(String), dept_id(Long), reasonMemo(String), preStatus(Integer), handoverUserId(String), status(Integer), mainDeptName(String), mainDeptId(Long), voluntaryReason(Array of String), passiveReason(Array of String)

## Limits
- 员工userId列表，最大长度50。

source_url: https://open.dingtalk.com/document/development/obtain-resignation-information-of-employees-new-version
updated_at: 2026-06-04 19:10:27
