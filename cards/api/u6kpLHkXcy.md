# 更新自定义屏幕模板

doc_id: u6kpLHkXcy
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/rooms/devices/screens/templates
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
- templateName (String, required): 模板名称。
- templateId (Long, required): 模板id，可调用查询自定义屏幕模板列表接口获取。
- optional: logo(String), orgName(String), customDoc(String), bgUrl(String), bgImgList(Array of String), instruction(Boolean), bgType(Integer), isPicTop(Integer), hideServerCodeWhenProjecting(Boolean), showCalendarTitle(Boolean), desensitizeUserName(Boolean), picturePlayInterval(Integer), showCalendarCard(Boolean), showFunctionCard(Boolean), deviceUnionIds(Array of String), groupIds(Array of Long), roomIds(Array of String)

## Returns
- optional: result(Boolean)

## Limits
- 模板logo，可调用上传媒体文件接口获取meidaId，图片尺寸：240\*240，单个图片大小不超过1M。
- 图片mediaId，可调用上传媒体文件接口获取出参`media_id`参数，最多可上传9张图片，单个图片大小不超过5M。

source_url: https://open.dingtalk.com/document/development/api-updatedevicecustomtemplate
updated_at: 2026-06-02 13:18:22
