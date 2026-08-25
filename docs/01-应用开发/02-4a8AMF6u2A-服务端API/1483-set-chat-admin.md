---
title: "更新群管理员"
source_url: "https://open.dingtalk.com/document/development/set-chat-admin"
namespace: "development"
slug: "set-chat-admin"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 即时通信 > 会话管理 > 群管理 > 更新群管理员"
doc_id: "VVYWxsq7ha"
updated_at: "2026-08-25 09:37:15"
---

> Source: https://open.dingtalk.com/document/development/set-chat-admin
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 即时通信 > 会话管理 > 群管理 > 更新群管理员
> Updated: 2026-08-25 09:37:15

# 更新群管理员

调用本接口更新群管理员，适用于群主调整群管理团队、优化群管理效率等场景。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[批量设置企业群管理员](0742-batch-setup-group-administrator.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 否 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/chat/subadmin/update`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| chatid | String | 是 | chat14432xxxx | 群会话ID，可通过[创建群](1481-session-management-creates-groups.md)接口获取chatid参数值。 |
| userids | String | 是 | userid1 | 群成员userId，可通过[根据手机号查询用户](0063-query-users-by-phone-number.md)接口获取userId参数值。 |
| role | Number | 是 | 2 | - **2**：添加为管理员。 - **3**：删除该管理员。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 是否调用成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 439gngjw9dzz | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/chat/subadmin/update?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "role":"2",
        "chatid":"chat14432xxxx",
        "userids":"userid1"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/chat/subadmin/update");
OapiChatSubadminUpdateRequest req = new OapiChatSubadminUpdateRequest();
req.setChatid("chat14432xxxx");
req.setUserids("userid1");
req.setRole(2L);
OapiChatSubadminUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "errcode": 0, 
        "success": true, 
        "errmsg": "ok", 
        "request_id": "439gngjw9dzz"
}
```

## 错误码

| 错误码（errorcode） | 错误信息（errmsg） | 解决方案 |
| --- | --- | --- |
| 40016 | 无效的chatId | 请检查chatId是否填写正确 |
| 40031 | 不合法的用户id | 请检查userId是否填写正确 |
| 49026 | 设置为管理员的人数过多 | 请减少管理员的数量 |
| 400002 | 参数错误 | 请校验参数是否符合入参要求 |
| 400001 | 系统错误 | 请稍后重试 |
