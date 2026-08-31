---
title: "创建群"
source_url: "https://open.dingtalk.com/document/development/create-a-scene-group-v2"
namespace: "development"
slug: "create-a-scene-group-v2"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 即时通信 > 会话管理 > 场景群 > 创建群"
doc_id: "Rd9vXSwYHS"
updated_at: "2026-08-25 09:37:16"
---

> Source: https://open.dingtalk.com/document/development/create-a-scene-group-v2
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 即时通信 > 会话管理 > 场景群 > 创建群
> Updated: 2026-08-25 09:37:16

# 创建群

调用本接口根据群模板ID创建群，适用于企业需要根据群模板快速创建群聊的场景，如项目协作、活动组织等。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[创建场景群](0746-create-a-scene-group.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 否 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/im/chat/scenegroup/create`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | beE4\*\*\*\*\*75d | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| title | String | 是 | 测试群 | 群名称。  **[!NOTE]**  最长不超过30字符，建议长度在10字符以内。 |
| template\_id | String | 是 | c354\*\*\*-\*\*\*-\*\*\*-b4ea-6f1ab\*\*\*65 | 群模板ID，登录[开发者后台 > 开放能力 > 场景群 > 群模板](https://open-dev.dingtalk.com/fe/im#/group/list)查看id。image |
| owner\_user\_id | String | 是 | 022\*\*\*\*\* | 群主的userid。 |
| user\_ids | String | 否 | 072\*\*\*\*\*,013\*\*\*\*\* | 群成员userid列表。  **[!NOTE]**  最多传999个。 |
| subadmin\_ids | String | 否 | 072\*\*\*\*\*,013\*\*\*\*\* | 群管理员userid列表。 |
| uuid | String | 否 | axcf\*-\*\*\*\*\*-\*\*\*\*\*-23da\* | 建群去重的业务ID，由接口调用方指定。  **[!NOTE]**  建议长度在64字符以内。 |
| icon | String | 否 | @lADOADma\*\*\*\*\*QKA | 群头像，格式为`mediaId`。需要调用[上传媒体文件](0646-upload-media-files.md)接口上传群头像，获取mediaId。 |
| mention\_all\_authority | Number | 否 | 0 | @all 权限：   - **0**（默认）：所有人都可以@all - **1**：仅群主可@all |
| show\_history\_type | Number | 否 | 0 | 新成员是否可查看聊天历史消息：   - **0**（默认）：不可以查看历史记录 - **1**：可以查看历史记录 |
| validation\_type | Number | 否 | 0 | 入群是否需要验证：   - **0**（默认）：不验证入群 - **1**：入群验证 |
| searchable | Number | 否 | 0 | 群是否可搜索：   - **0**（默认）：不可搜索 - **1**：可搜索 |
| chat\_banned\_type | Number | 否 | 0 | 是否开启群禁言：   - **0**（默认）：不禁言 - **1**：全员禁言 |
| management\_type | Number | 否 | 0 | 管理类型：   - **0**（默认）：所有人可管理 - **1**：仅群主可管理 |
| only\_admin\_can\_ding | Number | 否 | 0 | 群内发DING权限：   - **0**（默认）：所有人可发DING - **1**：仅群主和管理员可发DING |
| all\_members\_can\_create\_mcs\_conf | Number | 否 | 1 | 群会议权限：   - **0**：仅群主和管理员可发起视频和语音会议 - **1**（默认）：所有人可发起视频和语音会议 |
| all\_members\_can\_create\_calendar | Number | 否 | 0 | 群日历设置项，群内非好友/同事的成员是否可相互发起钉钉日程：   - **0**（默认）：非好友/同事的成员不可发起钉钉日程 - **1**：非好友/同事的成员可以发起钉钉日程 |
| group\_email\_disabled | Number | 否 | 0 | 是否禁止发送群邮件：   - **0**（默认）：群内成员可以对本群发送群邮件 - **1**：群内成员不可对本群发送群邮件 |
| only\_admin\_can\_set\_msg\_top | Number | 否 | 0 | 置顶群消息权限：   - **0**（默认）：所有人可置顶群消息 - **1**：仅群主和管理员可置顶群消息 |
| add\_friend\_forbidden | Number | 否 | 0 | 群成员私聊权限：   - **0**（默认）：所有人可私聊 - **1**：普通群成员之间不能够加好友、单聊，且部分功能使用受限（管理员与非管理员之间不受影响） |
| group\_live\_switch | Number | 否 | 1 | 群直播权限：   - **0**：仅群主与管理员可发起直播 - **1**（默认）：群内任意成员可发起群直播 |
| members\_to\_admin\_chat | Number | 否 | 0 | 是否禁止非管理员向管理员发起单聊：   - **0**（默认）：非管理员可以向管理员发起单聊 - **1**：禁止非管理员向管理员发起单聊 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenSceneGroupCreateResponse |  | 返回结果。 |
| open\_conversation\_id | String | cidt\*\*\*\*\*Xa4K10w== | 群ID。 |
| chat\_id | String | chat6d99a92e8x\*\*\* | 群ID。  **[!NOTE]**  老版本群ID，后续会逐步废弃此参数。 |
| success | Boolean | true | 调用是否成功。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | ed669urokuvq | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/im/chat/scenegroup/create?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "title":"测试群",
        "template_id":"c354***-***-***-b4ea-6f1ab***65",
        "owner_user_id":"022*****",
        "user_ids":"072*****,013*****",
        "subadmin_ids":"072*****,013*****",
        "uuid":"axcf*-*****-*****-23da*",
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
        "members_to_admin_chat":0
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/im/chat/scenegroup/create");
OapiImChatScenegroupCreateRequest req = new OapiImChatScenegroupCreateRequest();
req.setTitle("测试群");
req.setTemplateId("c354***-***-***-b4ea-6f1ab***65");
req.setOwnerUserId("022*****");
req.setUserIds("072*****,013*****");
req.setSubadminIds("072*****,013*****");
req.setUuid("axcf*-*****-*****-23da*");
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
OapiImChatScenegroupCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "result":{
                "open_conversation_id":"cidt*****Xa4K10w==",
                "chat_id":"chat6d99a92e8x***"
        },
        "errcode":0,
        "success":true,
        "errmsg":"ok",
        "request_id": "ed669urokuvq"
}
```

## 错误码

| 错误码（errorcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 40035 | 参数错误 | 根据接口要求，传入必要参数。 |
| 665033 | 群成员数量超出限制 | 请减少群成员数量 |
| 665036 | group template not found or offline | 请确认群模板id是否正确 |
| 660047 | scene group template permission denied, the corp list of gray rule not contain this corp | 请向模板所有者申请权限 |
| 660045 | 应用没有安装到目标企业 | 请在企业中安装应用 |
| 660046 | 企业内部应用模板，不能在其他企业使用 | 请在企业内部使用此模板 |
| 660036 | 权限校验失败 | 没有权限使用此模板 |
| 660041 | 不存在的员工 | 请确认群主的userid是否正确 |
| 400001 | 系统错误 | 请重试，若始终失败请提交工单 |
| -1 | 系统繁忙 | 请稍后再试 |
