---
title: "发送消息到企业群"
source_url: "https://open.dingtalk.com/document/development/send-group-messages"
namespace: "development"
slug: "send-group-messages"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 即时通信 > 消息通知 > 企业群消息 > 发送消息到企业群"
doc_id: "rHnemLx0Rn"
updated_at: "2026-08-25 09:37:19"
---

> Source: https://open.dingtalk.com/document/development/send-group-messages
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 即时通信 > 消息通知 > 企业群消息 > 发送消息到企业群
> Updated: 2026-08-25 09:37:19

# 发送消息到企业群

调用本接口发送消息到企业群。

> **[!IMPORTANT]**
>
> - 为提升接口的使用体验，当前接口计划升级，重新开放时间请[开放概览](0764-message-corpconversation-overview.md#section-rtj-q87-8ea)。
> - 不再支持新应用接入，已接入用户不受影响。

发送消息到企业群会话是指可以调用接口创建企业群会话，会以**企业名义**向企业群会话里推送消息。目前钉钉群共有5类，发送消息到企业群支持的钉钉群类型如下：

| 钉钉群类型 | 是否支持发送系统群消息 |
| --- | --- |
| 内部群 | 是 |
| 全员群 | 是 |
| 部门群 | 是 |
| 普通群 | 否 |
| 合作群 | 否 |

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/chat/send`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证，可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| chatid | String | 是 | chate39f5xxxxxx335 | 群会话的ID。   - 服务端API获取，调用[创建群](1483-session-management-creates-groups.md)接口的返回chatid字段。 - 前端API获取，小程序调用[选择会话](../03-Ogu5SlPY4t-客户端-JSAPI/0739-select-session.md)，微应用调用[根据corpid选择会话](../03-Ogu5SlPY4t-客户端-JSAPI/0798-select-session-based-on-corpid.md)。 |
| msg | JSON Object | 是 | {"msgtype":"text","text":{"content":"请提交日报。"}} | 消息内容，最长不超过2048个字节，消息类型和样例参考[消息通知类型](0775-message-types-and-data-format.md)。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| messageId | String | msgpjzCxxxxxB | 加密的消息ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/chat/send?access_token=ACCESS_TOKEN
```

请求正文

```
{
    "chatid": "chate39f5xxxxxx335",
    "msg": {
        "msgtype": "text",
        "text": {
            "content": "请于本月底提交月度工作报告。"
        }
    }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/chat/send");
OapiChatSendRequest req = new OapiChatSendRequest();
req.setChatid("chate39f5xxxxxx335");
Msg msg = new Msg();
Text text = new Text();
text.setContent("请于本月底提交月度工作报告。");
msg.setText(text);
msg.setMsgtype("text");
req.setMsg(msg);
OapiChatSendResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "errmsg": "ok",
    "messageId": "msgpjzCxxxxxB"
}
```

## 错误码

| 错误码（errorcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 43007 | 权限不足 | 请校验access\_token是否正确 |
| 34001 | 无效的chatid | 请校验chatid是否正确 |
| 34002 | 无效的消息发送者 | 请校验sender是否正确 |
| 34004 | 无效的消息类型 | 请校验消息类型是否正确 |
| 34016 | 消息内容太长 | 请缩短消息体长度 |
| 34014 | 无效的消息 | 请校验消息体是否符合json格式，消息体中内容是否按上述入参要求完整填写 |
| 40048 | 含有不安全的链接 | 请检验消息体中URL消息是否合法 |
| 40056 | 无效的agentid | 请确认是否以正确的企业进行token授权 |
| 400001 | 系统错误 | 请稍后再试 |
| -1 | 系统繁忙 | 请稍后再试 |
