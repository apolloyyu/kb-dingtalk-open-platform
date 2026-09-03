# 查询用户详情

doc_id: UbRx6mZowM
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/v2/user/get
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_get_member

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- userid (String, required): 用户的userId。
- optional: language(String)

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(Object), userid(String), unionid(String), name(String), avatar(String), state_code(String), manager_userid(String), mobile(String), hide_mobile(Boolean), telephone(String), job_number(String), title(String), email(String), work_place(String), remark(String), exclusive_account(Boolean), org_email(String), dept_id_list(Number[]), dept_order_list(Object[]), dept_id(Number), order(Number), extension(String), hired_date(Number), active(Boolean), real_authed(Boolean), senior(Boolean), admin(Boolean), boss(Boolean), leader_in_dept(Object[]), leader(Boolean), role_list(Object[]), id(Number), group_name(String), union_emp_ext(Object), union_emp_map_list(Object[]), corp_id(String), dept_position_list(DeptPosition[]), extension_i18n(Json)

## Limits
- 扩展属性，最大长度2000个字符。 **[!NOTE]** - 员工信息面板中添加的拓展字段内有值才返回。 - 企业内部应用，只有应用开通通讯录**邮箱等个人信息**权限，才会返回该字段。 - 第三方企业应用，不返回该字段。 - **重要提示**：直接添加新属性会覆盖原有属性值，需要先获取现有属性，然后将新属性追加到已有属性上，再进行整体更新。

source_url: https://open.dingtalk.com/document/development/query-user-details
updated_at: 2026-06-08 09:28:32
