# 批量删除指定矩阵的明细数据

doc_id: JUdhBuleo2
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/yida/forms/resources/matrices/remove
api_version: v2-new
app_types: 企业内部应用
permissions: Yida.PlatformResource.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- matrixId (String, required): 矩阵唯一标识，获取方式：平台管理-权限矩阵管理-权限矩阵ID。
- corpId (String, required): 组织的corpId。
- userId (String, required): 用户的userid。
- token (String, required): 验权token，校验方式如下：`md5(corpId + userId + code)`。md5取32位大写值。 **[!NOTE]** 每个企业有自己的唯一code。
- rowIds (String, required): 矩阵行数据rowId列表，多个以英文逗号分隔。

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-deletematrixdatabyrowids
updated_at: 2026-06-15 10:49:33
