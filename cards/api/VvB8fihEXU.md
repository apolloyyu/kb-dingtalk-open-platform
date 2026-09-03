# 查询视频会议设备属性信息

doc_id: VvB8fihEXU
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/rooms/devices/properties/query
api_version: v2-new
app_types: 企业内部应用
permissions: VideoConference.Conference.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- operatorUnionId (String, required): 操作查询的人员unionId，可调用查询用户详情接口获取获取。
- optional: deviceId(String), deviceUnionId(String)

## Body
- optional: propertyNames(Array of String)

## Returns
- optional: result(Array), propertyName(String), propertyValue(String)

## Limits
- 设备属性名称列表，最大值10。 - dev_code：投屏码 - dev_model：设备型号 - dev_app_status：设备状态 - dev_net_ip：设备ip - dev_net_type：设备网络类型 - dev_wifi_mac：设备无线mac地址 - dev_wire_mac：设备有线mac地址 - dev_firmware_v：设备固件版本 - dev_software_v：设备软件版本 - dev_hdmi：设备外接显示器

source_url: https://open.dingtalk.com/document/development/querying-video-conference-device-attribute-information
updated_at: 2026-06-02 13:04:58
