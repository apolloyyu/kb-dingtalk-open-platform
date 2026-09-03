# 添加待入职员工

doc_id: 4SzJHa7lZL
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrm/preentries
api_version: v2-new
app_types: 企业内部应用
permissions: Pro.HrmPreentry.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- name (String, required): 待入职员工的姓名。
- mobile (String, required): 待入职员工的手机号。
- optional: preEntryTime(Long), agentId(Long), groups(Array), groupId(String), sections(Array), oldIndex(Integer), empFieldVOList(Array), value(String), fieldCode(String), needSendPreEntryMsg(Boolean)

## Returns
- optional: tmpUserId(String)

## Limits
- 待入职员工花名册分组列表，建议不超过5个。
- 分组内字段列表，建议不超过5个。
- 分组内字段信息列表，建议不超过5个。

source_url: https://open.dingtalk.com/document/development/add-employees-to-be-hired-supports-system-and-custom-fields
updated_at: 2026-06-04 19:10:26
