# 更新企业账号用户信息

doc_id: XT62t9idMV
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/v2/user/update
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
- userid (String, required): 员工的userId。
- dept_id_list (String, required): 所属部门ID列表。
- optional: name(String), hide_mobile(Boolean), telephone(String), job_number(String), manager_userid(String), title(String), email(String), org_email(String), work_place(String), remark(String), dept_order_list(DeptOrder[]), dept_id(Number), order(Number), dept_title_list(DeptTitle[]), extension(String), ext_attrs_update_mode(Number), senior_mode(Boolean), hired_date(Number), language(String), force_update_fields(String), org_email_type(String), loginId(String), init_password(String), send_password_to_user(Boolean), exclusive_mobile(String), avatarMediaId(String), nickname(String), dept_position_list(DeptPosition[]), extension_i18n(Json)

## Returns
- optional: errcode(Number), errmsg(String)

## Limits
- 员工名称，长度最大80个字符。
- 分机号，长度最大50个字符。 **[!NOTE]** 分机号是唯一的，企业内不能重复。
- 员工工号，长度最大50个字符。
- 职位，长度最大200个字符。
- 员工邮箱，长度最大50个字符。 **[!NOTE]** 员工邮箱是唯一的，企业内不能重复。
- 办公地点，长度最大100个字符。
- 备注，长度最大2000个字符。
- 扩展属性，长度最大2000个字符。 **[!NOTE]** - 手机上最多只能显示10个扩展属性。 - 如果给员工设置有10个扩展属性字段，更新时即使扩展属性字段值没变，也必须要将10个扩展属性字段都传进去。如果只传其中1个，那么剩下9个字段都会被清空。 - 在使用该参数前，需要先在**钉钉管理后台** > **设置** > **通讯录信息**增加该属性。 - 该字段的值支持链接类型填写，同时链接支持变量通配符自动替换，目前支持通配符有：userid和corpid。示例： `

source_url: https://open.dingtalk.com/document/development/update-dedicated-accounts-information
updated_at: 2026-05-27 13:09:06
