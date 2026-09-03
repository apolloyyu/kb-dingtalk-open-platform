# 添加审批评论

doc_id: ccTcPAeZLJ
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/process/instance/comment/add
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证，可通过获取企业内部应用的access_token接口获取。

## Body
- request (AddCommentRequest, required): 请求对象。
- process_instance_id (String, required): 审批实例ID，调用获取审批实例ID列表接口获取。
- text (String, required): 评论的内容。
- comment_userid (String, required): 评论人的userid。
- optional: file(File), attachments(Attachment[]), space_id(String), file_type(String), file_name(String), file_id(String), file_size(String), photos(String[])

## Returns
- optional: result(Boolean), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/add-an-approval-comment
updated_at: 2026-08-25 09:37:43
