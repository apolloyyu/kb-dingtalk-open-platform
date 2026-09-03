# 创建实例

doc_id: pMujhtQZs9
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/processCentres/instances
api_version: v2-new
app_types: 第三方企业应用
permissions: Workflow.Instance.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- processCode (String, required): 审批模板code，可通过调用获取模板code接口获取processCode参数值。
- originatorUserId (String, required): 审批实例发起人的userId。
- url (String, required): 第三方审批系统中审批单详情页地址，最大长度1024字符。
- optional: formComponentValueList(Array), name(String), value(String), extValue(String), id(String), bizAlias(String), componentType(String), title(String), notifiers(Array), userid(String), position(String), featureConfig(Object), features(Array), pcUrl(String), mobileUrl(String), runType(String), callback(Object), appUuid(String), apiKey(String), version(String), config(String), bizData(String)

## Returns
- optional: result(Object), processInstanceId(String)

## Limits
- 表单控件列表，详情请参考FormComponentValues 参数说明说明，最多元素个数：100。 该接口不支持**地点控件**、**电话控件**。
- 表单名称。表单每一栏的名称，对应表单组件的label字段，最大长度64字符。
- 表单值，最大长度65535字符。
- 表单扩展值，最大长度8192字符。 目前联系人控件、关联审批单控件需要指定该值才能生成实例成功，具体请参照请求示例规范填写。
- 控件id，最大长度64字符，可调用创建或更新审批模板接口，获取FormComponent参数说明内的componentId参数值。
- 控件别名，最大长度64字符。
- 控件类型，最大长度64字符，详情请参考FormComponent参数说明。 - **TextField**：单行输入框 - **TextareaField**：多行输入框 - **NumberField**：数字输入框 - **DDSelectField**：单选框 选项值应当被配置在选项列表中 - **DDMultiSelectField**：多选框 选项值均应当被配置在选项列表中 - **DDDateField**：日期控件 - **DDDateRangeField**：
- 实例标题，最大长度64字符。

source_url: https://open.dingtalk.com/document/development/create-a-ticket-approval-instance
updated_at: 2026-06-03 10:12:38
