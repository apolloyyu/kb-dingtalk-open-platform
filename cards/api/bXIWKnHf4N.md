# 人才档案照片查询

doc_id: bXIWKnHf4N
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrbrain/profiles/attachmentPhotos/query
api_version: v2-new
app_types: 企业内部应用
permissions: Hrbrain.Data.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- optional: dingCorpId(String)

## Body
- none

## Returns
- optional: requestId(String), success(Boolean), result(Boolean), content(Object), staffAttachmentInfoList(Array), workNo(String), attachmentInfoList(Array), url(String), name(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-hrbraintalentprofileattachmentquery
updated_at: 2026-06-02 19:34:55
