# 查询待办列表

doc_id: w8VdPjes6f
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/process/workrecord/task/query
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- userid (String, required): 要查询的执行人userid。
- offset (Number, required): 分页游标。支持分页查询，与count参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。
- count (Number, required): 分页大小，最大50。
- status (Number, required): 待办事项的状态： - **0**：待处理 - **-1**：已经移除

## Returns
- optional: result(PageResult), has_more(Boolean), list(WorkRecordVo[]), url(String), task_id(String), instance_id(String), title(String), forms(FormItemVo[]), errcode(Number), errmsg(String), request_id(String)

## Limits
- 分页大小，最大50。

source_url: https://open.dingtalk.com/document/development/query-a-user-s-to-do-items
updated_at: 2026-08-25 13:50:01
