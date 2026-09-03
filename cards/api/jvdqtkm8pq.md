# 创建自定义部门下的班级

doc_id: jvdqtkm8pq
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/edu/customClasses
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
- customClass (Object, required): 班级信息。
- name (String, required): 班级名称。
- superId (Long, required): 上级部门ID，可通过调用获取部门列表接口获取dept_id参数值。
- operator (String, required): 操作人userId。

## Returns
- optional: result(Object), deptId(Long), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-classes-in-a-custom-department
updated_at: 2026-06-04 19:11:29
