# 删除自定义屏幕模板

doc_id: NA871TjlC6
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/rooms/devices/screens/templates/remove
api_version: v2-new
app_types: 第三方企业应用
permissions: Rooms.DeviceTemplate.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 接口调用凭证，调用获取用户token接口获取。 **[!NOTE]** 获取用户token的请求中，使用的入参`code`参数，在通过构造链接获取的过程中，scope范围必须为用户id和组织id，即`scope=openid corpid`。

## Path params
- none

## Query params
- none

## Body
- templateId (Long, required): 模板id，可调用查询自定义屏幕模板列表接口获取。

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-deletedevicecustomtemplate
updated_at: 2026-06-02 13:18:21
