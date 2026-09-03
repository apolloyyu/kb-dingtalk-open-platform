# 获取流程实例

doc_id: ZbDnTIgGk1
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/yida/processes/instances
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Yida.Process.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: pageNumber(Integer), pageSize(Integer)

## Body
- appType (String, required): 应用编码，获取方式可参考下图所示：
- systemToken (String, required): 应用密钥，获取方式可参考下图所示：
- userId (String, required): 用户的userId，可通过获取部门用户userid列表接口获取。
- formUuid (String, required): 页面编码，获取方式可参考下图所示：
- optional: language(String), searchFieldJson(String), originatorId(String), createFromTimeGMT(String), createToTimeGMT(String), modifiedFromTimeGMT(String), modifiedToTimeGMT(String), taskId(String), instanceStatus(String), approvedResult(String), orderConfigJson(String), useAlias(Boolean)

## Returns
- optional: totalCount(Long), pageNumber(Long), data(Array), createTimeGMT(String), processInstanceId(String), actionExecutor(Array), name(Object), nameInEnglish(String), type(String), nameInChinese(String), deptName(String), userId(String), email(String), approvedResult(String), formUuid(String), processCode(String), modifiedTimeGMT(String), originator(Object), title(String), instanceStatus(String), version(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getinstances-v2
updated_at: 2026-06-15 10:44:11
