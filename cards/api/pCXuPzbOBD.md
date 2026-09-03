# 获取指定权限矩阵的明细数据

doc_id: pCXuPzbOBD
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v2.0/yida/forms/resources/matrices
api_version: v2-new
app_types: 企业内部应用
permissions: Yida.PlatformResource.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- matrixId (String, required): 矩阵唯一标识，获取方式：平台管理-权限矩阵管理-权限矩阵ID。
- corpId (String, required): 组织的corpId。
- userId (String, required): 用户的userid。
- token (String, required): 验权token。 校验方式如下：`md5(corpId + userId + code)`。md5取32位大写值。 **[!NOTE]** 每个企业有自己的唯一code。
- optional: pageSize(Integer), pageNumber(Integer)

## Body
- none

## Returns
- optional: result(Object), matrixId(String), name(Object), en_US(String), zh_CN(String), type(String), description(Object), matrixTable(Object), conditionColumn(Array), columnId(String), componentType(String), resultColumn(Array), matrixData(Object), currentPage(Integer), totalCount(Integer), data(Any), rowTotalCount(Integer), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-getmatrixdetailbyid
updated_at: 2026-06-15 10:49:30
