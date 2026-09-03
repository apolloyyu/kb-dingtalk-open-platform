# 新增或删除花名册选项类型字段的选项

doc_id: EVHoKB1Chw
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/hrm/rosters/meta/fields/options
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_hrm_manager

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: appAgentId(Long)

## Body
- groupId (String, required): 花名册分组ID，可调用获取花名册元数据接口获取group_id参数值。
- fieldCode (String, required): 花名册字段标识。 - 企业内部应用，可调用获取花名册元数据接口获取。 - 第三方企业应用，可调用查询花名册中有权限的字段列表接口获取。
- labels (Array of String, required): 需要修改的选项值列表，最大值20。 - 如果modifyType值为**OPTIONS_ADD**，该参数值为自定义值。 - 如果modifyType值为**OPTIONS_DELETE**，该参数值可调用获取员工花名册字段信息接口获取label参数值。
- modifyType (String, required): 修改类型。 - **OPTIONS_ADD**：添加选项 - **OPTIONS_DELETE**：删除选项

## Returns
- optional: result(Boolean)

## Limits
- 需要修改的选项值列表，最大值20。 - 如果modifyType值为**OPTIONS_ADD**，该参数值为自定义值。 - 如果modifyType值为**OPTIONS_DELETE**，该参数值可调用获取员工花名册字段信息接口获取label参数值。

source_url: https://open.dingtalk.com/document/development/intelligent-personnel-roster-field-option-modification
updated_at: 2026-06-04 19:10:24
