# 删除老师

doc_id: GEYsJ1I4Rv
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/edu/classes/{classId}/teachers/{userId}
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_edu_safe

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- classId (Long, required): 班级ID，可调用获取部门列表接口获取dept_type为class时的dept_id参数值。
- userId (String, required): 老师的userId，可调用获取人员列表接口获取userid参数值。

## Query params
- adviser (Integer, required): 是否为班主任。 - **1**：班主任 - **0**：非班主任
- operator (String, required): 操作人userid，可调用通过免登码获取用户信息接口获取userid参数值。

## Body
- none

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-teacher
updated_at: 2026-06-04 19:11:26
