# 创建专属帐号用户

doc_id: 4GyKRTViVq
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/v2/user/create
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的访问凭证，通过获取企业内部应用的access_token接口获取。

## Body
- name (String, required): 员工名称，长度最大80个字符。
- dept_id_list (String, required): 所属部门ID列表，多个部门ID使用`英文,`隔开，每次调用最多传100个部门ID。
- exclusive_account (Boolean, required): 是否专属帐号。 - **true**：不能指定**loginEmail**或**mobile**。 - **false**：是否创建专属帐号 **[!NOTE]** 仅适用于专属帐号。
- optional: userid(String), telephone(String), job_number(String), title(String), email(String), org_email(String), org_email_type(String), work_place(String), remark(String), dept_order_list(Object[]), dept_id(Number), order(Number), dept_title_list(Object[]), extension(String), senior_mode(Boolean), hired_date(Number), manager_userid(String), exclusive_account_type(String), login_id(String), init_password(String), exclusive_mobile(String), outer_exclusive_corpid(String), outer_exclusive_userid(String), avatarMediaId(String), nickname(String)

## Returns
- optional: errcode(Number), errmsg(String), result(Object), userid(String), unionId(String)

## Limits
- 员工唯一标识ID（不可修改），企业内必须唯一。 长度为1~64个字符，如果不传，将自动生成一个userid。
- 员工名称，长度最大80个字符。
- 所属部门ID列表，多个部门ID使用`英文,`隔开，每次调用最多传100个部门ID。
- 分机号，长度最大50个字符。 **[!NOTE]** 分机号是唯一的，企业内不能重复。
- 员工工号，长度最大为50个字符。
- 职位，长度最大为200个字符。
- 员工个人邮箱，长度最大50个字符。 **[!NOTE]** 员工邮箱是唯一的，企业内不能重复。
- 员工的企业邮箱，长度最大100个字符。 **[!NOTE]** 需满足以下条件，此字段才生效：员工已开通企业邮箱。

source_url: https://open.dingtalk.com/document/development/create-dedicated-accounts
updated_at: 2026-08-25 09:36:48
