# 分页查询客户列表

doc_id: WyhGYBn4H1
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/dvi/customers
api_version: v2-new
app_types: 企业内部应用
permissions: Dvi.Sale.Customer.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- teamCode (String, required): 团队或门店ID，可通过获取团队信息接口获取。
- optional: ownerUserId(String), startTime(Long), endTime(Long), nextToken(String), maxResults(Integer)

## Body
- none

## Returns
- optional: result(Array), id(String), name(String), teamCode(String), createAt(String), ownerUserId(String), totalCount(Integer), nextToken(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-listcustomer
updated_at: 2026-06-24 13:44:35
