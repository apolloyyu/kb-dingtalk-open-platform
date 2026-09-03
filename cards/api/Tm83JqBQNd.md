# 写入每日用户碳数据明细信息

doc_id: Tm83JqBQNd
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/carbon/userDetails/write
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
- userDetailsList (Array, required): 请求参数。
- actionId (String, required): 全局唯一ID，用于数据订正。
- userId (String, required): 钉钉用户id
- corpId (String, required): 钉钉组织corpId。
- deptId (Long, required): 钉钉部门ID。
- actionType (String, required): 碳能量减排来源。
- carbonAmount (String, required): 碳能量克数。
- actionStartTime (String, required): 减排行为开始时间。
- actionEndTime (String, required): 减排行为结束时间。
- version (Integer, required): 版本号，默认为1。

## Returns
- optional: success(Boolean), result(Integer)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/write-in-the-detailed-information-of-daily-user-carbon-data
updated_at: 2026-06-03 09:34:07
