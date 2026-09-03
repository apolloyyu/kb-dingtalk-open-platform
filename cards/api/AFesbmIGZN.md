# 同步市内用车申请单

doc_id: AFesbmIGZN
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/alitrip/cityCarApprovals
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_ali_business_trip_write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- cause (String, required): 出差事由，用于说明本次市内用车的具体原因。
- city (String, required): 用车城市，填写城市名称，如“杭州”。
- corpId (String, required): 第三方企业的corpid，用于标识企业身份。
- date (String, required): 用车时间，按天管控，比如传值2021-03-18 20:26:56表示2021-03-18当天可用车，跨天情况配合finishedDate参数使用
- status (Long, required): 审批单状态： - **0**：申请 - **1**：同意 - **2**：拒绝
- thirdPartApplyId (String, required): 三方审批单ID。
- thirdPartCostCenterId (String, required): 审批单关联的三方成本中心ID。
- thirdPartInvoiceId (String, required): 审批单关联的三方发票抬头ID。
- timesTotal (Long, required): 审批单可用总次数。
- timesType (Long, required): 审批单可用次数类型： - **1**：次数不限制 - **2**：用户可指定次数 - **3**：管理员限制次数 如果企业没有限制审批单使用次数的需求，这个参数传1(次数不限制)，同时timesTotal和timesUsed都传0即可
- timesUsed (Long, required): 审批单已用次数。
- title (String, required): 审批单标题。
- userId (String, required): 发起审批的第三方员工ID。
- optional: projectCode(String), projectName(String), finishedDate(String)

## Returns
- optional: applyId(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/synchronize-third-party-city-vehicle-approval-form
updated_at: 2026-06-04 19:10:47
