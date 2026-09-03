# 获取企业内部小程序历史版本列表

doc_id: isiqxQgE8g
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/microApp/innerMiniApps/{agentId}/historyVersions
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_get_microapp_list

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- agentId (Long, required): 应用AgentId。 image

## Query params
- pageNumber (Integer, required): 当前页。
- pageSize (Integer, required): 本次读取的最大数据记录数量。

## Body
- none

## Returns
- optional: totalCount(Long), miniAppVersionList(Array), appVersionId(Long), miniAppId(String), appVersion(String), appVersionType(Integer), miniAppOnPc(Boolean), createTime(String), modifyTime(String)

## Limits
- 本次读取的最大数据记录数量。

source_url: https://open.dingtalk.com/document/development/obtain-the-list-of-historical-versions-of-enterprise-internal-applets
updated_at: 2026-07-14 09:22:22
