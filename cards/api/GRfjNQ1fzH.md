# 获取报修记录

doc_id: GRfjNQ1fzH
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/devicemng/customers/devices/maintainInfos/query
api_version: v2-new
app_types: 第三方企业应用
permissions: Manufacture.DeviceData.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: pageNumber(Integer), pageSize(Integer), deviceUuid(Array of String)

## Returns
- optional: totalCount(Long), success(Boolean), result(Array), gmtCreate(String), deviceCode(String), deviceName(String), remark(String), maintenanceStaff(Array of String), processState(Integer), handleTime(String)

## Limits
- 页面大小，最大值20。
- 设备uuIi列表，调用查询已经注册的设备信息接口获取的uuid，最大值10。

source_url: https://open.dingtalk.com/document/development/obtain-the-repair-report-record
updated_at: 2026-06-04 19:11:20
