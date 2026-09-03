# 新增钉钉待办任务

doc_id: ypO6yjZVTm
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/workrecord/add
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
- userid (String, required): 任务的执行人userid。
- create_time (Number, required): 待办时间，Unix时间戳。 **[!NOTE]** 该参数只影响待办显示的先后顺序。
- title (String, required): 待办任务的标题，最多50个字符。
- url (String, required): 待办任务的跳转链接。当链接是某个微应用链接时，希望在PC端工作台打开，可通过消息链接在PC端工作台打开实现。 **[!NOTE]** 待办跳转地址不支持跳转进入小程序。
- formItemList (FormItemVo[], required): 表单列表。
- content (String, required): 表单内容。
- optional: pcUrl(String), originator_user_id(String), source_name(String), pc_open_type(Number), biz_id(String)

## Returns
- optional: errcode(Number), errmsg(String), request_id(String), record_id(String)

## Limits
- 待办任务的标题，最多50个字符。
- - 每人每天最多收到一条表单内容相同的待办。触发这个限制，会返回错误码400001。
- - 每人每天最多收到100条待办。触发这个限制，会返回错误码400002。

source_url: https://open.dingtalk.com/document/development/new-to-do-items
updated_at: 2026-08-25 09:38:10
