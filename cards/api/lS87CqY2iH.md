# 更新申请单状态

doc_id: lS87CqY2iH
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/alitrip/btrip/approval/update
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_ali_business_trip_write

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- rq (OpenApiUpdateApplyRq, required): 请求对象，封装所有更新参数。
- thirdpart_apply_id (String, required): 外部申请单ID，调用获取申请单列表接口获取。
- operate_time (Date, required): 操作时间。
- status (Number, required): 申请单状态： - 1：已同意 - 2：已拒绝 - 3：已转交 - 4：已取消
- userid (String, required): 审批人的userid，需为钉钉系统内有效的用户标识。
- corpid (String, required): 企业的corpid，标识目标企业租户。
- optional: user_name(String), note(String)

## Returns
- optional: errmsg(String), errcode(Number), success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/update-approval-form
updated_at: 2026-06-03 09:58:25
