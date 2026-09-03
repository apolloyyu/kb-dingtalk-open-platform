# 获取巡检或保养记录

doc_id: hLsN31FzGu
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/devicemng/customers/devices/inspectInfos/query
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
- optional: pageNumber(Integer), pageSize(Integer), deviceUuid(Array of String), type(String)

## Returns
- optional: totalCount(Long), success(Boolean), result(Array), deviceName(String), deviceCode(String), type(String), status(Integer), repairStatus(Integer), maintenanceStaff(Array of String), handleTime(String), remark(String), name(String), gmtCreate(String)

## Limits
- 当页大小，最大值20。
- 设备uuIi列表，调用查询已经注册的设备信息接口获取的uuid，最大值10。

source_url: https://open.dingtalk.com/document/development/obtain-inspection-and-maintenance-records
updated_at: 2026-06-04 19:11:20
