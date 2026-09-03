# 发送邀请函

doc_id: OH12M9flPX
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/exclusive/partnerDepartments/invitations/send
api_version: v2-new
app_types: 第三方企业应用
permissions: Partner.Department.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- deptId (String, required): 部门ID。
- partnerNum (String, required): 伙伴编码。
- partnerLabelId (Long, required): 伙伴标签ID。
- phone (String, required): 手机号。
- orgAlias (String, required): 组织别名。

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/send-invitations
updated_at: 2026-06-02 19:14:52
