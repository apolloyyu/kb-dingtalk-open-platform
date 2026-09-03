# 创建日志

doc_id: DvP1O1C2FE
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/report/create
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_report_manage

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- create_report_param (OapiCreateReportParam, required): 创建日志的参数对象。
- contents (OapiReportContentVo[], required): 日志内容数组，根据该日志模板中每一项信息传参。
- sort (Number, required): 写日志对应的模板某个字段的唯一序列ID，可调用获取模板详情接口获取sort参数值。
- type (Number, required): 写日志对应的模板某个字段的类型，可调用获取模板详情接口获取type参数值。 **[!NOTE]** 只支持文本类型日志组件，即type参数固定值为1，其他类型不支持。
- content_type (String, required): 日志内容的类型。 **[!NOTE]** - 目前支持markdown类型。 - 支持获取模板详情接口中，日志组件是**文本**的类型。
- content (String, required): 日志内容。 **[!NOTE]** - 只支持 Markdown 语法。 - 内容不能超过 1000 字符，超出的内容会被截断。
- key (String, required): 写日志对应的模板某个字段的标题，可调用获取模板详情接口获取field_name参数值。
- template_id (String, required): 模板ID，可调用获取模板详情接口获取id参数值。
- to_chat (Boolean, required): 发送日志到员工时是否发送单聊消息。 - **true**：发送日志消息给指定用户 - **false**：不单独发送消息
- dd_from (String, required): 日志来源，每个组织可以自己起一个唯一的来源标识，自定义的值。
- userid (String, required): 创建日志的员工userId。
- optional: to_userids(String[]), to_cids(String[])

## Returns
- optional: errmsg(String), errcode(Number), result(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/create-a-log
updated_at: 2026-05-27 13:10:11
