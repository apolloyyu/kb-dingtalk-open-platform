---
title: "更新群"
source_url: "https://open.dingtalk.com/document/development/scene-group-update"
namespace: "development"
slug: "scene-group-update"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 即时通信 > 会话管理 > 场景群 > 更新群"
doc_id: "D3lA7IlNoU"
updated_at: "2026-08-25 09:37:16"
---

> Source: https://open.dingtalk.com/document/development/scene-group-update
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 即时通信 > 会话管理 > 场景群 > 更新群
> Updated: 2026-08-25 09:37:16

# 更新群

调用本接口根据群ID更新群信息，适用于企业需要对已创建的群聊信息进行修改的场景，如调整群名称、群主、群权限等。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[更新场景群](0747-api-updatescenegroup.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 否 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/im/chat/scenegroup/update`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1b\*\*\*\*\* | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| open\_conversation\_id | String | 是 | cidt\*\*\*\*\*Xa4K10w== | 群ID，调用[创建群](1484-create-a-scene-group-v2.md)接口获取`open_conversation_id`参数值。 |
| title | String | 否 | 测试群 | 群名称。  **[!NOTE]**  最长不超过30字符，建议长度在10字符以内。 |
| owner\_user\_id | String | 否 | 072\*\*\*\*\* | 群主的userId。 |
| icon | String | 否 | @lADOADma\*\*\*\*\*QKA | 群头像，格式为`mediaId`，调用[上传媒体文件](0646-upload-media-files.md)接口获取mediaId参数值。 |
| mention\_all\_authority | Number | 否 | 0 | @all 权限（此参数非必填）：   - **0 (默认)**：所有人可@all - **1**：仅群主可@all |
| show\_history\_type | Number | 否 | 0 | 新成员是否可查看聊天历史消息（此参数非必填）：   - **0 (默认)**：不可以 - **1**：可以 |
| validation\_type | Number | 否 | 0 | 入群验证（此参数非必填）：   - **0 (默认)**：不需要验证 - **1**：入群验证 |
| searchable | Number | 否 | 0 | 群是否可搜索（此参数非必填）：   - **0 (默认)：**不可搜索 - 1：可搜索 |
| chat\_banned\_type | Number | 否 | 0 | 群是否开启禁言（此参数非必填）：   - **0 (默认)**：不禁言 - 1：全员禁言 |
| management\_type | Number | 否 | 0 | 管理类型（此参数非必填）：   - **0 (默认)：**所有人可管理 - **1**：仅群主可管理 |
| only\_admin\_can\_ding | Number | 否 | 0 | 群内发DING权限：   - **0**（默认）：所有人可发DING - **1**：仅群主和管理员可发DING |
| all\_members\_can\_create\_mcs\_conf | Number | 否 | 1 | 群会议权限：   - **0**：仅群主和管理员可发起视频和语音会议 - **1**（默认）：所有人可发起视频和语音会议 |
| all\_members\_can\_create\_calendar | Number | 否 | 0 | 群日历设置项，群内非好友/同事的成员是否可相互发起钉钉日程：   - **0**（默认）：非好友/同事的成员不可发起钉钉日程 - **1**：非好友/同事的成员可以发起钉钉日程 |
| group\_email\_disabled | Number | 否 | 0 | 是否禁止发送群邮件：   - **0**（默认）：群内成员可以对本群发送群邮件 - **1**：群内成员不可对本群发送群邮件 |
| only\_admin\_can\_set\_msg\_top | Number | 否 | 0 | 置顶群消息权限：   - **0**（默认）：所有人可置顶群消息 - **1**：仅群主和管理员可置顶群消息 |
| add\_friend\_forbidden | Number | 否 | 0 | 群成员私聊权限：   - **0**（默认）：所有人可私聊 - **1**：普通群成员之间不能够加好友、单聊，且部分功能使用受限（管理员与非管理员之间不受影响） |
| group\_live\_switch | Number | 否 | 1 | 群直播权限：   - **0**：仅群主与管理员可发起直播 - **1**（默认）：群内任意成员可发起群直播 |
| members\_to\_admin\_chat | Number | 否 | 0 | 是否禁止非管理员向管理员发起单聊：   - **0**（默认）：非管理员可以向管理员发起单聊 - **1**：禁止非管理员向管理员发起单聊 |
| plugin\_customize\_verify | Number | 否 | 0 | 自定义群插件是否需要群主和管理员审批：   - **0**（默认）：不需要审批 - **1**：需要审批 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 返回结果，true表示执行成功，否则表示失败。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回信息。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/im/chat/scenegroup/update?access_token=ACCESS_TOKEN
```

请求正文

```
{
  			"open_conversation_id":"cidt*****Xa4K10w==",
        "title":"测试群",
        "owner_user_id":"072*****",
        "icon":"@lADOADma*****QKA",
        "mention_all_authority":0,
        "show_history_type":0,
        "validation_type":0,
        "searchable":0,
        "chat_banned_type":0,
        "management_type":0,
        "only_admin_can_ding":0,
        "all_members_can_create_mcs_conf":1,
        "all_members_can_create_calendar":0,
        "group_email_disabled":0,
        "only_admin_can_set_msg_top":0, 
        "add_friend_forbidden":0,
        "group_live_switch":1,
        "members_to_admin_chat":0,
        "plugin_customize_verify":0
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/im/chat/scenegroup/update");
OapiImChatScenegroupUpdateRequest req = new OapiImChatScenegroupUpdateRequest();
req.setOpenConversationId("cidt*****a4K10w==");
req.setTitle("测试群");
req.setOwnerUserId("072*****");
req.setIcon("@lADOADma*****QKA");
req.setMentionAllAuthority(0L);
req.setShowHistoryType(0L);
req.setValidationType(0L);
req.setSearchable(0L);
req.setChatBannedType(0L);
req.setManagementType(0L);
req.setOnlyAdminCanDing(0L);
req.setAllMembersCanCreateMcsConf(1L);
req.setAllMembersCanCreateCalendar(0L);
req.setGroupEmailDisabled(0L);
req.setOnlyAdminCanSetMsgTop(0L);
req.setAddFriendForbidden(0L);
req.setGroupLiveSwitch(1L);
req.setMembersToAdminChat(0L);
req.setPluginCustomizeVerify(0L);
OapiImChatScenegroupUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "errcode":0,
        "success":"true",
        "errmsg":"ok"
}
```

## 错误码

| 错误码（errorcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 40035 | 不合法的参数 | 请确认群管理项是否按要求填写参数 |
| 400020 | 没有访问权限 | 请确认此access\_token是否有操作这个群的权限 |
| 660041 | 员工不存在 | 请确认群主的userId是否正确 |
| 400001 | 系统错误 | 优先确认群ID是否正确，请稍后重试 |
