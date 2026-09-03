# 联系人

doc_id: IRmWewIe79
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/jzcrm/contacts
api_version: v2-new
app_types: 第三方企业应用
permissions: Jzcrm.Common.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- datatype (Long, required): 数据类型，固定值**197**。
- stamp (Long, required): 时间戳。
- data_userid (String, required): 创建人。
- lxr_customerid (String, required): 对应客户。
- lxr_name (String, required): 姓名。
- optional: msgid(Long), data(Object), lxr_handset(String), lxr_worktel(String), lxr_sex(String), lxr_group(String), lxr_preside(String), lxr_cttype(String), lxr_ctnumber(String), lxr_chengwei(String), lxr_type(String), lxr_department(String), lxr_headship(String), lxr_dingtalk(String), lxr_fax(String), lxr_wangwang(String), lxr_email(String), lxr_weixin(String), lxr_qq(String), lxr_tel(String), lxr_pst(String), lxr_skype(String), lxr_address(String), lxr_birthday(String), lxr_like(String), lxr_remark(String), lxr_photo(String)

## Returns
- optional: time(String), msgid(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/add-or-edit-contacts
updated_at: 2026-06-02 20:00:59
