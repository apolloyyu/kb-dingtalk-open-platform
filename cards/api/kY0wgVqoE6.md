# 获取离职员工列表

doc_id: kY0wgVqoE6
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/hrm/employees/dismissions
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_hrm_read_user

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: nextToken(Long), maxResults(Integer)

## Body
- none

## Returns
- optional: nextToken(Long), hasMore(Boolean), userIdList(Array of String)

## Limits
- 每页条目数，默认值30，最大值50。

source_url: https://open.dingtalk.com/document/development/obtain-the-list-of-employees-who-have-left
updated_at: 2026-06-04 19:10:26
