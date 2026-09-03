# 批量设置企业群管理员

doc_id: 2e31sgGFPZ
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/im/subAdministrators
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_chat_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- openConversationId (String, required): 开放群ID。可以调用创建群会话接口获取openConversationId参数值。
- userIds (Array of String, required): 企业员工userid列表。可以调用获取部门用户userid列表接口获取userid_list参数值。
- role (Integer, required): 设置类型，取值： - **2**：添加为管理员 - **3**：删除该管理员

## Returns
- optional: success(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/batch-setup-group-administrator
updated_at: 2026-06-15 10:56:53
