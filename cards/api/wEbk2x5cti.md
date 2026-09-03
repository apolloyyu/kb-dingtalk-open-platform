# 根据id获取待办卡片类型配置

doc_id: wEbk2x5cti
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/todo/users/{unionId}/configs/types/{cardTypeId}
api_version: v2-new
app_types: 企业内部应用
permissions: Todo.Todo.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过 获取用户token接口获取。

## Path params
- unionId (String, required): 用户的unionId，可通过查询用户详情接口获取。
- cardTypeId (String, required): 待办卡片类型ID，可通过创建待办卡片类型配置接口获取。

## Query params
- none

## Body
- none

## Returns
- optional: id(String), createdTime(Long), modifiedTime(Long), creatorId(String), modifierId(String), bizTag(String), requestId(String), cardType(Integer), icon(String), description(String), pcDetailUrlOpenMode(String), contentFieldList(Array), fieldKey(String), fieldType(String), nameI18n(Map), actionList(Array), actionKey(String), buttonStyleType(Integer), actionType(Integer), url(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/queries-the-to-do-card-type-configuration-details
updated_at: 2026-07-30 10:01:50
