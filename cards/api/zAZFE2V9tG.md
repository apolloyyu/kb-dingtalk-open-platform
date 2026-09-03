# 查询视频会议设备信息

doc_id: zAZFE2V9tG
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/rooms/devices
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
- none

## Returns
- optional: result(Object), deviceId(String), deviceUnionId(String), openRoomId(String), corpId(String), deviceName(String), shareCode(String), deviceSn(String), deviceMac(String), deviceType(String), deviceServiceId(Integer), deviceModel(String), deviceStatus(String), controllers(Array), creatorUnionId(String), roomName(String), firmwareVersion(String), softwareVersion(String), activeTime(Long), devNetType(String), devNetIp(String), devWifiMac(String), devWireMac(String), devCamera(String), devMic(String), devVoice(String), devMirror(String), devHdmi(String), sipAccountName(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/querying-video-conference-device-information
updated_at: 2026-06-02 13:04:58
