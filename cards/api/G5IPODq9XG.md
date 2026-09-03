# 获取员工花名册字段信息

doc_id: G5IPODq9XG
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrm/rosters/lists/query
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_hrm_read_user

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userIdList (Array of String, required): 员工的 userId 列表，多个 userId 之间使用英文逗号分隔，一次最多支持传100个值。
- appAgentId (Long, required): 应用的AgentId，详情参考AgentId。
- optional: fieldFilterList(Array of String), text2SelectConvert(Boolean)

## Returns
- optional: result(Array), corpId(String), userId(String), unionId(String), fieldDataList(Array), fieldCode(String), fieldName(String), groupId(String), fieldValueList(Array), value(String), label(String), itemIndex(Integer)

## Limits
- 员工的 userId 列表，多个 userId 之间使用英文逗号分隔，一次最多支持传100个值。
- 需要获取的花名册字段field_code值列表，多个字段之间使用逗号分隔，一次最多支持传100个值。 - 该参数不传时，获取全部字段信息。 - 查询字段越少，RT越低，建议按需查询。 - 企业内部应用： - 查看花名册自定义字段业务code中field_code字段。 - 调用获取获取花名册元数据接口获取field_code参数值。 - 第三方企业应用，调用查询花名册中有权限的字段列表接口获取field_code参数值。

source_url: https://open.dingtalk.com/document/development/api-getemployeerosterbyfield
updated_at: 2026-06-04 19:10:24
