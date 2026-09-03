# 报价记录

doc_id: zOdbQl1xm9
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/jzcrm/quotationRecords
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Jzcrm.Common.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- datatype (Long, required): 数据类型，固定值**161**。
- stamp (Long, required): 时间戳。
- data_userid (String, required): 创建人。
- bj_customerid (String, required): 对应客户。
- bj_bjren (String, required): 报价人。
- bj_date (String, required): 报价日期。
- bj_price (String, required): 报价（总）。
- optional: msgid(Long), data(Object), bj_title(String), bj_number(String), bj_state(String), bj_jshren(String), bj_lianxi(String), bj_xshid(String), bj_moneyzhekou(String), bj_kjmoney(String), bj_fjmoneylx(String), bj_fjmoney(String), bj_jfremark(String), bj_fkremark(String), bj_bzremark(String), bj_remark(String), child_mx(String)

## Returns
- optional: time(String), msgid(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/add-or-edit-quotation-records
updated_at: 2026-06-04 19:10:50
