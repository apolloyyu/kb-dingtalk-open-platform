# 员工加入待离职

doc_id: EvaV9iJgJ0
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrm/pendingDismission/start
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
- userId (String, required): 离职人userId。
- lastWorkDate (Long, required): 最后工作日。
- optional: terminationReasonVoluntary(Array of String), terminationReasonPassive(Array of String), remark(String), partner(Boolean), toHireBlackList(Boolean), toHireDismissionTalent(Boolean), toHrmBlackList(Boolean)

## Returns
- optional: requestId(String), success(Boolean), result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-empstartdismission
updated_at: 2026-06-04 19:10:28
