# 采购单

doc_id: 6BUbMt1lWj
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/jzcrm/purchases
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
- datatype (Long, required): 数据类型，固定值**153**。
- stamp (Long, required): 时间戳。
- data_userid (String, required): 创建人。
- gysid (String, required): 供应商。
- cgno (String, required): 采购单号。
- summoney (String, required): 采购金额。
- cgdate (String, required): 采购日期。
- cg_zxstate (String, required): 执行状态，取值。 - 执行中 - 结束 - 意外终止
- optional: msgid(Long), data(Object), order_khid(String), cgname(String), gys_lxrid(String), gys_lxrinfo(String), cgtype(String), gysjingban(String), empid(String), cg_moneyzhekou(String), cg_kjmoney(String), cg_fjmoneylx(String), cg_fjmoney(String), order_htid(String), cgremark(String), child_mx(String)

## Returns
- optional: time(String), msgid(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/edit-purchase-order
updated_at: 2026-06-04 19:10:50
