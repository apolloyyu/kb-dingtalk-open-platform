# 客户资料

doc_id: yr5XPoBYgr
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/jzcrm/customers
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
- datatype (Long, required): 数据类型，固定值**148**。
- stamp (Long, required): 时间戳，单位：秒。
- data_userid (String, required): 创建人。
- kh_class (String, required): 类别，取值。 - 企业客户 - 个人客户 - 供应商 - 个人供应商
- kh_name (String, required): 客户名称。
- optional: msgid(Long), data(Object), kh_pkhid(String), kh_sex(String), kh_shortname(String), kh_industry(String), kh_employees(String), kh_address(String), kh_country(String), kh_province(String), kh_city(String), kh_coaddress(String), kh_hottype(String), kh_hotlevel(String), kh_hotfl(String), kh_hotmemo(String), kh_type(String), kh_status(String), kh_sn(String), kh_handset(String), kh_email(String), kh_dingtalk(String), kh_tel(String), kh_weixin(String), kh_qq(String), kh_skype(String), kh_wangwang(String), kh_worktel(String), kh_fax(String), kh_pst(String), kh_department(String), kh_appellation(String), kh_preside(String), kh_headship(String), kh_web(String), kh_befontof(String), kh_from(String), kh_billinfo(String), kh_info(String), kh_ralagrade(String), kh_creditgrade(String), kh_valrating(String), kh_cttype(String), kh_ctnumber(String), kh_contype(String), kh_remark(String), kh_jibie(String)

## Returns
- optional: time(String), msgid(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/add-or-edit-customer-profile
updated_at: 2026-06-02 20:00:57
