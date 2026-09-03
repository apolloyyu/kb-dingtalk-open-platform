# 查询考勤机信息

doc_id: 5NXcD5WqDT
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/attendance/machines/{devId}
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_attendance_group_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- devId (Long, required): 考勤机设备ID，可调用查询设备列表接口获取device_id参数值。

## Query params
- none

## Body
- none

## Returns
- optional: result(Object), deviceId(String), devId(Long), deviceName(String), productName(String), netStatus(String), productVersion(String), deviceSn(String), maxFace(Integer), voiceMode(Integer), atmManagerList(Array of String), machineBluetoothVO(Object), bluetoothValue(Boolean), bluetoothCheckWithFace(Boolean), bluetoothDistanceMode(String), bluetoothDistanceModeDesc(String), monitorLocationAbnormal(Boolean), address(String), longitude(double), latitude(double), limitUserDeviceCount(Boolean), userDeviceCount(Integer)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-attendance-machine-information
updated_at: 2026-06-02 09:24:51
