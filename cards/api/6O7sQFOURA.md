# 添加老师

doc_id: 6O7sQFOURA
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/teacher/create
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
- class_id (Number, required): 班级ID，可调用获取部门列表接口获取dept_type为class时的dept_id参数值。
- adviser (Number, required): 是否为班主任。 - **0**：非班主任 - **1**：班主任
- userid (String, required): 老师的userId。
- operator (String, required): 钉钉企业管理员userId，即有家校通讯录管理范围的管理员userId。
- optional: biz_id(String)

## Returns
- optional: result(OpenEduUserCreateResponse), biz_id(String), userid(String), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- 业务ID，自定义值，每次调用该参数保持唯一。

source_url: https://open.dingtalk.com/document/development/add-teacher
updated_at: 2026-06-08 09:48:17
