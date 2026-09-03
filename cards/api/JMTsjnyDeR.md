# 获取在职员工列表

doc_id: JMTsjnyDeR
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/queryonjob
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
- status_list (String, required): 在职员工状态筛选，可以查询多个状态。不同状态之间使用英文逗号分隔。 - **2**：试用期 - **3**：正式 - **5**：待离职 - **-1**：无状态
- offset (Number, required): 分页游标，从0开始。根据返回结果里的next_cursor是否为空来判断是否还有下一页，且再次调用时offset设置成next_cursor的值。
- size (Number, required): 分页大小，最大50。

## Returns
- optional: result(PageResult), data_list(String), next_cursor(Number), errcode(Number), errmsg(String), success(Boolean), request_id(String)

## Limits
- 分页大小，最大50。
- - 该接口只能获取企业开通“智能人事”应用之后的员工信息，获取不到开通之前的员工信息。

source_url: https://open.dingtalk.com/document/development/intelligent-personnel-query-the-list-of-on-the-job-employees-of-the
updated_at: 2026-06-23 10:40:26
