# 创建钉钉待办任务

doc_id: H0z1RaakhS
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/todo/users/{unionId}/tasks
api_version: v2-new
app_types: 第三方企业应用
permissions: Todo.Todo.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证。 - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，授权后使用返回的**authCode** ，通过调用获取用户token接口获取。

## Path params
- unionId (String, required): 当前访问资源所归属用户的unionId，和创建者的unionId保持一致，通过调用查询用户详情接口获取unionid参数值。

## Query params
- optional: operatorId(String)

## Body
- subject (String, required): 待办标题，最大长度1024。
- optional: sourceId(String), creatorId(String), description(String), dueTime(Long), executorIds(Array of String), participantIds(Array of String), detailUrl(Object), appUrl(String), pcUrl(String), contentFieldList(Array), fieldKey(String), fieldValue(String), isOnlyShowExecutor(Boolean), priority(Integer), notifyConfigs(Object), dingNotify(String), sendTodoApn(String), sendAssistantChat(String), bizCategoryId(String), actionList(Array), title(String), actionType(Integer), param(Object), body(String), header(Map), url(String), actionKey(String), todoType(String), reminderTimeStamp(Long), remindNotifyConfigs(Object), thirdExtension(Map)

## Returns
- optional: id(String), subject(String), description(String), startTime(Long), dueTime(Long), finishTime(Long), done(Boolean), executorIds(Array of String), participantIds(Array of String), detailUrl(Object), pcUrl(String), appUrl(String), source(String), sourceId(String), createdTime(Long), modifiedTime(Long), creatorId(String), modifierId(String), bizTag(String), requestId(String), contentFieldList(Array), fieldKey(String), fieldValue(String), isOnlyShowExecutor(Boolean), priority(Integer), notifyConfigs(Object), dingNotify(String)

## Limits
- 待办标题，最大长度1024。
- 待办备注描述，最大长度4096。 - 创建第三方待办时，该字段无需传入，不会正常展示。
- 执行者的unionId，可调用查询用户详情接口获取unionid参数值，建议不超过100人。
- 参与者的unionId，可调用查询用户详情接口获取unionid参数值，建议不超过100人。
- APP端详情页url跳转地址，该字段长度限制为1024个字节。 - 创建个人待办时，该字段无需传入。 - 创建第三方待办时，需传入自身应用详情页链接。 如果创建第三方待办时配置了DING通知能力，appUrl需要支持以dingtalk协议打开。
- PC端详情页url跳转地址，该字段长度限制为1024个字节。 - 创建个人待办时，该字段无需传入。 - 创建第三方待办时，需传入自身应用详情页链接。
- 字段唯一标识，最大长度1024字节
- 字段值，最大长度1024字节

source_url: https://open.dingtalk.com/document/development/add-dingtalk-to-do-task
updated_at: 2026-06-04 19:09:50
