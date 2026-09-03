# 确认员工离职并删除

doc_id: I90rGNabkk
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrm/processes/terminateAndHandOver
api_version: v2-new
app_types: 企业内部应用
permissions: Hrm.Process.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userId (String, required): 要离职员工的 UserId。 - 本接口调用成功后企业员工将直接离职并从企业通讯录删除。 - 本接口不支持主管理员的离职， 需要先撤销主管理员权限；且不支持上下级组织员工和行业通讯录员工。
- optUserId (String, required): 离职的操作人。 必须是本组织员工，且不能是离职员工本人。
- lastWorkDate (Long, required): 离职日期，Unix事件戳，单位毫秒。
- dismissionMemo (String, required): 离职原因备注。
- optional: dismissionReason(Integer), terminationReasonVoluntary(Array of String), terminationReasonPassive(Array of String), aflowHandOverUserId(String), docNoteHandoverUserId(String), dingPanHandoverUserId(String), permissionHandoverUserId(String), directSubordinatesHandoverUserId(String)

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-hrmprocessterminationandhandover
updated_at: 2026-06-04 19:10:31
