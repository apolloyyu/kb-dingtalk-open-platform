# 获取企业信息

doc_id: 0cJeXcVvvc
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/storage/orgs/{corpId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.Org.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- corpId (String, required): 企业corpId。

## Query params
- unionId (String, required): 用户unionId，可调用查询用户详情接口获取。

## Body
- none

## Returns
- optional: org(Object), corpId(String), partitions(Array), partitionType(String), quota(Object), used(Long), max(Long), reserved(Long), type(String)

## Limits
- 最大容量，单位: Byte。
- 调用本接口，获取该企业的企业存储信息，例如存储空间为100GB，已使用953.5MB。

source_url: https://open.dingtalk.com/document/development/obtain-enterprise-storage-related-information
updated_at: 2026-06-04 19:09:29
