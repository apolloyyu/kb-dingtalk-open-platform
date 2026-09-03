# 智能人事员工调岗

doc_id: EOtxyB2KRO
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/hrm/processes/transfer
api_version: v2-new
app_types: 企业内部应用
permissions: Hrm.Process.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- userId (String, required): 被调岗员工userId。
- optional: deptIdsAfterTransfer(Array of Long), mainDeptIdAfterTransfer(Long), positionIdAfterTransfer(String), positionNameAfterTransfer(String), rankIdAfterTransfer(String), positionLevelAfterTransfer(String), jobIdAfterTransfer(String), operateUserId(String)

## Returns
- optional: result(Boolean)

## Limits
- 员工调岗后的职位名称，长度最大124字符。是否升级职位，该参数填写方式不同，可参考下方升级说明-职位。 **[!NOTE]** 该参数的填写方式与是否升级职位有关，可参考下方升级说明-职位说明。 - 如果是未升级，该参数必填，请填写职位名称。 - 如果是已升级，该参数不传，会自动更新参数职位ID参数`positionIdAfterTransfer`对应的职位名称。
- 员工调岗后的职级名称，长度不超过64字符。 **[!NOTE]** 该参数的填写方式与是否升级岗位职级有关，可参考下方升级说明-岗位职级说明。 - 如果是未升级，该参数必填，请填写岗位职级名称。 - 如果是已升级，该参数不传，会自动更新参数职级ID参数`rankIdAfterTransfer`对应的职级名称。

source_url: https://open.dingtalk.com/document/development/intelligent-personnel-staff-transfer
updated_at: 2026-07-14 09:22:32
