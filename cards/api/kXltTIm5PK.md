# 创建班级

doc_id: kXltTIm5PK
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/class/create
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_edu_safe

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- open_class (OpenClass, required): 班级信息。
- only_use_nick (String, required): 是否只展现nick。
- name (String, required): 班级名。
- class_level (Number, required): 每个年级下班级级数，1班为1，2班为2。
- super_id (Number, required): 年级ID，可调用获取部门列表接口获取dept_type为grade时的dept_id参数值。
- operator (String, required): 钉钉企业管理员userId，即有家校通讯录管理范围的管理员userId。
- optional: nick(String)

## Returns
- optional: result(OpenClassCreateResponse), dept_id(Number), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-a-class
updated_at: 2026-06-08 09:48:13
