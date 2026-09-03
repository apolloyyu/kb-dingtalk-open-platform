# 写入每日组织碳数据明细信息

doc_id: 3rrWiWMZ5X
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/carbon/orgDetails/write
api_version: v2-new
app_types: 第三方企业应用
permissions: Carbon.Common.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- orgDetailsList (Array, required): 请求参数。
- actionId (String, required): 全局唯一ID，用于数据订正。
- corpId (String, required): 钉钉组织的corpId。
- deptId (Long, required): 钉钉部门ID。
- actionType (String, required): 碳能量减排来源。
- carbonAmount (String, required): 碳能量克数。
- actionTime (String, required): 减排行为发生时间。
- version (Integer, required): 版本号，默认为1。

## Returns
- optional: success(Boolean), result(Integer)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/third-party-applications-write-daily-organizational-carbon-data-details-1
updated_at: 2026-06-05 15:15:10
