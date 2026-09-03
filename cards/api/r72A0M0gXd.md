# 获取权限列表

doc_id: r72A0M0gXd
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/storage/spaces/dentries/{dentryUuid}/permissions/query
api_version: v2-new
app_types: 企业内部应用
permissions: Storage.Permission.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- dentryUuid (String, required): 文件uuid，可调用搜索文件接口或获取dentryUuid信息接口，获取返回参数dentryUuid字段。

## Query params
- unionId (String, required): 用户unionId，调用查询用户详情接口获取。

## Body
- optional: option(Object), nextToken(String), maxResults(Integer), filterRoleIds(Array of String)

## Returns
- optional: permissions(Array), dentryUuid(String), member(Object), type(String), id(String), corpId(String), name(String), role(Object), duration(Long), nextToken(String)

## Limits
- 权限列表分页数据，最多显示30个。

source_url: https://open.dingtalk.com/document/development/get-permission-list
updated_at: 2026-07-08 14:38:37
