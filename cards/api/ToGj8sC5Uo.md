# 批量更新个人或企业客户数据

doc_id: ToGj8sC5Uo
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/crm/relationDatas/batch
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
- relationType (String, required): 客户类型。 - **crm_customer**：企业客户 - **crm_customer_personal**：个人客户
- operatorUserId (String, required): 操作人userId。
- relationList (Array, required): 更新的客户数据列表，最大值10。
- key (String, required): 模型字段key，该参数传客户对象元数据信息中获取字段的name值，调用获取个人或企业客户的元数据接口获取name参数值。 该参数是否必填，取决于调用获取客户对象的元数据信息接口，返回的nillable字段值： - nillable是**true**：本接口参数key和value为非必填。 - nillable是**false**：本接口参数key和value为必填。
- value (String, required): 模型字段value，不同类型的组件value值格式不同，请参考新增和更新客户字段格式说明V2。 该参数是否必填，取决于调用获取客户对象的元数据信息接口，返回的nillable字段值： - nillable是**true**：本接口参数key和value为非必填。 - nillable是**false**：本接口参数key和value为必填。
- relationId (String, required): 客户数据ID，调用根据指定条件查询个人或企业客户数据接口获取instanceId参数值。
- optional: skipDuplicateCheck(Boolean), bizDataList(Array), extendValue(String), bizExtMap(Map<String, String>)

## Returns
- optional: results(Array), success(Boolean), errorCode(String), errorMsg(String), relationId(String), duplicatedRelationIds(Array of String)

## Limits
- 更新的客户数据列表，最大值10。
- 更新的客户模型数据列表，最大值256。

source_url: https://open.dingtalk.com/document/development/update-multiple-relational-data-tables-at-a-time
updated_at: 2026-07-21 09:26:18
