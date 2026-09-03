# 批量新增Wi-Fi信息

doc_id: 7U7Hd1UIt9
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/group/wifis/add
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_attendance_group_manage

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- group_key (String, required): 考勤组ID。 **[!NOTE]** 如果你使用的考勤组标识是group_id，可以调用groupId转换为groupKey接口将group_id转换为group_key。
- wifi_list (Wifi[], required): Wi-Fi列表，每次调用最多新增100个Wi-Fi信息。
- foreign_id (String, required): 业务方wifiId。
- mac_addr (String, required): MAC地址。
- ssid (String, required): 名称。
- optional: op_userid(String)

## Returns
- optional: result(DingOpenResult), error_info_list(ErrorInfo[]), failure_list(Wifi[]), foreign_id(String), mac_addr(String), ssid(String), wifi_key(String), msg(String), code(String), success_list(Wifi[]), errcode(Number), errmsg(String), success(Boolean), request_id(String)

## Limits
- Wi-Fi列表，每次调用最多新增100个Wi-Fi信息。

source_url: https://open.dingtalk.com/document/development/batch-add-wifi-under-attendance-group
updated_at: 2026-05-27 13:10:03
