# 查询自定义屏幕信息

doc_id: HYEMa3tJUx
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/rooms/devices/screens/templates/{templateId}
api_version: v2-new
app_types: 第三方企业应用
permissions: Rooms.DeviceTemplate.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 接口调用凭证，调用获取用户token接口获取。 **[!NOTE]** 获取用户token的请求中，使用的入参`code`参数，在通过构造链接获取的过程中，scope范围必须为用户id和组织id，即`scope=openid corpid`。

## Path params
- templateId (Long, required): 模板id，可调用查询自定义屏幕模板列表接口获取。

## Query params
- none

## Body
- none

## Returns
- optional: result(Object), deviceCustomTemplate(Object), templateId(Long), corpId(String), logo(String), orgName(String), customDoc(String), bgUrl(String), bgImageList(Array of String), instruction(Boolean), bgType(Integer), isPicTop(Integer), templateName(String), confType(Integer), showCalendarTitle(Boolean), hideServerCodeWhenProjecting(Boolean), confSubType(Integer), desensitizeUserName(Boolean), picturePlayInterval(Integer), showCalendarCard(Boolean), showFunctionCard(Boolean), deviceUnionIds(Array of String), groupIds(Array of Long), roomIds(Array of String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-querydevicecustomtemplate
updated_at: 2026-06-02 13:18:23
