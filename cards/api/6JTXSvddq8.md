# 更新外部联系人

doc_id: 6JTXSvddq8
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/extcontact/update
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_ext_write

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- contact (OpenExtContact, required): 外部联系人信息。
- label_ids (Number[], required): 标签列表，可调用获取外部联系人列表接口查询标签信息。 参考企业如何自定义标签组添加自定义标签。 每次调用最多传20个labelId。
- follower_user_id (String, required): 负责人的userId。
- name (String, required): 外部联系人的姓名。
- user_id (String, required): 该外部联系人的userId，可调用获取外部联系人列表接口获取。
- optional: title(String), share_dept_ids(Number[]), address(String), remark(String), company_name(String), share_user_ids(String[])

## Returns
- optional: errcode(Number), request_id(String)

## Limits
- 标签列表，可调用获取外部联系人列表接口查询标签信息。 参考企业如何自定义标签组添加自定义标签。 每次调用最多传20个labelId。
- 共享给的部门ID，可调用获取子部门ID列表接口获取。 每次调用最多传20个部门ID。
- 共享给的员工userid列表。 每次调用最多传20个labelId。

source_url: https://open.dingtalk.com/document/development/update-enterprise-external-contacts
updated_at: 2026-05-27 13:09:32
