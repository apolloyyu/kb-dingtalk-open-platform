# 创建流程中心待处理任务

doc_id: mxGLeu4NYE
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/processCentres/tasks
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_aflow

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- processInstanceId (String, required): OA审批流程实例ID，可调用创建实例接口获取`processInstanceId`参数值。
- tasks (Array, required): 任务列表，最多20个元素。
- optional: activityId(String), userId(String), url(String), customData(String), dueTimestamp(Long), featureConfig(Object), features(Array), name(String), pcUrl(String), mobileUrl(String), runType(String), callback(Object), appUuid(String), apiKey(String), version(String), config(String)

## Returns
- optional: result(Array), taskId(Long), userId(String), success(Boolean)

## Limits
- 自定义审批节点ID，自定义参数，最大长度256字符。
- 任务列表，最多20个元素。
- 待办事项跳转URL，最大长度1024字符。 **[!NOTE]** - 创建审批实例里的url，实现的是钉钉审批应用里的审批单跳转。 - 本接口的url，实现的是钉钉待办页面，对应的待办卡片的跳转。 - 钉钉的待办页面，同时支持移动端和PC端，所以本接口传的url参数，它所对应的页面需要适配移动端和PC端。
- 用户自定义数据，页面跳转时将通过url参数回传，最大长度500字符。
- 三方自定义的pc端跳转链接，最大长度1024字符。
- 三方自定义的手机端跳转链接，最大长度1024字符。
- 三方进行自定义配置的功能模块对应的配置信息，最大长度1024字符。

source_url: https://open.dingtalk.com/document/development/create-pending-tasks-in-process-center
updated_at: 2026-06-02 15:54:12
