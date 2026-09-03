# 获取数据列表

doc_id: mNfNgceNve
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/jzcrm/data
api_version: v2-new
app_types: 第三方企业应用
permissions: Jzcrm.Common.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- datatype (String, required): 数据类型。
- page (Long, required): 页码。
- pagesize (Long, required): 分页条数。

## Body
- none

## Returns
- optional: data(Array), detail(Map<String, String>), dataname(Map<String, String>), page(Long), pageSize(Long), totalCount(Long), time(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-data-list
updated_at: 2026-06-02 20:01:06
