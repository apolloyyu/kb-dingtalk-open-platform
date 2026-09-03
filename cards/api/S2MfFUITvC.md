# 获取企业部门聊天数据（部门维度）

doc_id: S2MfFUITvC
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/kac/datav/dept/chat/summary/list
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- request (ImSummaryRequest, required): 请求对象。
- data_id (String, required): 日期标识。
- cursor (Number, required): 分页游标。首页请使用0，之后直接使用返回结果中next_cursor的值。
- size (Number, required): 分页大小，不超过100。

## Returns
- optional: result(Object), data(Object[]), send_message_avg_cnt(String), send_group_message_user_cnt(Number), send_single_message_user_cnt(Number), send_message_user_cnt(Number), group_message_cnt(Number), single_message_cnt(Number), message_cnt(Number), dept_name(String), dept_id(Number), group_send_file_message_cnt(String), next_cursor(Number), has_more(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- 分页大小，不超过100。
- 最近1天发消息数。
- 最近1天发送群文件数。
- > 1. 为了更好支持组织对钉钉数据分析和管理的需求，钉钉数据资产平台将统一所有数据资产相关的产品和服务，从数据层、功能层、业务层做升级，提供更好的服务体验。为此，我们将数据资产类 OpenAPI 接口的使用路径和产品定位做了调整，本开发者文档中所述 OpenAPI 接口及 60 个其他的数据资产类OpenAPI接口，已于 2023 年 9 月 1 日**关闭开发者后台应用开发的权限申请入口**，客户可以通过钉钉数据资产平台获取相应的数据服务。

source_url: https://open.dingtalk.com/document/development/dingtalk-chat-information-in-key-accounts
updated_at: 2026-08-27 14:07:52
