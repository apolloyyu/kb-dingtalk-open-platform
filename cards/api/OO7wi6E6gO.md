# 获取AI销售管理客户洞察信息

doc_id: OO7wi6E6gO
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/dvi/customers/insights
api_version: v2-new
app_types: 企业内部应用
permissions: Dvi.Sale.Customer.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- customerId (String, required): 客户ID，可通过调用分页查询客户列表接口获取。

## Body
- none

## Returns
- optional: result(Object), tag(Object), aiTag(Array), code(String), name(String), value(String), userTag(Array), intention(Object), description(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getcustomerinsight
updated_at: 2026-06-24 13:44:38
