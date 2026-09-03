# 获取填表实例列表

doc_id: fhOx86py27
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/swform/forms/{formCode}/instances
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_swapp_collection_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- formCode (String, required): 填表code，可调用获取用户创建的填表模板列表接口获取formCode参数值。

## Query params
- nextToken (Integer, required): 分页游标。 - 如果是首次查询，该参数值传0。 - 如果是非首次查询，该参数传上次调用时返回的nextToken。
- maxResults (Integer, required): 每页最大条目数，最大值100。
- optional: bizType(Integer), actionDate(String)

## Body
- none

## Returns
- optional: success(Boolean), result(Object), hasMore(Boolean), nextToken(Long), list(Array), createTime(String), modifyTime(String), formCode(String), title(String), submitterUserId(String), submitterUserName(String), forms(Array), label(String), key(String), value(String), formInstanceId(String), studentClassName(String), studentClassId(String), studentUserId(String), studentName(String)

## Limits
- 每页最大条目数，最大值100。

source_url: https://open.dingtalk.com/document/development/obtain-the-table-filling-instance-list-data
updated_at: 2026-06-04 19:10:38
