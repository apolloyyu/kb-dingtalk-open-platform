# 获取应用信息

doc_id: i3ZTw2pyx7
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/storage/currentApps/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Storage.App.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- unionId (String, required): 操作者unionId，可调用查询用户详情接口获取。

## Body
- none

## Returns
- optional: app(Object), corpId(String), appId(String), name(String), createTime(String), modifiedTime(String), partitions(Array), partitionType(String), quota(Object), used(Long), max(Long), reserved(Long), type(String)

## Limits
- 最大容量，单位Byte。 如果当前应用容量没有设置quota容量，不返回该字段。

source_url: https://open.dingtalk.com/document/development/obtains-the-information-about-the-current-application
updated_at: 2026-06-04 19:09:30
