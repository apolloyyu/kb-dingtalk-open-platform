# 创建钉钉自建企业账号

doc_id: AU7fEEmkyB
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/v2/user/create
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_manage_addresslist

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- exclusive_account (Boolean, required): 必须填true，表示要创建企业账号。 **[!NOTE]** 仅适用于企业账号。
- exclusive_account_type (String, required): 必须填dingtalk，表示钉钉自建企业账号。 **[!NOTE]** 仅适用于钉钉自建企业账号。
- login_id (String, required): 钉钉自建企业账号的登录名。 **[!NOTE]** 建议不要携带手机号、邮箱链接等信息，避免注册短信被运营商管控拦截，
- init_password (String, required): 钉钉自建企业账号的初始密码，初始密码至少8个字符。 **[!NOTE]** - 不能全是字母或者数字。 - 建议不要携带手机号、邮箱、链接等信息，避免注册短信被运营商管控拦截，
- name (String, required): 员工名称，长度最大80个字符。
- dept_id_list (String, required): 所属部门ID列表，多个部门ID使用`英文,`隔开，每次调用最多传100个部门ID。
- optional: userid(String), send_password_to_user(Boolean), telephone(String), job_number(String), title(String), email(String), org_email(String), org_email_type(String), work_place(String), remark(String), dept_order_list(Object[]), dept_id(Number), order(Number), dept_title_list(Object[]), extension(String), senior_mode(Boolean), hired_date(Number), manager_userid(String), exclusive_mobile(String), avatarMediaId(String), nickname(String)

## Returns
- optional: errcode(Number), errmsg(String), result(Object), userid(String), unionId(String)

## Limits
- 员工唯一标识ID（不可修改），长度为1~64个字符。 **[!NOTE]** - 企业内必须唯一。 - 如果不传，将自动生成一个userId。
- 钉钉自建企业账号的初始密码，初始密码至少8个字符。 **[!NOTE]** - 不能全是字母或者数字。 - 建议不要携带手机号、邮箱、链接等信息，避免注册短信被运营商管控拦截，
- 员工名称，长度最大80个字符。
- 所属部门ID列表，多个部门ID使用`英文,`隔开，每次调用最多传100个部门ID。
- 分机号，长度最大50个字符。 **[!NOTE]** 分机号是唯一的，企业内不能重复。
- 员工工号，长度最大为50个字符。
- 职位，长度最大为200个字符。
- 员工个人邮箱，长度最大50个字符。 **[!NOTE]** 员工邮箱是唯一的，企业内不能重复。

source_url: https://open.dingtalk.com/document/development/create-dingtalk-user-created-dedicated-account
updated_at: 2026-05-27 13:09:03
