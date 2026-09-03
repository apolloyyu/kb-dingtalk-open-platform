# 获取指定用户可见的审批表单列表

doc_id: UNCZI46dqz
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/workflow/processes/userVisibilities/templates
api_version: v2-new
app_types: 企业内部应用
permissions: Workflow.Form.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可通过获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- maxResults (Long, required): 分页大小，最大值100。
- nextToken (Long, required): 分页游标。 - 如果是首次调用，该参数传0。 - 如果是非首次调用，该参数传上次调用时返回的nextToken。
- optional: userId(String)

## Body
- none

## Returns
- optional: result(Object), processList(Array), name(String), url(String), iconUrl(String), processCode(String), dirId(String), dirName(String), nextToken(Long)

## Limits
- 分页大小，最大值100。
- 调用本接口，可根据员工的userId分页获取该用户可见的审批表单列表，每次最多获取100个表单。

source_url: https://open.dingtalk.com/document/development/obtains-a-list-of-approval-forms-visible-to-the-specified
updated_at: 2026-06-03 10:12:23
