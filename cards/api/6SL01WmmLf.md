# 更新学生

doc_id: 6SL01WmmLf
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/edu/students/infos
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_edu_safe

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userId (String, required): 学生ID，可调用获取人员列表接口获取userid参数值。
- operator (String, required): 钉钉企业管理员的userId。
- classId (Long, required): 班级ID，可调用获取部门列表接口获取dept_type为class时的dept_id参数值。
- name (String, required): 学生姓名。
- bizId (String, required): 业务的唯一ID，自定义值，每次调用保持唯一。
- studentNo (String, required): 学生学号，可调用获取人员列表接口获取student_no参数值。

## Returns
- optional: success(Boolean)

## Limits
- 业务的唯一ID，自定义值，每次调用保持唯一。

source_url: https://open.dingtalk.com/document/development/api-updatestudent
updated_at: 2026-06-03 09:13:44
