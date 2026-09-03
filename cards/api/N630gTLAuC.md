# 获取待入职员工列表

doc_id: N630gTLAuC
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/querypreentry
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_hrm_read_user

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- offset (Number, required): 分页游标，从0开始。根据返回结果里的next_cursor是否为空来判断是否还有下一页，且再次调用时offset设置成next_cursor的值。
- size (Number, required): 分页大小，最大50。

## Returns
- optional: result(PageResult), next_cursor(Number), data_list(String[]), errcode(Number), errmsg(String), success(Boolean), request_id(String)

## Limits
- 分页大小，最大50。

source_url: https://open.dingtalk.com/document/development/intelligent-personnel-query-the-list-of-employees-to-be-hired
updated_at: 2026-05-29 09:13:54
