# 合同订单

doc_id: gWQ5uO3y4I
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/jzcrm/orders
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
- datatype (Long, required): 数据类型，固定填写**150**。
- stamp (Long, required): 时间戳。
- data_userid (String, required): 创建人。
- ht_customerid (String, required): 对应客户。
- ht_date (String, required): 签单日期。
- ht_preside (String, required): 所有者。
- ht_state (String, required): 状态，取值。 - 执行中 - 结束 - 意外终止
- ht_summoney (String, required): 总金额。
- ht_order (String, required): 单据类型，取值。 - 合同 - 合同订单 - 店面单
- optional: msgid(Long), data(Object), ht_title(String), ht_number(String), ht_lxrid(String), ht_lxrinfo(String), ht_xshid(String), ht_type(String), ht_paymode(String), ht_begindate(String), ht_cusub(String), ht_wesub(String), ht_moneyzhekou(String), ht_kjmoney(String), ht_fjmoneylx(String), ht_fjmoney(String), ht_summemo(String), ht_deliplace(String), ht_enddate(String), ht_wuliutype(String), ht_yunfeimoney(String), fahuoaddressid(String), ht_contract(String), ht_remark(String), child_mx(String)

## Returns
- optional: time(String), msgid(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/add-or-edit-contract-orders
updated_at: 2026-06-02 20:00:59
