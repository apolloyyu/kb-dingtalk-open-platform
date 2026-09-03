# 通知换班通过

doc_id: 95Fb8pWqlm
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/approve/schedule/switch
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_attendance_group_manage

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- userid (String, required): 发起人的userId。
- switch_date (String, required): 申请换班日期，当天必须有排班或排休。
- reback_date (String, required): 还班日期，当天必须有排班或排休。 **[!NOTE]** 如果申请换班人和被换班人是同一个人，那么必须要有还班日期。
- apply_userid (String, required): 申请换班人的userId，仅支持排班制考勤组用户。
- target_userid (String, required): 被换班人的userId，仅支持排班制考勤组用户。
- approve_id (String, required): 审批单ID，自定义参数值。
- apply_shift_id (Number, required): 申请人换班日期当天的班次ID，可通过批量查询人员排班信息接口获取shift_id参数值。
- target_shift_id (Number, required): 被换班人换班日期当天的班次ID，可通过批量查询人员排班信息接口获取shift_id参数值。
- reback_apply_shift_id (Number, required): 申请人还班日期当天的班次ID，可通过批量查询人员排班信息接口获取shift_id参数值。
- reback_target_shift_id (Number, required): 被换班人还班日期当天的班次ID，可通过批量查询人员排班信息接口获取shift_id参数值。

## Returns
- optional: errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/shift-change-operation-after-approval
updated_at: 2026-05-27 17:06:23
