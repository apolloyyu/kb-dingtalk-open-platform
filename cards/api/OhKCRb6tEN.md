# 销售换货单

doc_id: OhKCRb6tEN
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/jzcrm/exchanges
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
- datatype (Long, required): 数据类型，固定值**228**。
- stamp (Long, required): 时间戳。
- data_userid (String, required): 创建人。
- hh_inlibid (String, required): 换入仓库。
- hh_outlibid (String, required): 换出仓库。
- hh_title (String, required): 主题。
- hh_number (String, required): 换货单号。
- optional: msgid(Long), data(Object), hh_customerid(String), hh_orderid(String), hh_type(String), hh_date(String), hh_inempid(String), hh_intime(String), hh_outempid(String), hh_outtime(String), hh_remark(String), hh_state(String), child_mx(String)

## Returns
- optional: time(String), msgid(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/add-or-edit-a-sales-order
updated_at: 2026-06-02 20:01:01
