# 批量更新跟进记录数据

doc_id: DfXBnZOvf0
completeness: full
archived: false
method: PUT
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
- instanceList (Array, required): 更新的跟进记录数据列表，最大值40。
- dataArray (Array, required): 更新的跟进记录模型数据列表，最大值256。
- key (String, required): 模型字段key，填写获取跟进记录对象的元数据接口返回的name值。该参数是否必填，取决于获取跟进记录对象的元数据接口中返回的nillable值： - 若nillable是true：则key和value非必填。 - 若nillable是false：则key和value必填。
- value (String, required): 模型字段value，不同类型的组件value值格式不同，请参考自定义控件字段格式说明V2。
- instanceId (String, required): 跟进记录ID，调用根据指定条件查询跟进记录数据接口获取。
- optional: extendValue(String)

## Returns
- optional: results(Array), success(Boolean), errorCode(String), errorMsg(String), instanceId(String)

## Limits
- 更新的跟进记录数据列表，最大值40。
- 更新的跟进记录模型数据列表，最大值256。

source_url: https://open.dingtalk.com/document/development/batch-update-follow-up-record-data
updated_at: 2026-06-04 19:12:14
