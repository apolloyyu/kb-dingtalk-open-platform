# 获取部门用户详情

doc_id: fPaCqtLCEL
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/v2/user/list
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_get_department_member

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- dept_id (Number, required): 部门ID，可调用获取部门列表获取，如果是根部门，该参数传1。 **[!NOTE]** 只获取当前部门下的员工信息，不包含子部门内的员工。
- cursor (Number, required): 分页查询的游标，最开始传0，后续传返回参数中的next_cursor值。
- size (Number, required): 分页大小。
- optional: order_field(String), contain_access_limit(Boolean), language(String)

## Returns
- optional: errcode(Number), errmsg(String), result(Object), has_more(Boolean), next_cursor(Number), list(Object[]), userid(String), unionid(String), name(String), avatar(String), state_code(String), mobile(String), hide_mobile(Boolean), telephone(String), job_number(String), title(String), email(String), org_email(String), work_place(String), remark(String), dept_id_list(Number[]), dept_order(Number), extension(String), hired_date(Number), active(Boolean), admin(Boolean), boss(Boolean), leader(Boolean), exclusive_account(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-the-complete-information-of-a-department-user
updated_at: 2026-06-08 09:28:35
