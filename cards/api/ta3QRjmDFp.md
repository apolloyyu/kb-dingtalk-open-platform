# 创建待办卡片类型配置

doc_id: ta3QRjmDFp
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/todo/users/{unionId}/configs/types
api_version: v2-new
app_types: 企业内部应用
permissions: Todo.Todo.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过 获取用户token接口获取。

## Path params
- unionId (String, required): 用户的unionId，可通过查询用户详情接口获取。

## Query params
- optional: operatorId(String)

## Body
- cardType (Integer, required): 卡片类型，取值。 - **1**：标准卡片 - **2**：自定义卡片
- icon (String, required): 卡片类型图标，用于在待办列表展示。 图片资源的mediaId可通过上传媒体文件接口获取。 **[!NOTE]** 图标要求如下： - 尺寸：24px \* 24px - 圆角：6px - 大小：小于500k
- pcDetailUrlOpenMode (String, required): 详情页链接在PC端的打开方式，取值。 - **PC_SLIDE**：PC端侧边栏打开 - **PC_BROWSER**：浏览器打开
- optional: description(String), contentFieldList(Array), fieldKey(String), fieldType(String), nameI18n(Map), actionList(Array), actionKey(String), buttonStyleType(Integer), actionType(Integer), url(String)

## Returns
- optional: id(String), createdTime(Long), modifiedTime(Long), creatorId(String), modifierId(String), bizTag(String), requestId(String), cardType(Integer), icon(String), description(String), pcDetailUrlOpenMode(String), contentFieldList(Array), fieldKey(String), fieldType(String), nameI18n(Map), actionList(Array), actionKey(String), buttonStyleType(Integer), actionType(Integer), url(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/add-todo-cardtype-configuration
updated_at: 2026-07-30 10:01:52
