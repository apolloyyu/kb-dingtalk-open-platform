# 发货单

doc_id: VrQubVTnLr
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/jzcrm/invoices
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
- datatype (Long, required): 数据类型，固定值**169**。
- stamp (Long, required): 时间戳。
- data_userid (String, required): 创建人。
- fh_customerid (String, required): 对应客户。
- fh_date (String, required): 发货日期。
- fh_number (String, required): 发货单号。
- fh_mode (String, required): 发货方式。
- optional: msgid(Long), data(Object), fh_htorder(String), fh_title(String), fh_yunfei(String), fh_jianshu(String), fh_kg(String), fh_shipper(String), fh_preside(String), fh_lxrid(String), fh_linkman(String), fh_tel(String), fh_handset(String), fh_post(String), fh_address(String), fh_email(String), fh_msn(String), fh_remark(String), fh_state(String), child_mx(String)

## Returns
- optional: time(String), msgid(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/add-or-edit-invoices
updated_at: 2026-06-02 20:01:00
