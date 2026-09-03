# 销售机会

doc_id: A6YFNMtEGq
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/jzcrm/sales
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
- datatype (Long, required): 数据类型，固定值**158**。
- stamp (Long, required): 时间戳。
- data_userid (String, required): 创建人。
- xsh_customerid (String, required): 对应客户。
- xsh_title (String, required): 主题。
- xsh_date (String, required): 发现时间。
- optional: msgid(Long), data(Object), xsh_number(String), xsh_lxrid(String), xsh_lianxi(String), xsh_type(String), xsh_from(String), xsh_preside(String), xsh_provider(String), xsh_require(String), xsh_expdate(String), xsh_expmoney(String), xsh_moneynote(String), xsh_phase(String), xsh_knx(String), xsh_state(String), xsh_phasenote(String)

## Returns
- optional: time(String), msgid(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/add-or-edit-opportunities
updated_at: 2026-06-04 19:10:49
