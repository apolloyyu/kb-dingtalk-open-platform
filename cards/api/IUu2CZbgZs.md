# 更新卡片

doc_id: IUu2CZbgZs
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/card/instances
api_version: v2-new
app_types: 第三方企业应用
permissions: Card.Instance.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- outTrackId (String, required): 外部卡片实例Id。 **[!NOTE]** 由开发者自己生成并作为入参传递给钉钉的，钉钉只在对应使用到outTrackId的场景，帮助开发者对TrackId进行记录。
- optional: cardData(Object), cardParamMap(Map<String, String>), privateData(Map<String, Object>), cardUpdateOptions(Object), updateCardDataByKey(Boolean), updatePrivateDataByKey(Boolean), userIdType(Integer)

## Returns
- optional: success(Boolean), result(Boolean)

## Limits
- 卡片模板内容替换参数： - key：参数名（最长不超过100B） - value: 参数值（最长不超过1KB） **[!NOTE]** - 属性字段只支持 String 类型，非 String 类型的属性填写请参考文档：API 卡片数据的填写说明。 - 务必确保属性值的类型与卡片搭建器中所配置的变量类型相匹配，否则可能出现属性不生效，或者在移动端无法显示等问题。

source_url: https://open.dingtalk.com/document/development/interactive-card-update-interface
updated_at: 2026-06-04 10:49:19
