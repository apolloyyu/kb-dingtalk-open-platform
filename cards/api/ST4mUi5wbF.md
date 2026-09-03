# 批量删除宜搭角色成员

doc_id: ST4mUi5wbF
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/yida/forms/resources/roles/remove
api_version: v2-new
app_types: 企业内部应用
permissions: Yida.PlatformResource.Write

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
- memberIds (String, required): 角色里要删除的成员userId，多个成员用英文逗号分隔。
- optional: pageSize(Integer), pageNumber(Integer)

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/batch-deleterolemembers
updated_at: 2026-06-15 10:49:26
