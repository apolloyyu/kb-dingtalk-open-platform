# 获取指定宜搭角色的角色详情

doc_id: WbP6bwhqLH
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/yida/forms/resources/roles
api_version: v2-new
app_types: 企业内部应用
permissions: Yida.PlatformResource.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- roleUuid (String, required): 角色唯一标识，获取方式：平台管理-角色管理-宜搭角色-角色ID。
- corpId (String, required): 组织的corpId。
- userId (String, required): 用户的userid。
- token (String, required): 验权token。 校验方式如下：`md5(corpId + userId + code)`。md5取32位大写值。 **[!NOTE]** 每个企业有自己的唯一code。
- optional: pageSize(Integer), pageNumber(Integer)

## Returns
- optional: result(Object), roleUuid(String), parentUuid(String), name(String), description(String), memberTotalCount(Integer), canModifyOwners(Any), members(Object), currentPage(Integer), totalCount(Integer), data(Any), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/get-roledetailbyid
updated_at: 2026-06-15 10:49:28
