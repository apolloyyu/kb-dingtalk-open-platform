# 获取回收站信息

doc_id: bf5fLWtE94
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/storage/recycleBins
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.RecycleBin.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- recycleBinScope (String, required): 回收站范围类型。 - **ORG**：企业
- scopeId (String, required): 回收站范围Id。 如果recycleBinScope只为ORG，该参数值传corpId。
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取。

## Body
- none

## Returns
- optional: recycleBin(Object), id(String), scope(String), scopeId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-information-about-the-recycle-bin
updated_at: 2026-06-04 19:09:42
