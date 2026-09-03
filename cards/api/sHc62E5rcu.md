# 邀请其他组织企业账号加入

doc_id: sHc62E5rcu
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
- outer_exclusive_corpid (String, required): 需要添加的企业账号所属的corpId。
- outer_exclusive_userid (String, required): 需要添加的企业账号所属的userId。
- name (String, required): 员工名称，长度最大80个字符。
- dept_id_list (String, required): 所属部门ID列表，多个部门ID使用`英文,`隔开，每次调用最多传100个部门ID。
- optional: userid(String), telephone(String), job_number(String), title(String), email(String), org_email(String), org_email_type(String), work_place(String), remark(String), dept_order_list(Object[]), dept_id(Number), order(Number), dept_title_list(Object[]), extension(String), senior_mode(Boolean), hired_date(Number), manager_userid(String)

## Returns
- optional: errcode(Number), errmsg(String), result(Object), userid(String), unionId(String)

## Limits
- 员工唯一标识ID（不可修改），长度为1~64个字符。 **[!NOTE]** - 企业内必须唯一。 - 如果不传，将自动生成一个userid。
- 员工名称，长度最大80个字符。
- 所属部门ID列表，多个部门ID使用`英文,`隔开，每次调用最多传100个部门ID。
- 分机号，长度最大50个字符。 **[!NOTE]** 分机号是唯一的，企业内不能重复。
- 员工工号，长度最大为50个字符。
- 职位，长度最大为200个字符。
- 员工个人邮箱，长度最大50个字符。 **[!NOTE]** 员工邮箱是唯一的，企业内不能重复。
- 员工的企业邮箱，长度最大100个字符。 **[!NOTE]** 需满足以下条件，此字段才生效：员工已开通企业邮箱。

source_url: https://open.dingtalk.com/document/development/invite-other-organization-specific-accounts-to-join
updated_at: 2026-05-27 13:09:04
