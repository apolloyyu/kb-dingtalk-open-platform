# 查询企业账号用户详情

doc_id: 7TMeqD6H0C
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
- userid (String, required): 用户的UserId。
- optional: language(String), login_id(String)

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(Object), userid(String), unionid(String), name(String), avatar(String), state_code(String), mobile(String), hide_mobile(Boolean), telephone(String), job_number(String), title(String), email(String), org_email(String), work_place(String), remark(String), dept_id_list(Number[]), dept_order_list(Object[]), dept_id(Number), order(Number), extension(String), hired_date(Number), active(Boolean), real_authed(Boolean), senior(Boolean), admin(Boolean), boss(Boolean), leader_in_dept(Object[]), leader(Boolean), role_list(Object[]), id(Number), group_name(String), exclusive_account(Boolean), union_emp_ext(Object), union_emp_map_list(Object[]), corp_id(String), exclusive_account_type(String), login_id(String), manager_userid(String), org_email_type(String), nickname(String), exclusive_account_corp_name(String), exclusive_account_corp_id(String), disable_status(Boolean)

## Limits
- 登录名，非空则忽略userid。 **[!NOTE]** 使用登录名进行查询，仅限归属于本企业的钉钉自建企业账号
- 扩展属性，最大长度2000个字符。 **[!NOTE]** - 企业内部应用如果没有返回该字段，需要检查当前应用通讯录权限中**邮箱等个人信息**权限是否开启。 - 员工信息面板中添加的拓展字段内有值才返回。 - 第三方企业应用不返回该字段。

source_url: https://open.dingtalk.com/document/development/queries-the-details-of-a-dedicated-account
updated_at: 2026-05-27 13:09:07
