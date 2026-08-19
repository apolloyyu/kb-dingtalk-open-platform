---
title: "更新群"
source_url: "https://open.dingtalk.com/document/development/modify-a-group-session"
namespace: "development"
slug: "modify-a-group-session"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 即时通信 > 会话管理 > 群管理 > 更新群"
doc_id: "erN0VLB8Xa"
updated_at: "2026-05-13 15:50:31"
---

> Source: https://open.dingtalk.com/document/development/modify-a-group-session
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 即时通信 > 会话管理 > 群管理 > 更新群
> Updated: 2026-05-13 15:50:31

# 更新群

调用本接口更新群会话，适用于修改群相关信息，包括群名称、群主、成员列表、群头像等，适用于群管理员修改群设置、调整群成员等场景。

> **[!IMPORTANT]**
>
> 当前接口已完成升级迭代且不再支持新应用申请，存量应用调用不受影响，建议未接入的开发者使用[更新群会话](0739-api-updategroup.md)接口，已接入的开发者结合实际尽快完成迁移。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 否 | **[!IMPORTANT]**  不支持新增申请 | — |
| 第三方企业应用 | 否 | 暂不支持 | — |
| 第三方个人应用 | 否 | 暂不支持 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/chat/update`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| chatid | String | 是 | chatxxxx | 群会话ID。   - 仅支持通过调用服务端[创建群](1481-session-management-creates-groups.md)接口获取的chatid参数值。 - 不支持通过调用前端JSAPI获取的chatid。 |
| name | String | 否 | 全员群。 | 群名称，长度限制为1~20个字符。 |
| owner | String | 否 | 04201724372xxxx | 群主的userId，可通过[根据手机号查询用户](0063-query-users-by-phone-number.md)接口获取userId。  **[!NOTE]**  该员工必须为会话**useridlist**的成员之一。 |
| ownerType | String | 否 | emp | 群主类型。   - **emp**：企业员工 - **ext**：外部联系人 |
| add\_useridlist | String[] | 否 | ["userid1","userid2"] | 添加的群成员列表，每次最多支持40人，群人数上限为1000。  可通过[根据手机号查询用户](0063-query-users-by-phone-number.md)接口获取userId。 |
| del\_useridlist | String[] | 否 | ["userid1","userid2"] | 删除的成员列表，可通过[根据手机号查询用户](0063-query-users-by-phone-number.md)接口获取userId。 |
| add\_extidlist | String[] | 否 | ["userid1","userid2"] | 添加的外部联系人成员列表。 |
| del\_extidlist | String[] | 否 | ["userid1","userid2"] | 删除的外部联系人成员列表。 |
| icon | String | 否 | @mediaId | 群头像的mediaId，可通过[上传媒体文件](0646-upload-media-files.md)接口获取media\_id参数值。 |
| searchable | Number | 否 | 0 | 群是否可以被搜索。   - **0**（默认）：不可搜索 - **1**：可搜索 |
| validationType | Number | 否 | 0 | 入群是否需要验证。   - **0**（默认）：不验证 - **1**：入群验证 |
| mentionAllAuthority | Number | 否 | 0 | @all 使用范围。   - **0**（默认）：所有人可使用 - **1**：仅群主可@all |
| managementType | Number | 否 | 0 | 群管理类型。   - **0**（默认）：所有人可管理 - **1**：仅群主可管理 |
| chatBannedType | Number | 否 | 0 | 是否开启群禁言。   - **0**（默认）：不禁言 - **1**：全员禁言 |
| showHistoryType | Number | 否 | 0 | 新成员是否可查看100条历史消息。   - **1**：可查看 - **0**：不可查看   **[!NOTE]**  如果不传值，代表不可查看。 |
| isBan | boolean | 否 | true | 是否禁言。   - **true**：禁言 - **false**：不禁言 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/chat/update?access_token=ACCESS_TOKEN
```

请求正文

```
{
    "owner": "04201724372xxxx", 
    "ownerType": "emp", 
    "showHistoryType": 0, 
    "chatid": "chatxxxx", 
    "add_useridlist": [
        "user2"
    ], 
    "validationType": 0, 
    "del_useridlist": [
        "user1"
    ],  
    "add_extidlist": [
        "user1"
    ], 
     "del_extidlist": [
       "user2"
    ], 
    "icon": "@mediaId", 
    "searchable": 0, 
    "chatBannedType": 0, 
    "managementType": 0, 
    "mentionAllAuthority": 0, 
    "name": "群名称1", 
    "isBan": "true"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/chat/update");
OapiChatUpdateRequest req = new OapiChatUpdateRequest();
req.setChatid("chatxxxx");
req.setName("群名称1");
req.setOwner("04201724372xxxx");
req.setOwnerType("emp");
req.setAddUseridlist(Arrays.asList("userid2"));
req.setDelUseridlist(Arrays.asList("userid1"));
req.setAddExtidlist(Arrary.asList("userid1"));
req.setDelExtidlist(Arrary.asList("userid2"));
req.setIcon("@mediaId");
req.setIsBan(true);
req.setSearchable(0L);
req.setValidationType(0L);
req.setMentionAllAuthority(0L);
req.setManagementType(0L);
req.setChatBannedType(0L);
req.setShowHistoryType(0L);
OapiChatUpdateResponse rsp = client.execute(req,access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "errcode":"0",
        "errmsg":"ok"
}
```

## 错误码

| 错误码（errorcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 43009 | 参数需要是json格式 | 请用json格式输入参数 |
| 43007 | 没有调用权限 | 请确认应用有操作群的权限 |
| 40031 | 无效的userid列表 | 请确认userid列表是否填写正确 |
| 49000 | 需要chatid | 请确认正确填入了chatid |
| 40001 | 无效的access\_token | 请确认access\_token是否正确 |
| 40016 | 无效的chatid | 请确认chatid是否正确 |
| 49015 | 无效的群名称 | 请确认群名称是否正确 |
| 49011 | userid列表超限 | 请减少填入的userid的数量 |
| 49009 | 企业群不允许添加和删除外部联系人 | 企业内部群请不要添加和删除外部联系人 |
| 49004 | 添加和删除的人员有交集 | 请去除添加和删除人员的交集 |
| 49023 | 添加和删除外部联系人有交集 | 请去除添加和删除的外部联系人的交集 |
| 71010 | JSON解析失败 | 请使用合法的json格式 |
| -1 | 系统繁忙 | 请稍后再试 |
