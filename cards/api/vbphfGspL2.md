# 获取资源上传信息

doc_id: vbphfGspL2
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/doc/docs/resources/{docId}/uploadInfos/query
api_version: v2-new
app_types: 企业内部应用
permissions: Storage.File.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- docId (String, required): 文档ID (dentryUuid/documentId/workbookId/baseId)，可通过以下两种方式获取： - 调用创建知识库文档接口获取。 - 调用获取节点列表接口获取。

## Query params
- operatorId (String, required): 操作人的unionId，可通过调用查询用户详情接口或通过免登码获取用户信息接口获取。

## Body
- size (Long, required): 资源大小，单位：字节。
- mediaType (String, required): 资源类型，具体值请参考 MIME Types。
- resourceName (String, required): 资源名称。

## Returns
- optional: success(Boolean), result(Object), uploadUrl(String), resourceId(String), resourceUrl(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getresourceuploadinfo
updated_at: 2026-06-02 18:38:02
