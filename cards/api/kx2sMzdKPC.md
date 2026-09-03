# 添加服务群成员

doc_id: kx2sMzdKPC
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/serviceGroup/groups/members
api_version: v2-new
app_types: 企业内部应用
permissions: ServiceGroup.Group.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- openTeamId (String, required): 开放团队ID。如下图所示，查看**ID信息**内的**团队ID**值。
- openConversationId (String, required): 服务群openConversionId，可调用创建场景服务群接口获取openConversationId参数值。
- userIds (Array of String, required): 待添加员工在钉钉组织内的的userId列表，最大值100。 **[!NOTE]** 请确保userId值的正确性，如果userId值不正确，该接口不会报错，添加时会自动忽略该成员。

## Returns
- optional: success(Boolean)

## Limits
- 待添加员工在钉钉组织内的的userId列表，最大值100。 **[!NOTE]** 请确保userId值的正确性，如果userId值不正确，该接口不会报错，添加时会自动忽略该成员。

source_url: https://open.dingtalk.com/document/development/add-service-group-members
updated_at: 2026-06-03 09:11:04
