# 批量修改联系人数据

doc_id: kaWxsT38ZW
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/crm/contacts/batch
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
- operatorUserId (String, required): 操作人userId。
- relationList (Array, required): 联系人数据列表，最大值10。
- key (String, required): 模型字段key，该参数传获取联系人的元数据接口中获取的name字段值。 该参数是否必填，取决于**获取联系人的元数据**接口，返回的nillable字段值。 - nillable是**true**：本接口参数key和value为非必填。 - nillable是**false**：本接口参数key和value为必填。
- value (String, required): 模型字段value，不同类型的组件value值格式不同，请参考新增和更新联系人字段格式说明V2。
- relationId (String, required): 要修改的联系人ID，调用根据指定条件查询联系人数据接口获取instance_id参数值。
- optional: bizDataList(Array), extendValue(String), bizExtMap(Map<String, String>)

## Returns
- optional: results(Array), success(Boolean), errorCode(String), errorMsg(String), relationId(String)

## Limits
- 联系人数据列表，最大值10。
- 新增联系人的模型数据列表，最大值256。

source_url: https://open.dingtalk.com/document/development/modify-contact-data-in-batches
updated_at: 2026-06-04 19:12:12
