# 创建用户

doc_id: wBWOPgQnfQ
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
- name (String, required): 员工名称，长度最大80个字符。
- mobile (String, required): 手机号码，企业内必须唯一，不可重复。 - 如果是国际号码、中国香港、中国澳门和中国台湾地区号码，请使用+xx-xxxxxx的格式。 - 如果公司注册地址是非中国大陆地区，则在添加用户时，手机号要使用+86-xxxxxx格式。 **[!NOTE]** 登录钉钉管理后台，查看企业注册地址。iShot2022-05-31 15
- dept_id_list (String, required): 所属部门id列表，每次调用最多传100个部门ID。
- optional: userid(String), hide_mobile(Boolean), telephone(String), job_number(String), title(String), email(String), org_email(String), org_email_type(String), work_place(String), remark(String), dept_order_list(Object[]), dept_id(Number), order(Number), dept_title_list(Object[]), extension(Object), senior_mode(Boolean), hired_date(Number), manager_userid(String), login_email(String), dept_position_list(DeptPosition[]), extension_i18n(Json)

## Returns
- optional: errcode(Number), errmsg(String), result(Object), userid(String), unionId(String)

## Limits
- 员工唯一标识ID（不可修改），企业内必须唯一。 长度为1~64个字符，如果不传，将自动生成一个userid。
- 员工名称，长度最大80个字符。
- 分机号，长度最大50个字符。 **[!NOTE]** 分机号是唯一的，企业内不能重复。
- 员工工号，长度最大为50个字符。
- 职位，长度最大为200个字符。
- 员工个人邮箱，长度最大50个字符。 **[!NOTE]** 员工邮箱是唯一的，企业内不能重复。
- 员工的企业邮箱，长度最大100个字符。 **[!NOTE]** 需满足以下条件，此字段才生效：员工的企业邮箱已开通。
- 办公地点，长度最大100个字符。

source_url: https://open.dingtalk.com/document/development/user-information-creation
updated_at: 2026-06-30 17:29:32
