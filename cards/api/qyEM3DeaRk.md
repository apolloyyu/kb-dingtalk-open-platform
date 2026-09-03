# 获取多个表单实例ID

doc_id: qyEM3DeaRk
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/yida/forms/instances/ids/{appType}/{formUuid}
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Yida.Form.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- appType (String, required): 应用编码。
- formUuid (String, required): 表单ID。

## Query params
- optional: pageNumber(Integer), pageSize(Integer)

## Body
- systemToken (String, required): 应用密钥。
- userId (String, required): 用户userid。
- optional: modifiedToTimeGMT(String), modifiedFromTimeGMT(String), language(String), searchFieldJson(String), originatorId(String), createToTimeGMT(String), createFromTimeGMT(String), useAlias(Boolean)

## Returns
- optional: totalCount(Long), pageNumber(Long), data(Array of String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-searchformdataidlist-v2
updated_at: 2026-06-15 10:44:14
