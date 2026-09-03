# 获取实例ID列表

doc_id: 7fWOTeVhWA
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/yida/processes/instanceIds
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Yida.Process.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: pageSize(Integer), pageNumber(Integer)

## Body
- formUuid (String, required): 表单的页面编码，获取方式如下图所示：
- systemToken (String, required): 应用密钥。
- userId (String, required): 用户userid，可通过查询用户详情或获取部门用户userid列表接口获取。
- appType (String, required): 应用编码，获取方式如下图所示：
- optional: modifiedToTimeGMT(String), modifiedFromTimeGMT(String), language(String), searchFieldJson(String), instanceStatus(String), approvedResult(String), originatorId(String), createToTimeGMT(String), taskId(String), createFromTimeGMT(String), useAlias(Boolean)

## Returns
- optional: totalCount(Long), pageNumber(Long), data(Array of String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getinstanceidlist-v2
updated_at: 2026-06-15 10:44:10
