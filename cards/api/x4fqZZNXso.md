# 批量新增跟进记录数据

doc_id: x4fqZZNXso
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/crm/followRecords/batch
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_crm_maindata_write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- operatorUserId (String, required): 操作人userId，可调用通过免登码获取用户信息接口获取userId。
- instanceList (Array, required): 跟进记录数据字段列表，最大值40。
- dataArray (Array, required): 新增跟进记录的模型数据列表，最大值256。
- key (String, required): 模型字段key，该参数传跟进记录对象元数据信息中获取字段的name值，调用获取跟进记录对象的元数据接口获取name参数值。 该参数是否必填，取决于调用获取跟进记录对象的元数据信息接口，返回的nillable字段值： - 若nillable是**true**：本接口参数key和value为非必填。 - 若nillable是**false**：本接口参数key和value为必填。
- value (String, required): 模型字段value，不同类型的组件value值格式不同，请参考自定义控件字段格式说明V2。
- optional: extendValue(String)

## Returns
- optional: results(Array), success(Boolean), errorCode(String), errorMsg(String), instanceId(String)

## Limits
- 跟进记录数据字段列表，最大值40。
- 新增跟进记录的模型数据列表，最大值256。

source_url: https://open.dingtalk.com/document/development/batch-add-follow-up-record-data
updated_at: 2026-06-04 19:12:13
