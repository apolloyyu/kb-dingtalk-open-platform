# 授权预览审批附件

doc_id: OZO8mhzxQZ
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/processinstance/cspace/preview
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- request (GrantCspaceRequest, required): 请求信息。
- process_instance_id (String, required): 实例ID： - 企业内部应用，通过获取审批实例ID列表接口获取。 - 第三方企业应用，通过推送的审批事件中获取，参考biz_type=22。
- file_id (String, required): 审批附件ID。 **[!NOTE]** file_id必须与发起审批实例中附件组件中的文件fileId保持一致，否则出现无权限错误信息。
- userid (String, required): 授权允许预览附件的用户userid。
- optional: agentid(Number), fileid_list(String[])

## Returns
- optional: errmsg(String), result(AppSpaceResponse), space_id(Number), errcode(Number), request_id(String)

## Limits
- 附件ID列表，支持批量授权，最大列表长度：20。

source_url: https://open.dingtalk.com/document/development/preview-authorization-attachment
updated_at: 2026-08-25 09:37:48
