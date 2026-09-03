# 发送钉盘文件给指定用户

doc_id: uE3OPEwzXz
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/cspace/add_to_single_chat
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- file_name (String, required): 文件名包含扩展名，需要utf-8 urlEncode。
- media_id (String, required): 文件media_id，调用获取文件上传信息接口或者提交文件接口获取。 **[!NOTE]** 参数需要utf-8 urlEncode处理。
- userid (String, required): 文件接收人的userid。
- agent_id (String, required): 文件发送者应用的AgentId。 - 企业内部应用可以在开发者后台的应用详情页获取。 - 第三方企业应用可以调用获取企业授权信息接口获取。

## Returns
- optional: errmsg(String), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/sends-a-file-to-a-specified-user
updated_at: 2026-08-25 09:38:13
